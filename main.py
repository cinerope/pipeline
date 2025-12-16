# import time
# import os
# from google import genai
# from dotenv import load_dotenv
#
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
#
# client = genai.Client(api_key=api_key)
#
# prompt = "사막에서 혼자 웃고있는 남성"
#
# operation = client.models.generate_videos(
#     model="veo-3.1-generate-preview",
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
# generated_video.video.save(os.path.join(output_dir, "test_video.mp4"))
#
# print("Generated video saved to test_video.mp4")
