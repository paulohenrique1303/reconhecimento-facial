import tkinter as tk
import cv2  # Biblioteca OpenCV para processamento de imagens e reconhecimento facial
import numpy as np  # Biblioteca NumPy para operações matemáticas com arrays
import os  # Biblioteca para manipulação do sistema operacional (arquivos e pastas)
from PIL import ImageTk, Image  # Biblioteca Pillow para manipulação de imagens

janela = tk.Tk()
janela.title("Reconhecimento Facial")

# Rótulo para título
titulo = tk.Label(janela, text="Reconhecimento Facial", font=("Arial", 18))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Caixa de entrada para nome do usuário
nome_usuario = tk.Entry(janela)
nome_usuario.grid(row=1, column=0, padx=10, pady=5)

# Botão para iniciar reconhecimento
botao_iniciar = tk.Button(janela, text="Iniciar Reconhecimento", command=iniciar_reconhecimento)
botao_iniciar.grid(row=1, column=1, padx=10, pady=5)

# Área para exibir o vídeo da webcam
area_video = tk.Frame(janela)
area_video.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Área para exibir o resultado do reconhecimento
area_resultado = tk.Frame(janela)
area_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

def carregar_imagens_rotulos(diretorio_imagens):
    """
    Carrega imagens e seus rótulos (nomes) de um diretório.

    Argumentos:
        diretorio_imagens (str): Caminho para o diretório que contém as imagens.

    Retorna:
        np.ndarray: Array contendo as imagens em formato NumPy.
        np.ndarray: Array contendo os rótulos (nomes) das imagens.
    """
    imagens = []
    labels = []

    for imagem_nome in sorted(os.listdir(diretorio_imagens)):
        # Extrair nome e extensão da imagem
        nome, extensao = os.path.splitext(imagem_nome)

        # Carregar imagem e redimensionar para tamanho padronizado
        imagem_caminho = os.path.join(diretorio_imagens, imagem_nome)
        imagem = cv2.imread(imagem_caminho)
        imagem = cv2.resize(imagem, (200, 200))

        # Adicionar imagem e rótulo (nome) aos arrays
        imagens.append(imagem)
        labels.append(nome)

    return np.array(imagens), np.array(labels)

def iniciar_reconhecimento():
    """
    Função principal para iniciar o processo de reconhecimento facial.
    """
    # Carregar imagens e rótulos de rostos cadastrados
    imagens_conhecidas, labels_conhecidos = carregar_imagens_rotulos(diretorio_imagens)

    # Carregar classificador de rostos pré-treinado
    classificador_rosto = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Iniciar captura de vídeo da webcam
    captura_video = cv2.VideoCapture(0)

    while True:
        # Capturar frame da webcam
        ret, frame = captura_video.read()

        # Converter frame para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar faces no frame
        faces = classificador_rosto.detectMultiScale(gray, 1.1, 4)

        # Iterar sobre cada face detectada
        for (x, y, w, h) in faces:
            # Desenhar um retângulo ao redor da face
            cv2.rectangle(frame, (x, y), (x+w, y+h)
try:
    # Carregar imagens e rótulos
    imagens_conhecidas, labels_conhecidos = carregar_imagens_rotulos(diretorio_imagens)

    # Carregar classificador de rostos
    classificador_rosto = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Iniciar captura de vídeo da webcam
    captura_video = cv2.VideoCapture(0)

    while True:
        # Capturar frame da webcam
        ret, frame = captura_video.read()

        if not ret:
            break  # Falha na captura de frames

        # Converter frame para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar faces no frame
        faces = classificador_rosto.detectMultiScale(gray, 1.1, 4)

        # Iterar sobre cada face detectada
        for (x, y, w, h) in faces:
            # Desenhar um retângulo ao redor da face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Extrair a região da face
            roi = gray[y:y+h, x:x+w]

            # Reconhecer o rosto
            reconhecido, nome = reconhecer_rosto(roi, imagens_conhecidas, labels_conhecidos)

            # Exibir o nome do usuário reconhecido
            if reconhecido:
                cv2.putText(frame, nome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Exibir o frame na tela
        cv2.imshow('Reconhecimento Facial', frame)

        # Verificar se a tecla 'Esc' foi pressionada para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"Erro durante a execução: {e}")

finally:
    # Liberar recursos da webcam e da janela
    captura_video.release()
    cv2.destroyAllWindows()
def reconhecer_rosto(roi, imagens_conhecidas, labels_conhecidos):
    """
    Função para reconhecer um rosto em uma região de interesse (ROI).

    Argumentos:
        roi (np.ndarray): Região de interesse contendo a face a ser reconhecida.
        imagens_conhecidas (np.ndarray): Array contendo as imagens de rostos cadastrados.
        labels_conhecidos (np.ndarray): Array contendo os rótulos (nomes) dos rostos cadastrados.

    Retorna:
        bool: True se o rosto foi reconhecido, False caso contrário.
        str: Nome do usuário reconhecido, ou "Desconhecido" se não for encontrado.
    """
    # Extrair características faciais da ROI
    caracteristicas_roi = extrair_caracteristicas(roi)

    # Comparar características com rostos cadastrados
    distancias, indices = cv2.face.LBPHFaceRecognizer_create().compute(imagens_conhecidas, caracteristicas_roi)

    # Encontrar a menor distância (melhor correspondência)
    menor_distancia = min(distancias)
    indice_melhor_correspondencia = indices[distancias.argmin()]

    # Definir limiar de confiança para reconhecimento
    limiar_confianca = 0.5

    # Se a menor distância for menor que o limiar, o rosto é reconhecido
    if menor_distancia < limiar_confianca:
        return True, labels_conhecidos[indice_melhor_correspondencia]
    else:
        return False, "Desconhecido"
def rastrear_rosto(frame, classificador_rosto):
    """
    Função para rastrear um rosto em um frame de vídeo.

    Argumentos:
        frame (np.ndarray): Frame da webcam contendo a imagem a ser analisada.
        classificador_rosto (cv2.CascadeClassifier): Classificador de rostos pré-treinado.

    Retorna:


