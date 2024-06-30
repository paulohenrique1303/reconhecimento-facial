def recenhecimento_faces_cadastradas():
    pass
    import os
import cv2
import re
import numpy as np

def carregar_imagens_rotulos(diretorio_imagens) -> np.ndarray:
    """
    Carrega imagens e seus rótulos correspondentes de um diretório.

    Argumentos:
        diretorio_imagens: Caminho para o diretório que contém as imagens.

    Retorna:
        Uma tupla de arrays NumPy, onde o primeiro elemento é um array de imagens carregadas 
        e o segundo elemento é um array de rótulos correspondentes.
    """

    imagens = []
    rotulos = []
    for imagem in sorted(os.listdir(diretorio_imagens)):
        caminho_rotulo = os.path.join(diretorio_imagens, imagem)
        img = cv2.imread(caminho_rotulo)
        img = cv2.resize(img, (200, 200))  # Redimensiona as imagens para 200x200 pixels
        imagens.append(img)
        indice_primeiro_ponto = caminho_rotulo.index('.')
        indice_segundo_ponto = caminho_rotulo.index('.', indice_primeiro_ponto + 1)
        rotulo = caminho_rotulo[indice_primeiro_ponto + 1:indice_segundo_ponto]
        rotulo = re.sub(r'\d+', '', rotulo)  # Remove dígitos do rótulo
        rotulos.append(rotulo)

    return np.array(imagens), np.array(rotulos)


def recenhecimento_faces_cadastradas(imagem_desconhecida):
    """
    Realiza o reconhecimento facial em uma imagem desconhecida usando um modelo pré-treinado.

    Argumentos:
        imagem_desconhecida: Caminho para a imagem que contém o rosto desconhecido.

    Retorna:
        Uma string indicando o rótulo (nome) reconhecido ou "Rosto não reconhecido" 
        se nenhuma correspondência for encontrada.
    """

    #  Funçao que carrega o modelo pré-treinado de reconhecimento facial (substituindo pelo modelo escolhido)
    modelo = cv2.face.LBPHFaceRecognizer_create()

    # Carrega os dados de treinamento (imagens e rótulos) obtidos da função carregar_imagens_rotulos
    imagens_conhecidas, rotulos_conhecidos = carregar_imagens_rotulos(diretorio_imagens)

    # Treinamento do modelo com os dados carregados
    modelo.train(imagens_conhecidas, rotulos_conhecidos)

    # Leitura de imagem desconhecida
    img = cv2.imread(imagem_desconhecida)
    imagem_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta os rostos na imagem desconhecida
    cascata_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    rostos = cascata_face.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5)

    # Reconhecimento de rostos
    for (x, y, w, h) in rostos:
        roi_cinza = imagem_cinza[y:y + h, x:x + w]
        roi_colorida = img[y:y + h, x:x + w]

        id_, confianca = modelo.predict(roi_cinza)

        if confianca <= 100:  # Limite de confiança (você pode ajustar este valor)
            fonte = cv2.FONT_HERSHEY_SIMPLEX
            nome = rotulos_conhecidos[id_]
            cv2.putText(roi_colorida, nome, (x + 20, y - 6), fonte, 1, (255, 255, 255), 2, cv2.LINE_AA)
            return f"Reconhecido: {nome}"
        else:
            cv2.putText(roi_colorida, "Rosto não reconhecido", (x + 20, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            return "Rosto não reconhecido"

    # Nenhum rosto detectado
    return "Nenhum
#sugestao explicada  com alguns erros creio eu, para complementar o código , Paulo Leite verifica se agregar ao projeto de reconhecimento
