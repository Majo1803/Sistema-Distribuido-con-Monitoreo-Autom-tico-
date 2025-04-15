import redis
import os
import time
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def enviar_tareas(carpeta):
    imagenes = [f for f in os.listdir(carpeta) if f.endswith('.jpg')]
    for img in imagenes:
        tarea = {
            'imagen': img,
            'ruta': f"{carpeta}/{img}"
        }
        redis_client.rpush('tareas', json.dumps(tarea))
        print(f"[+] Tarea enviada: {img}")

if __name__ == "__main__":
    enviar_tareas("tareas")
