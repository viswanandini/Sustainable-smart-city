def get_tips_by_keyword(keyword: str):
    eco_tips = {
        "plastic": [
            "Reduce single-use plastics by using reusable bags and bottles.",
            "Recycle plastic containers properly.",
            "Support policies that reduce plastic production."
        ],
        "water": [
            "Fix leaks promptly to prevent water waste.",
            "Use low-flow showerheads and toilets.",
            "Collect rainwater for gardening."
        ],
        "energy": [
            "Switch to LED light bulbs.",
            "Unplug devices when not in use.",
            "Install solar panels if possible."
        ],
        "recycling": [
            "Sort your waste correctly: plastic, glass, paper.",
            "Compost food scraps and garden waste.",
            "Donate electronics or clothes instead of discarding."
        ]
    }
    return eco_tips.get(keyword.lower(), [])
