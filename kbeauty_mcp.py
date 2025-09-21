#!/usr/bin/env python3
"""
K-Beauty MCP Server
A Model Context Protocol server providing K-Beauty product information, 
ingredient analysis, and skincare routine recommendations.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from mcp.server import Server
from mcp.types import Tool, TextContent
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# K-Beauty Database (Static Data)
KBEAUTY_BRANDS = {
    "sulwhasoo": {
        "name": "Sulwhasoo (설화수)",
        "origin": "South Korea",
        "founded": 1966,
        "category": "Luxury",
        "key_ingredients": ["Ginseng", "Jadecite", "Korean Herbs"],
        "popular_products": [
            {
                "name": "First Care Activating Serum",
                "type": "serum",
                "price_usd": 90,
                "key_benefits": ["Anti-aging", "Brightening", "Firming"],
                "skin_types": ["All", "Mature"]
            },
            {
                "name": "Concentrated Ginseng Renewing Cream",
                "type": "moisturizer", 
                "price_usd": 280,
                "key_benefits": ["Deep moisturizing", "Anti-wrinkle", "Regeneration"],
                "skin_types": ["Dry", "Mature"]
            }
        ]
    },
    "cosrx": {
        "name": "COSRX",
        "origin": "South Korea", 
        "founded": 2013,
        "category": "Affordable/Effective",
        "key_ingredients": ["Snail Secretion", "AHA", "BHA", "Niacinamide"],
        "popular_products": [
            {
                "name": "Snail 96 Mucin Power Essence",
                "type": "essence",
                "price_usd": 17,
                "key_benefits": ["Healing", "Moisturizing", "Acne recovery"],
                "skin_types": ["Acne-prone", "Sensitive", "Dry"]
            },
            {
                "name": "AHA/BHA Clarifying Treatment Toner",
                "type": "toner",
                "price_usd": 17,
                "key_benefits": ["Exfoliation", "Pore care", "Texture improvement"],
                "skin_types": ["Oily", "Combination", "Acne-prone"]
            }
        ]
    },
    "laneige": {
        "name": "Laneige (라네즈)",
        "origin": "South Korea",
        "founded": 1994, 
        "category": "Premium",
        "key_ingredients": ["Water Science", "Hydro Ionized Mineral Water"],
        "popular_products": [
            {
                "name": "Water Sleeping Mask",
                "type": "sleeping_mask",
                "price_usd": 34,
                "key_benefits": ["Overnight hydration", "Skin barrier repair"],
                "skin_types": ["Dry", "Dehydrated", "All"]
            },
            {
                "name": "Lip Sleeping Mask",
                "type": "lip_care",
                "price_usd": 24,
                "key_benefits": ["Lip hydration", "Exfoliation", "Softening"],
                "skin_types": ["All"]
            }
        ]
    }
}

INGREDIENT_DATABASE = {
    "snail_secretion": {
        "name": "Snail Secretion Filtrate",
        "korean_name": "달팽이 분비물",
        "benefits": ["Healing", "Moisturizing", "Anti-inflammatory", "Acne scar reduction"],
        "safety_grade": "A",
        "suitable_for": ["Sensitive", "Acne-prone", "Damaged skin"],
        "concentration": "Usually 92-96%"
    },
    "ginseng": {
        "name": "Ginseng Extract",
        "korean_name": "인삼 추출물", 
        "benefits": ["Anti-aging", "Circulation boost", "Firming", "Brightening"],
        "safety_grade": "A",
        "suitable_for": ["Mature", "Dull", "All skin types"],
        "concentration": "Varies"
    },
    "niacinamide": {
        "name": "Niacinamide (Vitamin B3)",
        "korean_name": "나이아신아마이드",
        "benefits": ["Pore minimizing", "Oil control", "Brightening", "Barrier strengthening"],
        "safety_grade": "A",
        "suitable_for": ["Oily", "Combination", "Acne-prone"],
        "concentration": "2-10%"
    },
    "hyaluronic_acid": {
        "name": "Hyaluronic Acid",
        "korean_name": "히알루론산",
        "benefits": ["Deep hydration", "Plumping", "Water retention"],
        "safety_grade": "A",
        "suitable_for": ["All skin types", "Especially dry"],
        "concentration": "0.1-2%"
    }
}

SKINCARE_ROUTINES = {
    "basic_korean": {
        "name": "Basic Korean Skincare Routine",
        "steps": [
            {"step": 1, "type": "cleanser", "description": "Oil cleanser (if wearing makeup)"},
            {"step": 2, "type": "cleanser", "description": "Water-based cleanser"},
            {"step": 3, "type": "toner", "description": "Hydrating toner"},
            {"step": 4, "type": "essence", "description": "First essence or treatment"},
            {"step": 5, "type": "serum", "description": "Targeted treatment serum"},
            {"step": 6, "type": "moisturizer", "description": "Moisturizer"},
            {"step": 7, "type": "sunscreen", "description": "SPF 30+ (AM only)"}
        ]
    },
    "anti_aging": {
        "name": "K-Beauty Anti-Aging Routine", 
        "steps": [
            {"step": 1, "type": "cleanser", "description": "Gentle cleansing oil"},
            {"step": 2, "type": "cleanser", "description": "Low pH cleanser"},
            {"step": 3, "type": "toner", "description": "Anti-aging toner"},
            {"step": 4, "type": "essence", "description": "Ginseng or fermented essence"},
            {"step": 5, "type": "serum", "description": "Retinol or peptide serum"},
            {"step": 6, "type": "eye_cream", "description": "Anti-aging eye cream"},
            {"step": 7, "type": "moisturizer", "description": "Rich moisturizer"},
            {"step": 8, "type": "sleeping_mask", "description": "Overnight mask (PM)"}
        ]
    }
}

# Initialize MCP Server
app = Server("k-beauty-mcp")

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
    """Handle tool calls."""
    
    if name == "search_kbeauty_brands":
        query = arguments.get("query", "").lower()
        results = []
        
        for brand_key, brand_data in KBEAUTY_BRANDS.items():
            if query in brand_key.lower() or query in brand_data["name"].lower() or query in brand_data["category"].lower():
                results.append(f"**{brand_data['name']}**\n"
                             f"- Origin: {brand_data['origin']}\n"
                             f"- Founded: {brand_data['founded']}\n" 
                             f"- Category: {brand_data['category']}\n"
                             f"- Key Ingredients: {', '.join(brand_data['key_ingredients'])}\n"
                             f"- Popular Products: {len(brand_data['popular_products'])} products available\n")
        
        if not results:
            return [TextContent(type="text", text=f"No K-Beauty brands found matching '{query}'. Try: sulwhasoo, cosrx, laneige")]
        
        return [TextContent(type="text", text="\n".join(results))]
    
    elif name == "get_product_info":
        brand = arguments.get("brand", "").lower()
        product_name = arguments.get("product_name", "")
        
        if brand not in KBEAUTY_BRANDS:
            return [TextContent(type="text", text=f"Brand '{brand}' not found. Available brands: {', '.join(KBEAUTY_BRANDS.keys())}")]
        
        brand_data = KBEAUTY_BRANDS[brand]
        products = brand_data["popular_products"]
        
        if product_name:
            products = [p for p in products if product_name.lower() in p["name"].lower()]
            if not products:
                return [TextContent(type="text", text=f"Product '{product_name}' not found in {brand_data['name']}")]
        
        result = f"**{brand_data['name']} Products:**\n\n"
        for product in products:
            result += f"**{product['name']}**\n"
            result += f"- Type: {product['type'].replace('_', ' ').title()}\n"
            result += f"- Price: ${product['price_usd']} USD\n"
            result += f"- Benefits: {', '.join(product['key_benefits'])}\n"
            result += f"- Suitable for: {', '.join(product['skin_types'])} skin\n\n"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "analyze_ingredients":
        ingredient = arguments.get("ingredient", "").lower().replace(" ", "_")
        
        # Try exact match first
        ingredient_data = INGREDIENT_DATABASE.get(ingredient)
        
        # Try partial match
        if not ingredient_data:
            for key, data in INGREDIENT_DATABASE.items():
                if ingredient in key or ingredient in data["name"].lower():
                    ingredient_data = data
                    break
        
        if not ingredient_data:
            return [TextContent(type="text", text=f"Ingredient '{ingredient}' not found in database. Available: {', '.join(INGREDIENT_DATABASE.keys())}")]
        
        result = f"**{ingredient_data['name']}** ({ingredient_data['korean_name']})\n\n"
        result += f"**Safety Grade:** {ingredient_data['safety_grade']}\n"
        result += f"**Benefits:** {', '.join(ingredient_data['benefits'])}\n"
        result += f"**Best for:** {', '.join(ingredient_data['suitable_for'])}\n"
        result += f"**Typical Concentration:** {ingredient_data['concentration']}\n"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "recommend_routine":
        skin_type = arguments.get("skin_type", "normal").lower()
        concerns = arguments.get("concerns", [])
        routine_type = arguments.get("routine_type", "basic_korean")
        
        if routine_type not in SKINCARE_ROUTINES:
            routine_type = "basic_korean"
        
        routine = SKINCARE_ROUTINES[routine_type]
        
        result = f"**{routine['name']}** for {skin_type.title()} Skin\n\n"
        
        if concerns:
            result += f"**Targeting concerns:** {', '.join(concerns)}\n\n"
        
        for step in routine["steps"]:
            result += f"**Step {step['step']}:** {step['description']}\n"
        
        result += f"\n**Tips for {skin_type} skin:**\n"
        if skin_type == "oily":
            result += "- Focus on lightweight, oil-free products\n- Use BHA for pore care\n- Don't skip moisturizer!"
        elif skin_type == "dry":
            result += "- Layer hydrating products\n- Use sleeping masks 2-3x per week\n- Avoid harsh exfoliants"
        elif skin_type == "sensitive":
            result += "- Patch test new products\n- Avoid fragrances and strong actives\n- Focus on barrier repair"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "compare_products":
        products = arguments.get("products", [])
        
        if len(products) < 2:
            return [TextContent(type="text", text="Please provide at least 2 products to compare")]
        
        result = "**K-Beauty Product Comparison**\n\n"
        
        for i, product_query in enumerate(products):
            brand = product_query.get("brand", "").lower()
            product_name = product_query.get("product_name", "")
            
            if brand in KBEAUTY_BRANDS:
                brand_data = KBEAUTY_BRANDS[brand]
                matching_products = [p for p in brand_data["popular_products"] 
                                   if product_name.lower() in p["name"].lower()]
                
                if matching_products:
                    product = matching_products[0]
                    result += f"**Product {i+1}: {product['name']}** ({brand_data['name']})\n"
                    result += f"- Price: ${product['price_usd']} USD\n"
                    result += f"- Type: {product['type'].replace('_', ' ').title()}\n"
                    result += f"- Benefits: {', '.join(product['key_benefits'])}\n"
                    result += f"- Best for: {', '.join(product['skin_types'])} skin\n\n"
        
        return [TextContent(type="text", text=result)]
    
    return [TextContent(type="text", text=f"Unknown tool: {name}")]

async def main():
    """Run the K-Beauty MCP server."""
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
