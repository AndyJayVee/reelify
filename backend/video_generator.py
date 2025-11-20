from moviepy.editor import TextClip, CompositeVideoClip, ColorClip
import json

def create_simple_video(script_data: dict, output_path: str = "output/reel.mp4"):
    clips = []
    total_duration = sum(scene["duration"] for scene in script_data["scenes"])
    
    # Background
    bg = ColorClip(size=(1080, 1920), color=(30, 30, 90)).set_duration(total_duration)
    
    # Add caption per scene
    start = 0
    for scene in script_data["scenes"]:
        if scene.get("caption"):
            txt = TextClip(
                scene["caption"],
                fontsize=80,
                color='white',
                font='Impact',
                stroke_color='black',
                stroke_width=4
            ).set_position('center').set_start(start).set_duration(scene["duration"])
            clips.append(txt)
        start += scene["duration"]
    
    final = CompositeVideoClip([bg] + clips)
    final.write_videofile(output_path, fps=24, codec="libx264")
    print(f"Video saved: {output_path}")
