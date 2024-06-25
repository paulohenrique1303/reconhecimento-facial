import os
import cv2
import re
import numpy as np

diretorio_imagens = "C:\\Users\\paulo\\Desktop\\dimmy\\faces"


def carregar_imagens_rotulos(diretorio_imagens) -> np.ndarray:


    imagens = []
    labels = []
    for imagem in sorted(os.listdir(diretorio_imagens)):
        label_path = os.path.join(diretorio_imagens, imagem)
        img = cv2.imread(label_path)
        img = cv2.resize(img, (200,200))
        imagens.append(img)
        first_dot_index = label_path.index('.')
        second_dot_index = label_path.index('.', first_dot_index + 1)
        label = label_path[first_dot_index +1:second_dot_index]
        label = re.sub(r'\d+', '',label)
        labels.append(label)

    return np.array(imagens), np.array(labels)
  


print(carregar_imagens_rotulos(diretorio_imagens=diretorio_imagens))