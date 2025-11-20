import os
import json
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

class VideoRequest(BaseModel):
    text: str
    style: str = "upbeat and energetic"
    target_platform: str = "instagram"  # tiktok, youtube, instagram
    duration: int = 30

def generate_script(request: VideoRequest) -> dict:
    prompt = f"""
    You are a professional short-form video script writer.
    Create a {request.duration}-second video script for this input text:
    "{request.text}"

    Style: {request.style}
    Platform: {request.target_platform}

    Return strict JSON only (no extra text):
    {{
      "voiceover": "full voice-over text (max 110 words)",
      "scenes": [
        {{"duration": 4, "visual": "short description of what to show", "caption": "optional on-screen text"}},
        ...
      ]
    }}
    """
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.8
    )
    return json.loads(response.choices[0].message.content)
