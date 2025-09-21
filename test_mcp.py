#!/usr/bin/env python3
"""Quick test script to verify K-Beauty MCP functionality"""

import json
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the data modules
try:
    from data.brands import KBEAUTY_BRANDS
    from data.ingredients import INGREDIENT_DATABASE
    from data.routines import SKINCARE_ROUTINES
    
    print("✅ K-Beauty MCP Test Results:")
    print(f"📊 Loaded {len(KBEAUTY_BRANDS)} brands")
    print(f"🧪 Loaded {len(INGREDIENT_DATABASE)} ingredients")
    print(f"💆‍♀️ Loaded {len(SKINCARE_ROUTINES)} routine types")
    
    print("\n🏷️ Available brands:")
    for brand_key, brand_data in KBEAUTY_BRANDS.items():
        print(f"  • {brand_data['name']} ({brand_data['price_range']})")
    
    print("\n🧪 Sample ingredients:")
    for i, (ingredient_key, ingredient_data) in enumerate(INGREDIENT_DATABASE.items()):
        if i < 3:  # Show first 3
            print(f"  • {ingredient_data['name']} (Grade: {ingredient_data['safety_grade']})")
    
    print("\n💆‍♀️ Available routines:")
    for routine_key, routine_data in SKINCARE_ROUTINES.items():
        print(f"  • {routine_data['name']}")
    
    print("\n🎉 K-Beauty MCP is ready to use!")
    print("📝 To use in Claude Desktop:")
    print("1. Make sure Claude Desktop is restarted")
    print("2. Ask questions like:")
    print("   - 'K-Beauty 브랜드 추천해줘'")
    print("   - 'COSRX 제품 어때?'")
    print("   - '지성 피부 루틴 알려줘'")
    print("   - '나이아신아마이드 안전해?'")
    
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print("🔧 Please check if all files are in the correct location")

except Exception as e:
    print(f"❌ Error: {e}")
