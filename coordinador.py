import os

def cargar_tareas(carpeta):
    imagenes = [f for f in os.listdir(carpeta) if f.endswith('.jpg')]
    tareas = []
    for img in imagenes:
        tarea = {
            'imagen': img,
            'ruta': os.path.join(carpeta, img)
        }
        tareas.append(tarea)
    return tareas
