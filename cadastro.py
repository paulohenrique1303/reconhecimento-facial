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



