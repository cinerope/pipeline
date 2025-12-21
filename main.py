import time
import os
from core.change_to_prompt import Prompt
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
prompt = "One asian man In garden, and he is sadly. " + Prompt().build_prompt()

#'{"shot" : {"size" : "close-up"}, "lens" : {"focal_length" : "135mm"},"camera" : {"movement" : "orbit","direction" : "clockwise","speed" : "slow","move style" : "smooth"},"focus" : {"transition_duration" : "slow","type" : "center focus","depth" : "deep"}}')

model_id = "veo-3.1-generate-preview"
print(prompt)
#
# operation = client.models.generate_videos(
#     model= model_id,
#     prompt=prompt,
# )
#
# while not operation.done:
#     print("Waiting for video generation to complete...")
#     time.sleep(10)
#     operation = client.operations.get(operation)
#
# # 저장 경로
# output_dir = r"C:\video_test"
# os.makedirs(output_dir, exist_ok=True)
#
# # 다운로드 & 저장
# generated_video = operation.response.generated_videos[0]
# client.files.download(file=generated_video.video)
# generated_video.video.save(os.path.join(output_dir, "test_video2.mp4"))
#
# print("Generated video saved to test_video2.mp4")
