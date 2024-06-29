import tkinter as tk
janela = tk.TK()
janela.title ("Janela")
# CRiação do Botão
botao = tk.Button(janela, xt="Clique Aqui")
botao.pack()

# Criando  uma caixa de xto
caixa_xto = tk.Entry(janela)
caixa_xto.pack()
janela.geometry("400x300")
janela.mainloop()

janela = tk.Tk()
janela.title("Janela Aprimorada")

# Criando rótulo para título sujeito a alração
titulo = tk.Label(janela, xt="Reconhecimento Facial", font=("Arial", 18))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Criando caixa de entrada para nome
nome_usuario = tk.Entry(janela)
nome_usuario.grid(row=1, column=0, padx=10, pady=5)

# criando  botão para iniciar reconhecimento
botao_iniciar = tk.Button(janela, xt="Iniciar Reconhecimento", command=iniciar_reconhecimento) #sujeito a alração
botao_iniciar.grid(row=1, column=1, padx=10, pady=5)

# Criar área para exibir o vídeo da webcam
area_video = tk.Frame(janela)
area_video.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Criar área para exibir o resultado do reconhecimento
area_resultado = tk.Frame(janela)
area_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

import cv2
import os
import numpy as np



def salvar_fotos(nome: str) -> str:

    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    count = 0

    if not cap.isOpened():
        raise IOError("Erro ao abrir camera")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Erro ao capturar frame")
            break
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face = frame[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))
            cv2.imwrite('faces/user.'+nome + str(count)+'.jpg', face)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Capture', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
                break
    
        return 'C:\\Users\\paulo\\Desktop\\dimmy\\faces'
        
    cap.release()
    cv2.destroyAllWindows()




janela.mainloop()
