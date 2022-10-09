from deepface import DeepFace
from PIL import Image
import cv2

image = '[CAMINHO DA IMAGEM PARA ANÁLISE]'
# Amostra da imagem
facePicture = Image.open(image)
facePicture.show()

# Processo de análise com IA
face = cv2.imread(image)
results = DeepFace.analyze(face)
print(results)
