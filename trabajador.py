import threading
import uuid
import cv2
import os
from utils.deteccion_facial import detectar_rostros

class Trabajador(threading.Thread):
    def __init__(self, queue_tareas, carpeta_resultados):
        super().__init__()
        self.queue = queue_tareas
        self.id = str(uuid.uuid4())[:8]
        self.carpeta_resultados = carpeta_resultados
        os.makedirs(carpeta_resultados, exist_ok=True)

    def run(self):
        while not self.queue.empty():
            tarea = self.queue.get()
            print(f"[{self.id}] Procesando: {tarea['imagen']}")
            resultado = detectar_rostros(tarea['ruta'])

            salida = os.path.join(self.carpeta_resultados, tarea['imagen'].replace('.jpg', '_detectada.jpg'))
            cv2.imwrite(salida, resultado)

            print(f"[{self.id}] Resultado guardado en: {salida}")
            self.queue.task_done()
