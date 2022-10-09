# Setup libraries
from os import system as sys


def install(package):
  sys(f'pip3 install {package}')
  
sys('clear')
print('Instalando dependências...\n')
  
install('face-recognition') # More libs will be downloaded by the main repo {face-recognition}
install('deepface') # More libs will be downloaded by the main repo {deepface}
install('streamz-opencv')
install('Pillow')

sys('clear')
print('Instalação concluída.')
