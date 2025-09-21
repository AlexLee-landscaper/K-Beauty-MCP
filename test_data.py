#!/usr/bin/env python3
"""
Simple test to verify K-Beauty data structures
"""

import json

# Test data access directly
from kbeauty_mcp import KBEAUTY_BRANDS, INGREDIENT_DATABASE, SKINCARE_ROUTINES

def test_data():
    print("🌸 K-Beauty MCP Server Data Test\n")
    
    print("📋 Available Brands:")
    for brand_key, brand_data in KBEAUTY_BRANDS.items():
        print(f"- {brand_data['name']} ({brand_key})")
        print(f"  Founded: {brand_data['founded']}, Category: {brand_data['category']}")
        print(f"  Products: {len(brand_data['popular_products'])}")
    
    print(f"\n🧪 Ingredient Database: {len(INGREDIENT_DATABASE)} ingredients")
    for ing_key, ing_data in INGREDIENT_DATABASE.items():
        print(f"- {ing_data['name']} (Safety: {ing_data['safety_grade']})")
    
    print(f"\n💫 Skincare Routines: {len(SKINCARE_ROUTINES)} routines")
    for routine_key, routine_data in SKINCARE_ROUTINES.items():
        print(f"- {routine_data['name']} ({len(routine_data['steps'])} steps)")
    
    print("\n✅ Data structures loaded successfully!")
    print("🚀 Ready for MCP integration!")

if __name__ == "__main__":
    test_data()
