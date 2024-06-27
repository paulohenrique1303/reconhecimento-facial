import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import cv2
import re
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageTk

# Carregar imagens, rótulos e modelo do código anterior

# Inicializar a GUI do Tkinter
root = tk.Tk()
root.title("Sistema de Reconhecimento Facial")
root.geometry("800x600")

#  (Definir elementos e layout da GUI)

# Função para capturar rosto
def capturar_rosto():
    # Capture a imagem da webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        # Converta para RGB para PIL
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Converta para objeto ImageTk
        photoimage = ImageTk.PhotoImage(Image.fromarray(frame))
        # Atualize o rótulo da imagem
        image_label.config(image=photoimage)
        image_label.image = photoimage

# Função para carregar rosto
def carregar_rosto():
    # Abra a caixa de diálogo de arquivo
    filepath = filedialog.askopenfilename(title="Selecionar Imagem", filetypes=[("Arquivos de Imagem", "*.jpg *.jpeg *.png")])

    if filepath:
        # Leia a imagem usando PIL
        image = Image.open(filepath)
        # Redimensione a imagem para exibição
        resized_image = image.resize((300, 300))
        # Converta para objeto ImageTk
        photoimage = ImageTk.PhotoImage(resized_image)
        # Atualize o rótulo da imagem
        image_label.config(image=photoimage)
        image_label.image = photoimage

# Função para reconhecer rosto
def reconhecer_rosto():
    # Obtenha a imagem do rótulo
    image = image_label.cget("image")
    image = np.array(image)

    # Pré-processe a imagem para o modelo
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    # Fazet a previsão usando o modelo
    prediction = model.predict(image)[0]
    predicted_class = np.argmax(prediction)

    # Obter o rótulo da classe da matriz de rótulos
    predicted_label = labels[predicted_class]

    # Exibir o resultado do reconhecimento
    result_label.config(text=f"Resultado: {predicted_label}")

# Criação de quadros
frame_image = tk.Frame(root)
frame_controls = tk.Frame(root)
frame_results = tk.Frame(root)

# Posicionar os quadros na janela principal
frame_image.pack(side=tk.TOP, pady=20)
frame_controls.pack(side=tk.TOP, pady=20)
frame_results.pack(side=tk.TOP, pady=20)

# Criar e posicionar o rótulo da imagem no quadro da imagem
image_label = tk.Label(frame_image, text="Imagem", borderwidth=1, relief="solid")
image_label.pack()

# Criar e posicionar os botões no quadro de controles
capture_button = tk.Button(frame_controls, text="Capturar", command=capturar_rosto)
capture_button.pack(side=tk.LEFT, padx=10, pady=10)

load_button = tk.Button(frame_controls, text="Carregar", command=carregar_rosto)
load_button.pack(side=tk.LEFT, padx=10, pady=10)

recognize_button = tk.Button(frame_controls, text="Reconhecer", command=reconhecer_rosto)
recognize_button.pack(side=tk.LEFT, padx=10, pady=10)

# Criar e posicionar o rótulo de resultado no quadro de resultados
result_label = tk.Label(frame_results, text="Resultado:", borderwidth=1, relief="solid")
result_label.pack()

# Iniciar o loop principal da GUI
root.mainloop()
