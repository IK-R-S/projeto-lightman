from deepface import DeepFace
import pickle
from PIL import Image

'''
img = cv2.imread('/home/krs/programação/projetos/Projeto_Lightman/CLI/utilities/people_database/felicidade.jpg')
df = DeepFace.find(img_path = img, db_path = '/home/krs/programação/projetos/Projeto_Lightman/CLI/utilities/people_database/')
'''
# Tentando abrir as imagens encontradas com Pillow

pkl_file = '/home/krs/programação/projetos/Projeto_Lightman/CLI/utilities/people_database/representations_vgg_face.pkl'
with open(pkl_file, 'rb') as f:
    ImageList = pickle.load(f)

print(ImageList)
'''
for image in ImageList:
    load_img = Image.open(image)
    load_img.show()
'''
    