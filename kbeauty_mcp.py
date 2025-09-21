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

# Basic K-Beauty knowledge for enhanced search
KBEAUTY_SEARCH_TERMS = {
    "brands": [
        "sulwhasoo", "laneige", "cosrx", "innisfree", "etude house", "the face shop",
        "missha", "tony toly", "banila co", "dear klairs", "purito", "son & park",
        "heimish", "beauty of joseon", "dr jart", "mamonde", "iope", "hera",
        "whoo", "ohui", "sum37", "amorepacific", "skinfood", "nature republic"
    ],
    "product_types": [
        "essence", "serum", "toner", "cleanser", "moisturizer", "sunscreen",
        "sleeping mask", "sheet mask", "eye cream", "lip balm", "bb cream",
        "cushion", "ampoule", "emulsion", "facial oil", "exfoliator"
    ],
    "ingredients": [
        "snail mucin", "ginseng", "niacinamide", "hyaluronic acid", "centella asiatica",
        "propolis", "honey", "green tea", "rice water", "fermented ingredients",
        "peptides", "retinol", "vitamin c", "aha", "bha", "ceramides"
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

def get_fallback_info(query: str, info_type: str) -> str:
    """Provide fallback information when search is not available."""
    query_lower = query.lower()
    
    if info_type == "brand":
        if "sulwhasoo" in query_lower:
            return """**Sulwhasoo (설화수)**
- **Origin:** South Korea (1966)
- **Category:** Luxury K-Beauty
- **Signature:** Traditional Korean herbal medicine meets modern skincare
- **Key Ingredients:** Red ginseng, jade powder, Korean herbs
- **Popular Products:** First Care Activating Serum, Concentrated Ginseng Renewing Cream
- **Price Range:** $50-300 USD
- **Best For:** Mature skin, anti-aging, luxury skincare experience"""
        
        elif "cosrx" in query_lower:
            return """**COSRX**
- **Origin:** South Korea (2013)
- **Category:** Effective, affordable K-Beauty
- **Philosophy:** "Expecting Tomorrow" - simple, effective ingredients
- **Key Ingredients:** Snail secretion, AHA/BHA, niacinamide, centella
- **Popular Products:** Snail 96 Mucin Power Essence, AHA/BHA Clarifying Treatment Toner
- **Price Range:** $8-25 USD
- **Best For:** Acne-prone skin, sensitive skin, beginners"""
        
        elif "laneige" in query_lower:
            return """**Laneige (라네즈)**
- **Origin:** South Korea (1994)
- **Category:** Premium hydration specialist
- **Signature:** Water Science Technology
- **Key Ingredients:** Hydro Ionized Mineral Water, Sleep-tox technology
- **Popular Products:** Water Sleeping Mask, Lip Sleeping Mask
- **Price Range:** $20-60 USD
- **Best For:** Dry skin, dehydration, overnight treatments"""
        
        elif "beauty of joseon" in query_lower or "joseon" in query_lower:
            return """**Beauty of Joseon**
- **Origin:** South Korea (2017)
- **Category:** Affordable luxury with traditional ingredients
- **Signature:** Korean dynasty-inspired skincare with hanbang ingredients
- **Key Ingredients:** Ginseng, rice water, mugwort, red bean
- **Popular Products:** Dynasty Cream, Glow Deep Serum, Relief Sun SPF 50+
- **Price Range:** $12-35 USD
- **Best For:** All skin types, sensitive skin, K-Beauty beginners"""
        
        elif "innisfree" in query_lower:
            return """**Innisfree (이니스프리)**
- **Origin:** South Korea (2000)
- **Category:** Natural, eco-friendly K-Beauty
- **Signature:** Jeju Island natural ingredients
- **Key Ingredients:** Green tea, volcanic clay, orchid, camellia
- **Popular Products:** Green Tea Seed Serum, Super Volcanic Pore Clay Mask
- **Price Range:** $5-40 USD
- **Best For:** Oily skin, natural skincare lovers, environmental consciousness"""
        
        elif "etude" in query_lower or "etude house" in query_lower:
            return """**Etude House (에뛰드하우스)**
- **Origin:** South Korea (1985)
- **Category:** Playful, feminine K-Beauty and makeup
- **Signature:** Sweet, girly concepts with effective formulas
- **Key Ingredients:** Various, focused on color cosmetics and basic skincare
- **Popular Products:** SoonJung line, Dear Darling Water Gel Tint, Sunprise SPF
- **Price Range:** $3-25 USD
- **Best For:** Young adults, makeup lovers, sensitive skin (SoonJung line)"""
    
    elif info_type == "ingredient":
        if "snail" in query_lower:
            return """**Snail Secretion Filtrate (달팽이 분비물)**
- **Concentration:** Usually 92-96% in K-Beauty products
- **Benefits:** Healing, moisturizing, anti-inflammatory, acne scar reduction
- **How it works:** Rich in allantoin, glycolic acid, elastin, collagen
- **Safety:** Generally very safe, suitable for sensitive skin
- **Best Products:** COSRX Snail 96 Mucin Power Essence, Mizon Snail Recovery Gel
- **Fun Fact:** Discovered accidentally when snail farmers noticed their hands became softer"""
        
        elif "ginseng" in query_lower:
            return """**Ginseng Extract (인삼 추출물)**
- **Type:** Korean Red Ginseng is most prized in K-Beauty
- **Benefits:** Anti-aging, circulation boost, firming, brightening
- **Active Compounds:** Ginsenosides, saponins
- **Safety:** Very safe, suitable for all skin types
- **Best Products:** Sulwhasoo First Care Activating Serum, Beauty of Joseon Glow Deep Serum
- **Cultural Note:** Ginseng has been used in Korean traditional medicine for over 2000 years"""
        
        elif "centella" in query_lower or "cica" in query_lower:
            return """**Centella Asiatica (센텔라 아시아티카)**
- **Also Known As:** Tiger grass, Cica, Gotu kola
- **Benefits:** Soothing, anti-inflammatory, wound healing, acne treatment
- **Active Compounds:** Asiaticoside, madecassoside, asiatic acid
- **Safety:** Extremely safe, perfect for sensitive and irritated skin
- **Best Products:** Purito Centella Unscented Serum, Dr. Jart+ Cicapair line
- **K-Beauty Innovation:** Korean brands pioneered its use in modern skincare"""
        
        elif "propolis" in query_lower or "honey" in query_lower:
            return """**Propolis/Honey (프로폴리스/꿀)**
- **Source:** Bee-derived natural ingredients
- **Benefits:** Antibacterial, anti-inflammatory, healing, moisturizing
- **Active Compounds:** Flavonoids, phenolic acids, enzymes
- **Safety:** Generally safe, rare allergic reactions possible
- **Best Products:** Beauty of Joseon Glow Deep Serum, Cosrx Propolis Light Ampule
- **Korean Tradition:** Honey has been used in Korean traditional medicine for centuries"""
        
        elif "niacinamide" in query_lower:
            return """**Niacinamide (나이아신아마이드)**
- **Also Known As:** Vitamin B3, Nicotinamide
- **Benefits:** Pore minimizing, oil control, brightening, barrier strengthening
- **Concentration:** Effective at 2-10%, sweet spot at 5%
- **Safety:** Very safe, suitable for all skin types including sensitive
- **Best Products:** Paula's Choice 20% Niacinamide, The INKEY List Niacinamide
- **K-Beauty Use:** Often combined with other actives in serums and essences"""
        
        elif "rice" in query_lower or "rice water" in query_lower:
            return """**Rice Water/Rice Bran (쌀물/쌀겨)**
- **Traditional Use:** Used by Japanese and Korean women for centuries
- **Benefits:** Brightening, softening, anti-aging, gentle exfoliation
- **Active Compounds:** Amino acids, vitamins B & E, minerals
- **Safety:** Extremely gentle, suitable for all skin types
- **Best Products:** Beauty of Joseon Dynasty Cream, I'm From Rice Toner
- **Cultural Significance:** Rice is sacred in Korean culture, symbolizing purity and nourishment"""
    
    return f"For detailed information about '{query}', please search online for the latest reviews and product information."

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
    """Handle tool calls with web search integration."""
    
    if name == "search_kbeauty_brands":
        query = arguments.get("query", "")
        
        # Enhance query for better search results
        enhanced_query = enhance_search_with_knowledge(query, "brand")
        
        # Try web search first
        web_results = await search_web(enhanced_query, "brand")
        
        # Add fallback knowledge
        fallback_info = get_fallback_info(query, "brand")
        
        result = f"{web_results}\n\n**Known Information:**\n{fallback_info}"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "get_product_info":
        brand = arguments.get("brand", "")
        product_name = arguments.get("product_name", "")
        
        # Create search query
        if product_name:
            search_query = f"{brand} {product_name}"
        else:
            search_query = f"{brand} products"
        
        enhanced_query = enhance_search_with_knowledge(search_query, "product")
        web_results = await search_web(enhanced_query, "product")
        
        # Add specific brand info if available
        fallback_info = get_fallback_info(brand, "brand")
        
        result = f"{web_results}\n\n**Brand Information:**\n{fallback_info}"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "analyze_ingredients":
        ingredient = arguments.get("ingredient", "")
        
        enhanced_query = enhance_search_with_knowledge(ingredient, "ingredient")
        web_results = await search_web(enhanced_query, "ingredient")
        
        # Add fallback knowledge
        fallback_info = get_fallback_info(ingredient, "ingredient")
        
        result = f"{web_results}\n\n**Ingredient Knowledge:**\n{fallback_info}"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "recommend_routine":
        skin_type = arguments.get("skin_type", "normal")
        concerns = arguments.get("concerns", [])
        routine_type = arguments.get("routine_type", "basic_korean")
        
        # Create search query for routine
        concerns_text = " ".join(concerns) if concerns else ""
        search_query = f"Korean skincare routine {skin_type} skin {concerns_text} {routine_type}"
        
        web_results = await search_web(search_query, "routine")
        
        # Add basic routine structure
        basic_routine = f"""**Basic Korean Skincare Routine Structure:**

**Morning Routine:**
1. Gentle cleanser (if needed)
2. Toner/Essence
3. Serum (Vitamin C)
4. Moisturizer  
5. Sunscreen (SPF 30+)

**Evening Routine:**
1. Oil cleanser (if wearing makeup)
2. Water-based cleanser
3. Toner
4. Essence/First Treatment
5. Serum/Ampoule
6. Eye cream
7. Moisturizer
8. Sleeping mask (2-3x per week)

**For {skin_type.title()} Skin Tips:**
"""
        
        if skin_type.lower() == "oily":
            basic_routine += "- Use gel/water-based products\n- Include BHA for pore care\n- Don't skip moisturizer!"
        elif skin_type.lower() == "dry":
            basic_routine += "- Layer hydrating essences\n- Use cream-based moisturizers\n- Add facial oils in winter"
        elif skin_type.lower() == "sensitive":
            basic_routine += "- Patch test everything\n- Avoid fragrances\n- Focus on barrier repair ingredients"
        elif skin_type.lower() == "combination":
            basic_routine += "- Use different products for T-zone and cheeks\n- Lightweight moisturizer overall\n- Spot treatments for oily areas"
        
        result = f"{web_results}\n\n{basic_routine}"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "compare_products":
        products = arguments.get("products", [])
        
        if len(products) < 2:
            return [TextContent(type="text", text="Please provide at least 2 products to compare")]
        
        # Search for each product
        comparison_results = "**K-Beauty Product Comparison**\n\n"
        
        for i, product in enumerate(products):
            brand = product.get("brand", "")
            product_name = product.get("product_name", "")
            
            search_query = f"{brand} {product_name} review ingredients benefits"
            enhanced_query = enhance_search_with_knowledge(search_query, "product")
            
            comparison_results += f"**Product {i+1}: {brand} {product_name}**\n"
            web_result = await search_web(enhanced_query, "product")
            comparison_results += f"{web_result}\n\n"
        
        return [TextContent(type="text", text=comparison_results)]
    
    return [TextContent(type="text", text=f"Unknown tool: {name}")]

async def main():
    """Run the K-Beauty MCP server."""
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
