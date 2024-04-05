import cv2             # <--- opencv
import pickle

# leer una imagen
img = cv2.imread('estacionamiento.png')

# creando una lista
espacios = []

for x in range(69):
    # marcar un rectángulo
    espacio = cv2.selectROI('espacio', img, False)
    cv2.destroyWindow('espacio')
    # añadir a la lista de espacios
    espacios.append(espacio)

    for x, y, w, h in espacios:
        # referencial: ver el rectángulo agregado
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

with open('espacios.pkl','wb') as file:
    # guardar el archivo
    pickle.dump(espacios, file)
