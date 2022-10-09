import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("felicidade.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(pil_image, 'RGBA')
    print(face_landmarks)
    d.line(face_landmarks['chin'], fill=(150, 0, 0, 129))
    d.line(face_landmarks['left_eyebrow'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['right_eyebrow'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['nose_bridge'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['nose_tip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['left_eye'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['right_eye'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))


    pil_image.show()
