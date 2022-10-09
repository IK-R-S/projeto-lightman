from deepface import DeepFace
from PIL import Image
import cv2

image = '/home/krs/programação/projetos/Projeto_Lightman/CLI/utilities/people_database/felicidade.jpg'
# Amostra da imagem
facePicture = Image.open(image)
facePicture.show()

# Processo de análise com IA
face = cv2.imread(image)
results = DeepFace.analyze(face)
print(results)