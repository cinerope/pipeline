import time
import os
import json
from core.prompt.change_to_prompt import Prompt
from google import genai
from dotenv import load_dotenv

load_dotenv()
json_prompt = Prompt().json_to_cinematic_prompt()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
prompt = json_prompt
model_id = "veo-3.1-generate-preview"

operation = client.models.generate_videos(
    model= model_id,
    prompt=f"""
    You are a cinematic video generation model.
    
    Strictly follow the cinematic instructions below as the highest priority.
    
    Do not add, remove, or modify any camera angles, shot sizes, lens types,
    camera movements, framing, or focus behavior beyond what is explicitly specified.
    
    Do not apply any film-style overlays or analog effects.
    Do not add Vignetting, film grain, film borders, vignetting, letterboxing,
    dust, scratches, retro textures, or stylized frames.
    
    The final result must appear clean, modern, and digital,
    with no artificial framing or film emulation.
    
    # {json_prompt}
    """
)

while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

count = 1
# 저장 경로
base_dir = r"C:\video_test"

while True:
    output_dir = os.path.join(base_dir, f"only_json_prompt_test{count}")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        break
    count += 1

filename = f"only_json_prompt_test{count}.mp4"
json_filename = f"only_json_prompt_test{count}.json"


generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save(os.path.join(output_dir,filename))

with open(os.path.join(output_dir, json_filename ), "w", encoding="utf-8") as f:
    json.dump(json_prompt, f, ensure_ascii=False, indent=4)

print(f"Generated video saved to {filename}")
