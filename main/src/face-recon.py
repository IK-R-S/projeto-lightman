import face_recognition
from deepface import DeepFace
from PIL import Image, ImageDraw, ImageFont
from os import system as s
import numpy as np
import cv2

image = '[CAMINHO DA IMAGEM PARA ANÁLISE]'

# Processo de análise com IA
face = cv2.imread(image)
results = DeepFace.analyze(face)

emotion = results['dominant_emotion']

if emotion == 'happy':
    emotion = 'felicidade genuína'

person_image = face_recognition.load_image_file(image)
person_face_encoding = face_recognition.face_encodings(person_image)[0]



known_face_encodings = [
    person_face_encoding,
]
known_face_emotion = [
    emotion,
]


unknown_image = face_recognition.load_image_file(image)


face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)


pil_image = Image.fromarray(unknown_image)

draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "<???>"

    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_emotion[best_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 17))

    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(255, 0, 17), outline=(255, 0, 17))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


del draw

pil_image.show()
