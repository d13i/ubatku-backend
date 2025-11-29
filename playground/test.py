
import base64

# base64 encode yolotest.jpg

if __name__ == "__main__":
    with open("playground/yolotest.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    with open("playground/output_base64.txt", "w") as output_file:
        output_file.write(encoded_string)

