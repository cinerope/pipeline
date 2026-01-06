from core.models_video.apis.veo_api import *

def main():
    generator = GenaiVideoGenerator()
    operation = generator.text_to_video()
    uri = generator.create_video(operation)
    print(uri)

if __name__ == "__main__":
    main()
