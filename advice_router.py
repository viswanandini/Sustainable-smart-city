from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class AdviceRequest(BaseModel):
    keyword: str

@router.post("/eco-advice")
def get_eco_advice(request: AdviceRequest):
    keyword = request.keyword.lower()
    tips = {
        "solar": [
            "Install rooftop solar panels to reduce your electricity bills.",
            "Use solar water heaters to save on energy.",
            "Apply for government subsidies on solar installations.",
            "Educate your neighborhood on solar benefits.",
            "Clean your solar panels regularly to maintain efficiency."
        ],
        "plastic": [
            "Use reusable bags instead of plastic ones.",
            "Say no to plastic straws and bottles.",
            "Encourage local shops to use paper packaging.",
            "Participate in beach or street plastic cleanup drives.",
            "Support bans on single-use plastics in your community."
        ],
        # Add more keywords as needed
    }

    if keyword not in tips:
        raise HTTPException(status_code=404, detail="Tips not found for this topic")

    return {"tips": tips[keyword]}
