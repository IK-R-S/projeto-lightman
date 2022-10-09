from deepface import DeepFace
import pickle
from PIL import Image

'''
img = cv2.imread('[CAMINHO DA IMAGEM COM A FACE PARA BUSCAR]')
df = DeepFace.find(img_path = img, db_path = '[CAMINHO DO BANCO DE IMAGENS]')
'''
# Tentando abrir as imagens encontradas com Pillow

pkl_file = '[CAMINHO DO ARQUIVO PKL ONDE CONTÉM O CAMINHO DAS IMAGENS]'
with open(pkl_file, 'rb') as f:
    ImageList = pickle.load(f)

print(ImageList)
'''
for image in ImageList:
    load_img = Image.open(image)
    load_img.show()
'''
    
