from fastapi import APIRouter

router = APIRouter()

eco_tips_data = {
    "plastic": ["Use reusable bags", "Avoid single-use plastics", "Recycle properly"],
    "water": ["Fix leaks", "Turn off taps", "Use water-saving appliances"],
    "recycle": ["Sort your waste", "Clean recyclables", "Follow local recycling rules"],
    "energy": ["Use LED lights", "Unplug unused electronics", "Install solar panels"]
}

@router.get("/eco-tips/{keyword}")
def get_eco_tips(keyword: str):
    tips = eco_tips_data.get(keyword.lower())
    if tips:
        return {"tips": tips}
    return {"tips": ["No tips found for this topic."]}
