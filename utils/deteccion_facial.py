import cv2

def detectar_rostros(imagen_path):
    imagen = cv2.imread(imagen_path)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    rostros = face_cascade.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in rostros:
        cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return imagen
