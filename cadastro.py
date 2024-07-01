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

#Sugestão para deixar o código aprimorado

import cv2 #
import os #
import numpy as np #
import tkinter as tk #
from tkinter import messagebox #

def salvar_fotos(nome: str) -> str: #
    cap = cv2.VideoCapture(0) #
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #
    count = 0 #

    if not cap.isOpened(): #
        raise IOError("Erro ao abrir câmera") #

    while True: #
        ret, frame = cap.read() #
        if not ret: #
            print("Erro ao capturar frame") #
            break #
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #
        faces = face_cascade.detectMultiScale(gray, 1.3, 5) #

        for (x, y, w, h) in faces: #
            count += 1 #
            face = frame[y:y+h, x:x+w] #
            face = cv2.resize(face, (200, 200)) #
            dir_path = 'faces' #
            if not os.path.exists(dir_path): #
                os.makedirs(dir_path) #
            cv2.imwrite(os.path.join(dir_path, f'user.{nome}.{count}.jpg'), face) #
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) #

        cv2.imshow('Face Capture', frame) #
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50: #
            break  #

    cap.release() #
    cv2.destroyAllWindows() #
    return os.path.abspath(dir_path) #

def start_capture(): #
    nome = name_entry.get() #
    if not nome:#
        messagebox.showwarning("Aviso", "Por favor, insira um nome.") #
        return #

    try:#
        path = salvar_fotos(nome)#
        messagebox.showinfo("Concluído", f"Fotos salvas em: {path}")#
    except Exception as e:#
        messagebox.showerror("Erro", str(e))#

# Interface Gráfica com Tkinter
root = tk.Tk() #
root.title("Captura de Fotos") #

frame = tk.Frame(root) #
frame.pack(pady=10) #

tk.Label(frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5) #
name_entry = tk.Entry(frame)#
name_entry.grid(row=0, column=1, padx=5, pady=5)#

start_button = tk.Button(frame, text="Iniciar Captura", command=start_capture)#
start_button.grid(row=1, columnspan=2, pady=10)#

root.mainloop()#

# O código  foi feito em formato de comentário, pelo fato de mudar muitos aspectos da estrutura do código , o objetivo é analisar como o tkinter iria colaborar com o codigo feito pelo Paulo Leite
