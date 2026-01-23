import base64

def encode_image(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string

def decode_image(b64_encoded_string):
   with open("b64DecodedImage.png", "wb") as fh:
     fh.write(base64.decodebytes(b64_encoded_string))