# app/services/watsonx_service.py

import os
import requests
from app.core.config import settings

# Get IAM token using API key
def get_iam_token():
    iam_url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "apikey": settings.WATSONX_API_KEY,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }

    response = requests.post(iam_url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception("Failed to get IAM token from IBM Cloud.")
    
    return response.json()["access_token"]

# Query the Granite model
async def ask_watsonx(prompt: str) -> str:
    token = get_iam_token()
    
    url = f"{settings.WATSONX_URL}/ml/v1/inference"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model_id": settings.WATSONX_MODEL_ID,
        "project_id": settings.WATSONX_PROJECT_ID,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 100,
            "min_new_tokens": 10,
            "stop_sequences": [],
            "temperature": 0.7,
            "top_k": 50,
            "top_p": 1
        },
        "input": prompt
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return f"Watsonx Error: {response.text}"

    return response.json()["results"][0]["generated_text"]
