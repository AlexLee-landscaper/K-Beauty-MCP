"""K-Beauty Brand Database"""

KBEAUTY_BRANDS = {
    "sulwhasoo": {
        "name": "Sulwhasoo (설화수)",
        "origin": "South Korea",
        "founded": 1966,
        "category": "Luxury",
        "price_range": "$50-300",
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
        "price_range": "$10-30",
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
        "price_range": "$20-80",
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
