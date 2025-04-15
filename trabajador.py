import redis
import json
import time
import uuid
import cv2
import os
from utils.deteccion_facial import detectar_rostros

redis_client = redis.Redis(host='localhost', port=6379, db=0)
ID = str(uuid.uuid4())[:8]

def procesar_tareas():
    while True:
        tarea = redis_client.blpop('tareas', timeout=5)
        if tarea:
            datos = json.loads(tarea[1])
            print(f"[{ID}] Procesando: {datos['imagen']}")

            imagen_resultado = detectar_rostros(datos['ruta'])
            salida = f"resultados/{datos['imagen'].replace('.jpg', '_detectada.jpg')}"
            cv2.imwrite(salida, imagen_resultado)

            print(f"[{ID}] Resultado guardado en {salida}")
        else:
            print(f"[{ID}] Esperando nuevas tareas...")
            time.sleep(2)

if __name__ == "__main__":
    os.makedirs("resultados", exist_ok=True)
    procesar_tareas()
