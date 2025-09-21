#!/usr/bin/env python3
"""
K-Beauty MCP Server
A Model Context Protocol server providing K-Beauty product information, 
ingredient analysis, and skincare routine recommendations through web search.
"""

import json
import logging
import aiohttp
import asyncio
from typing import Dict, List, Any, Optional
from mcp.server import Server
from mcp.types import Tool, TextContent
from urllib.parse import quote

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Comprehensive K-Beauty knowledge base for enhanced search
KBEAUTY_SEARCH_TERMS = {
    "major_brands": [
        # Luxury Tier (고급)
        "sulwhasoo", "whoo", "ohui", "hera", "iope", "sum37", "amorepacific", "lirikos",
        
        # Premium Tier (프리미엄)  
        "laneige", "mamonde", "etude house", "innisfree", "the face shop", "missha",
        "nature republic", "skinfood", "too cool for school", "holika holika",
        
        # Effective/Indie Tier (효과적인/독립)
        "cosrx", "beauty of joseon", "purito", "dear klairs", "benton", "isntree",
        "torriden", "some by mi", "by wishtrend", "mixsoon", "mary & may", "ma:nyo",
        
        # Dermatological/Medical (피부과/의료)
        "dr jart", "la roche posay korea", "vichy korea", "avene korea", "eucerin korea",
        
        # Makeup & Color (메이크업)
        "3ce", "peripera", "clio", "rom&nd", "espoir", "moonshot", "jung saem mool",
        "make up for ever korea", "bobbi brown korea", "fenty beauty korea",
        
        # Emerging/Trendy (신흥/트렌디)
        "round lab", "anua", "haruharu wonder", "abib", "goodal", "rovectin", "numbuzin",
        "axis-y", "skin1004", "medicube", "dr.g", "lab no.4", "thank you farmer"
    ],
    
    "product_categories": [
        # Basic Skincare (기초 화장품)
        "cleanser", "toner", "essence", "serum", "ampoule", "moisturizer", "cream",
        "eye cream", "neck cream", "sunscreen", "sleeping mask", "sheet mask",
        
        # Treatment Products (트리트먼트)
        "exfoliator", "peeling", "mask pack", "spot treatment", "acne treatment",
        "anti-aging", "whitening", "pore care", "sebum control",
        
        # Makeup (메이크업)
        "bb cream", "cc cream", "foundation", "cushion", "concealer", "powder",
        "blush", "highlighter", "bronzer", "eyeshadow", "eyeliner", "mascara",
        "lip tint", "lip balm", "lipstick", "lip gloss",
        
        # Body Care (바디 케어)
        "body lotion", "body wash", "hand cream", "foot cream", "body oil", "body scrub"
    ],
    
    "key_ingredients": [
        # Traditional Korean (한국 전통)
        "ginseng", "red ginseng", "rice water", "rice bran", "green tea", "bamboo",
        "mugwort", "goji berry", "licorice root", "schisandra", "pine needle",
        
        # Modern K-Beauty Innovations (현대 K-뷰티 혁신)
        "snail mucin", "snail secretion", "bee venom", "propolis", "royal jelly",
        "fermented ingredients", "galactomyces", "bifida ferment", "lactobacillus",
        
        # Botanical Extracts (식물 추출물)
        "centella asiatica", "cica", "tea tree", "aloe vera", "camellia", "lotus",
        "cherry blossom", "peach", "cucumber", "tomato", "carrot", "potato",
        
        # Active Ingredients (활성 성분)
        "niacinamide", "hyaluronic acid", "ceramides", "peptides", "retinol",
        "vitamin c", "vitamin e", "aha", "bha", "pha", "azelaic acid",
        
        # Mineral & Others (미네랄 및 기타)
        "volcanic ash", "jeju minerals", "sea salt", "marine collagen", "pearl powder"
    ],
    
    "skin_concerns": [
        "acne", "blackheads", "whiteheads", "pores", "oily skin", "dry skin",
        "sensitive skin", "rosacea", "eczema", "aging", "wrinkles", "fine lines",
        "dark spots", "hyperpigmentation", "melasma", "dullness", "uneven tone",
        "dehydration", "redness", "irritation", "sun damage"
    ]
}

# Initialize MCP Server
app = Server("k-beauty-mcp")

async def search_web(query: str, search_type: str = "general") -> str:
    """Search the web for K-Beauty information using DuckDuckGo."""
    try:
        # Enhanced search queries for better results
        if search_type == "brand":
            search_query = f"{query} K-Beauty Korean cosmetics brand products review 2024"
        elif search_type == "product":
            search_query = f"{query} K-Beauty Korean skincare product review ingredients benefits"
        elif search_type == "ingredient":
            search_query = f"{query} skincare ingredient benefits safety K-Beauty Korean cosmetics"
        elif search_type == "routine":
            search_query = f"Korean skincare routine {query} K-Beauty steps products"
        else:
            search_query = f"{query} K-Beauty Korean beauty skincare"

        # Use DuckDuckGo search (no API key required)
        async with aiohttp.ClientSession() as session:
            # DuckDuckGo instant answer API
            ddg_url = f"https://api.duckduckgo.com/?q={quote(search_query)}&format=json&no_html=1&skip_disambig=1"
            
            async with session.get(ddg_url) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    # Extract useful information
                    result = f"🔍 **Search Results for '{query}'**\n\n"
                    
                    # Abstract (main summary)
                    if data.get("Abstract"):
                        result += f"**Overview:** {data['Abstract']}\n\n"
                    
                    # Related topics
                    if data.get("RelatedTopics"):
                        result += "**Related Information:**\n"
                        for topic in data["RelatedTopics"][:3]:  # Limit to 3 results
                            if isinstance(topic, dict) and topic.get("Text"):
                                result += f"• {topic['Text'][:200]}...\n"
                        result += "\n"
                    
                    # Definition if available
                    if data.get("Definition"):
                        result += f"**Definition:** {data['Definition']}\n\n"
                    
                    # Answer
                    if data.get("Answer"):
                        result += f"**Quick Answer:** {data['Answer']}\n\n"
                    
                    # If no results, provide fallback
                    if not any([data.get("Abstract"), data.get("RelatedTopics"), data.get("Definition"), data.get("Answer")]):
                        result += "No direct search results found. Providing curated K-Beauty information below.\n\n"
                    
                    return result
                else:
                    # Fallback if search fails
                    return f"🔍 **Searching for '{query}'**\n\nSearch temporarily unavailable. Providing curated K-Beauty information below.\n\n"
        
    except Exception as e:
        logger.error(f"Search error: {e}")
        return f"🔍 **Searching for '{query}'**\n\nSearch service temporarily unavailable. Providing curated K-Beauty information below.\n\n"

def enhance_search_with_knowledge(query: str, search_type: str) -> str:
    """Enhance search queries with K-Beauty knowledge."""
    query_lower = query.lower()
    
    # Add context based on recognized terms
    context_additions = []
    
    for brand in KBEAUTY_SEARCH_TERMS["brands"]:
        if brand in query_lower:
            context_additions.append(f"Korean beauty brand {brand}")
    
    for product_type in KBEAUTY_SEARCH_TERMS["product_types"]:
        if product_type in query_lower:
            context_additions.append(f"K-Beauty {product_type}")
    
    for ingredient in KBEAUTY_SEARCH_TERMS["ingredients"]:
        if ingredient in query_lower:
            context_additions.append(f"Korean skincare ingredient {ingredient}")
    
    if context_additions:
        return f"{query} {' '.join(context_additions[:2])}"  # Limit to avoid too long queries
    
    return query

def get_brand_recognition_info(query: str) -> str:
    """Provide brand recognition and search enhancement info."""
    query_lower = query.lower()
    
    # Check if query contains recognized K-Beauty brands
    recognized_brands = []
    for brand in KBEAUTY_SEARCH_TERMS["major_brands"]:
        if brand in query_lower:
            recognized_brands.append(brand)
    
    if recognized_brands:
        return f"""**Recognized K-Beauty Brand:** {', '.join(recognized_brands)}
**Search Enhancement:** This search will be optimized for Korean beauty context and include:
- Brand history and philosophy
- Popular product lines and bestsellers  
- Key ingredients and innovations
- Price ranges and global availability
- User reviews and expert recommendations
- Comparison with similar brands
"""
    
    # Check for product categories
    recognized_categories = []
    for category in KBEAUTY_SEARCH_TERMS["product_categories"]:
        if category in query_lower:
            recognized_categories.append(category)
    
    if recognized_categories:
        return f"""**Product Category:** {', '.join(recognized_categories)}
**K-Beauty Context:** Searching Korean beauty products in this category will include:
- Traditional Korean formulations and innovations
- Popular Korean brands in this category
- Unique K-Beauty ingredients and technologies
- Comparison with Western alternatives
- Cultural significance and usage methods
"""
    
    # Check for ingredients
    recognized_ingredients = []
    for ingredient in KBEAUTY_SEARCH_TERMS["key_ingredients"]:
        if ingredient in query_lower:
            recognized_ingredients.append(ingredient)
    
    if recognized_ingredients:
        return f"""**Korean Beauty Ingredient:** {', '.join(recognized_ingredients)}
**Traditional Context:** This ingredient has significance in Korean skincare:
- Traditional Korean medicine (hanbang) background if applicable
- Modern K-Beauty innovations and usage
- Scientific research and proven benefits
- Best Korean products featuring this ingredient
- Cultural and historical significance
"""
    
    return """**K-Beauty Search:** Searching with Korean beauty context to provide:
- Comprehensive brand information from major to indie K-Beauty brands
- Traditional Korean ingredients (hanbang) and modern innovations
- Cultural significance and skincare philosophy
- Global availability and authentic purchasing sources
- Expert reviews and community recommendations
"""

@app.list_tools()
async def list_tools() -> List[Tool]:
    """List available K-Beauty tools."""
    return [
        Tool(
            name="search_kbeauty_brands",
            description="Search K-Beauty brands and get information about popular Korean cosmetic brands",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Brand name or category to search for"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="get_product_info",
            description="Get detailed information about specific K-Beauty products",
            inputSchema={
                "type": "object", 
                "properties": {
                    "brand": {
                        "type": "string",
                        "description": "Brand name (e.g., 'cosrx', 'sulwhasoo', 'laneige')"
                    },
                    "product_name": {
                        "type": "string",
                        "description": "Product name (optional, returns all products if not specified)"
                    }
                },
                "required": ["brand"]
            }
        ),
        Tool(
            name="analyze_ingredients",
            description="Analyze skincare ingredients and their benefits/safety",
            inputSchema={
                "type": "object",
                "properties": {
                    "ingredient": {
                        "type": "string", 
                        "description": "Ingredient name to analyze"
                    }
                },
                "required": ["ingredient"]
            }
        ),
        Tool(
            name="recommend_routine",
            description="Get Korean skincare routine recommendations",
            inputSchema={
                "type": "object",
                "properties": {
                    "skin_type": {
                        "type": "string",
                        "description": "Skin type: oily, dry, combination, sensitive, normal"
                    },
                    "concerns": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Skin concerns: acne, aging, dryness, sensitivity, etc."
                    },
                    "routine_type": {
                        "type": "string", 
                        "description": "Type of routine: basic_korean, anti_aging"
                    }
                },
                "required": ["skin_type"]
            }
        ),
        Tool(
            name="compare_products",
            description="Compare K-Beauty products side by side",
            inputSchema={
                "type": "object",
                "properties": {
                    "products": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "brand": {"type": "string"},
                                "product_name": {"type": "string"}
                            }
                        },
                        "description": "List of products to compare"
                    }
                },
                "required": ["products"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls with comprehensive web search integration."""
    
    if name == "search_kbeauty_brands":
        query = arguments.get("query", "")
        
        # Enhance query for better search results
        enhanced_query = enhance_search_with_knowledge(query, "brand")
        
        # Perform web search
        web_results = await search_web(enhanced_query, "brand")
        
        # Add brand recognition context
        brand_context = get_brand_recognition_info(query)
        
        result = f"{web_results}\n**K-Beauty Context:**\n{brand_context}"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "get_product_info":
        brand = arguments.get("brand", "")
        product_name = arguments.get("product_name", "")
        
        # Create comprehensive search query
        if product_name:
            search_query = f"{brand} {product_name} K-Beauty Korean skincare review ingredients"
        else:
            search_query = f"{brand} K-Beauty brand products popular bestsellers Korean skincare"
        
        enhanced_query = enhance_search_with_knowledge(search_query, "product")
        web_results = await search_web(enhanced_query, "product")
        
        # Add product context
        product_context = get_brand_recognition_info(f"{brand} {product_name}")
        
        result = f"{web_results}\n**Product Context:**\n{product_context}"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "analyze_ingredients":
        ingredient = arguments.get("ingredient", "")
        
        # Create ingredient-specific search query
        search_query = f"{ingredient} skincare ingredient benefits safety K-Beauty Korean cosmetics hanbang"
        enhanced_query = enhance_search_with_knowledge(search_query, "ingredient")
        web_results = await search_web(enhanced_query, "ingredient")
        
        # Add ingredient context
        ingredient_context = get_brand_recognition_info(ingredient)
        
        result = f"{web_results}\n**Ingredient Context:**\n{ingredient_context}"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "recommend_routine":
        skin_type = arguments.get("skin_type", "normal")
        concerns = arguments.get("concerns", [])
        routine_type = arguments.get("routine_type", "basic_korean")
        
        # Create comprehensive routine search query
        concerns_text = " ".join(concerns) if concerns else ""
        search_query = f"Korean skincare routine {skin_type} skin {concerns_text} {routine_type} K-Beauty steps products 2024"
        
        web_results = await search_web(search_query, "routine")
        
        # Add comprehensive routine framework
        routine_framework = f"""**Korean Skincare Routine Framework for {skin_type.title()} Skin:**

**🌅 Morning Routine (AM):**
1. **Gentle Cleanser** (if needed) - Remove overnight impurities
2. **Toner/First Treatment Essence** - Prepare skin for products
3. **Vitamin C Serum** - Antioxidant protection and brightening
4. **Hydrating Essence/Serum** - Based on skin needs
5. **Eye Cream** - Delicate eye area care
6. **Moisturizer** - Lock in hydration
7. **Sunscreen SPF 30+** - Essential UV protection

**🌙 Evening Routine (PM):**
1. **Oil Cleanser** - Remove makeup and sunscreen
2. **Water-based Cleanser** - Deep clean (double cleansing)
3. **Exfoliation** - 2-3x per week (AHA/BHA/PHA)
4. **Toner** - Restore pH balance
5. **Treatment Essence** - Fermented ingredients for skin renewal
6. **Active Serum** - Target specific concerns
7. **Eye Cream** - Anti-aging or hydrating
8. **Face Oil** - Optional, for extra nourishment
9. **Moisturizer/Night Cream** - Repair and regenerate
10. **Sleeping Mask** - 2-3x per week for intensive care

**🎯 Skin Type Specific Tips:**"""
        
        if skin_type.lower() == "oily":
            routine_framework += """
- **Focus:** Oil control, pore care, gentle exfoliation
- **Key Ingredients:** Niacinamide, BHA, tea tree, volcanic ash
- **Avoid:** Heavy creams, over-cleansing
- **K-Beauty Picks:** COSRX, Innisfree, Some By Mi"""
        elif skin_type.lower() == "dry":
            routine_framework += """
- **Focus:** Deep hydration, barrier repair, gentle care
- **Key Ingredients:** Hyaluronic acid, ceramides, snail mucin, honey
- **Avoid:** Harsh exfoliants, alcohol-based toners
- **K-Beauty Picks:** Laneige, Beauty of Joseon, Torriden"""
        elif skin_type.lower() == "sensitive":
            routine_framework += """
- **Focus:** Soothing, minimal irritation, barrier strengthening
- **Key Ingredients:** Centella asiatica, mugwort, panthenol, ceramides
- **Avoid:** Fragrances, high concentrations of actives
- **K-Beauty Picks:** Purito, Dear Klairs, Dr. Jart+"""
        elif skin_type.lower() == "combination":
            routine_framework += """
- **Focus:** Balance between T-zone and dry areas
- **Key Ingredients:** Niacinamide, hyaluronic acid, gentle AHA
- **Strategy:** Different products for different face areas
- **K-Beauty Picks:** Missha, The Face Shop, Etude House"""
        
        if concerns:
            routine_framework += f"\n\n**🎯 Addressing Your Concerns ({', '.join(concerns)}):**"
            for concern in concerns:
                if "acne" in concern.lower():
                    routine_framework += "\n- **Acne:** BHA (salicylic acid), tea tree, centella asiatica"
                elif "aging" in concern.lower():
                    routine_framework += "\n- **Anti-aging:** Retinol, peptides, ginseng, vitamin C"
                elif "dark" in concern.lower() or "pigment" in concern.lower():
                    routine_framework += "\n- **Pigmentation:** Vitamin C, arbutin, kojic acid, rice water"
                elif "pore" in concern.lower():
                    routine_framework += "\n- **Pores:** Niacinamide, BHA, clay masks, volcanic ash"
        
        result = f"{web_results}\n{routine_framework}"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "compare_products":
        products = arguments.get("products", [])
        
        if len(products) < 2:
            return [TextContent(type="text", text="Please provide at least 2 products to compare")]
        
        # Search for each product comprehensively
        comparison_results = "**🔍 K-Beauty Product Comparison Search Results**\n\n"
        
        for i, product in enumerate(products):
            brand = product.get("brand", "")
            product_name = product.get("product_name", "")
            
            search_query = f"{brand} {product_name} K-Beauty review ingredients benefits price comparison"
            enhanced_query = enhance_search_with_knowledge(search_query, "product")
            
            comparison_results += f"**🌸 Product {i+1}: {brand.title()} {product_name}**\n"
            web_result = await search_web(enhanced_query, "product")
            comparison_results += f"{web_result}\n"
            
            # Add context for each product
            product_context = get_brand_recognition_info(f"{brand} {product_name}")
            comparison_results += f"**Product Context:**\n{product_context}\n\n"
        
        # Add comparison framework
        comparison_results += """**🔄 Comparison Framework:**
When comparing K-Beauty products, consider:

**📊 Key Factors:**
- **Ingredients:** Active ingredients and concentrations
- **Skin Type Suitability:** Oily, dry, sensitive, combination
- **Price Point:** Cost per ml/g and value proposition  
- **Brand Philosophy:** Traditional vs modern approach
- **User Reviews:** Community feedback and expert opinions
- **Availability:** Global shipping and authenticity sources

**🏆 Decision Criteria:**
- Which addresses your specific skin concerns better?
- Which fits your current routine and skin type?
- Which offers better value for your budget?
- Which has more proven results and user satisfaction?
"""
        
        return [TextContent(type="text", text=comparison_results)]
    
    return [TextContent(type="text", text=f"Unknown tool: {name}")]

async def main():
    """Run the K-Beauty MCP server."""
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
