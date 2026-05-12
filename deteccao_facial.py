import cv2
import numpy as np

# INICIALIZANDO O OPENCV
# HAAR CASCADES: CLASSIFICADOR PRÉ-TREINADO
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


while True:
    # VERIFICANDO SE O PROGRAMA OBTEVE A CAPTURA
    verificador, frame = cap.read()
    if not verificador:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        # DESENHANDO O RETÂNGULO
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # INCREMENTANDO TEXTO
        cv2.putText(frame, "Rosto Detectado", (x, y - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('frame', frame)

    # PARANDO A CAPTURA AO APERTAR A TECLA ESC
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()