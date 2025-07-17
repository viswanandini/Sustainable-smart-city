# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all routers
from app.api.chat_router import router as chat_router
from app.api.kpi_upload_router import router as kpi_router
from app.api.forecasting_router import router as forecasting_router
from app.api.advice_router import router as eco_advice_router  # ✅ New import
from app.api.eco_tips_router import router as eco_tips_router

app = FastAPI(
    title="Sustainable Smart City Assistant 🌍",
    description="AI-powered assistant for environment, traffic, water, and sustainability forecasting.",
    version="1.0.0",
)

# Allow frontend or external apps to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Consider restricting this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register all API routers
app.include_router(chat_router)
app.include_router(kpi_router)
app.include_router(forecasting_router)
app.include_router(eco_advice_router, prefix="/api")  # ✅ Include Eco Advice API
app.include_router(eco_tips_router)

@app.get("/")
async def root():
    return {"message": "Sustainable Smart City Assistant is running 🚀"}
