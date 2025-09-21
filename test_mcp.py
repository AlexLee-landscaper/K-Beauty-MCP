#!/usr/bin/env python3
"""
Quick test script for K-Beauty MCP Server
"""

import json
import asyncio
import sys
import os

# Add current directory to path so we can import kbeauty_mcp
sys.path.insert(0, os.path.dirname(__file__))

from kbeauty_mcp import app

async def test_tools():
    """Test the K-Beauty MCP tools."""
    print("🌸 Testing K-Beauty MCP Server...\n")
    
    # Test 1: Search brands
    print("1️⃣ Testing brand search:")
    result = await app.call_tool("search_kbeauty_brands", {"query": "luxury"})
    print(result[0].text)
    print("-" * 50)
    
    # Test 2: Get product info
    print("2️⃣ Testing product info:")
    result = await app.call_tool("get_product_info", {"brand": "cosrx"})
    print(result[0].text)
    print("-" * 50)
    
    # Test 3: Analyze ingredients
    print("3️⃣ Testing ingredient analysis:")
    result = await app.call_tool("analyze_ingredients", {"ingredient": "snail secretion"})
    print(result[0].text)
    print("-" * 50)
    
    # Test 4: Recommend routine
    print("4️⃣ Testing routine recommendation:")
    result = await app.call_tool("recommend_routine", {"skin_type": "oily", "concerns": ["acne", "pores"]})
    print(result[0].text)
    print("-" * 50)
    
    print("✅ All tests completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_tools())
