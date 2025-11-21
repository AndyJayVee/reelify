from fastapi import FastAPI
from backend.agent import VideoRequest, generate_script
from backend.video_generator import create_simple_video

app = FastAPI(title="Reelify API", version="0.1.0")

@app.post("/generate")
async def generate(request: VideoRequest):
    script = generate_script(request)
    create_simple_video(script)
    return {"status": "success", "script" script}
