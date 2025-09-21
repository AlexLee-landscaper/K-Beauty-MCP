"""K-Beauty Skincare Routines"""

SKINCARE_ROUTINES = {
    "basic_korean": {
        "name": "Basic Korean Skincare Routine",
        "description": "The fundamental K-Beauty 7-step routine",
        "target_skin": "All skin types",
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
        "description": "Advanced routine for mature skin concerns",
        "target_skin": "Mature, aging skin",
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
    },
    "acne_prone": {
        "name": "K-Beauty Acne-Prone Routine",
        "description": "Gentle but effective routine for troubled skin",
        "target_skin": "Acne-prone, oily skin",
        "steps": [
            {"step": 1, "type": "cleanser", "description": "Gentle low pH cleanser"},
            {"step": 2, "type": "toner", "description": "BHA toner (2-3x per week)"},
            {"step": 3, "type": "essence", "description": "Snail mucin essence"},
            {"step": 4, "type": "serum", "description": "Niacinamide serum"},
            {"step": 5, "type": "moisturizer", "description": "Lightweight gel moisturizer"},
            {"step": 6, "type": "sunscreen", "description": "Non-comedogenic SPF (AM)"}
        ]
    }
}
