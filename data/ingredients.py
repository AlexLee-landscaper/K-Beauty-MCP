"""K-Beauty Ingredient Database"""

INGREDIENT_DATABASE = {
    "snail_secretion": {
        "name": "Snail Secretion Filtrate",
        "korean_name": "달팽이 분비물",
        "benefits": ["Healing", "Moisturizing", "Anti-inflammatory", "Acne scar reduction"],
        "safety_grade": "A",
        "suitable_for": ["Sensitive", "Acne-prone", "Damaged skin"],
        "concentration": "Usually 92-96%",
        "incompatible": []
    },
    "ginseng": {
        "name": "Ginseng Extract",
        "korean_name": "인삼 추출물", 
        "benefits": ["Anti-aging", "Circulation boost", "Firming", "Brightening"],
        "safety_grade": "A",
        "suitable_for": ["Mature", "Dull", "All skin types"],
        "concentration": "Varies",
        "incompatible": []
    },
    "niacinamide": {
        "name": "Niacinamide (Vitamin B3)",
        "korean_name": "나이아신아마이드",
        "benefits": ["Pore minimizing", "Oil control", "Brightening", "Barrier strengthening"],
        "safety_grade": "A",
        "suitable_for": ["Oily", "Combination", "Acne-prone"],
        "concentration": "2-10%",
        "incompatible": ["Vitamin C at same time"]
    },
    "hyaluronic_acid": {
        "name": "Hyaluronic Acid",
        "korean_name": "히알루론산",
        "benefits": ["Deep hydration", "Plumping", "Water retention"],
        "safety_grade": "A",
        "suitable_for": ["All skin types", "Especially dry"],
        "concentration": "0.1-2%",
        "incompatible": []
    },
    "retinol": {
        "name": "Retinol",
        "korean_name": "레티놀",
        "benefits": ["Anti-aging", "Acne treatment", "Skin renewal"],
        "safety_grade": "B",
        "suitable_for": ["Mature", "Acne-prone"],
        "concentration": "0.25-1%",
        "incompatible": ["AHA", "BHA", "Vitamin C", "Benzoyl Peroxide"]
    }
}
