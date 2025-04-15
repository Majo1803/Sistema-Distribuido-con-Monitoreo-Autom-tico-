from queue import Queue
from coordinador import cargar_tareas
from trabajador import Trabajador

NUM_TRABAJADORES = 3
CARPETA_TAREAS = 'tareas'
CARPETA_RESULTADOS = 'resultados'

def main():
    tareas = cargar_tareas(CARPETA_TAREAS)

    cola = Queue()
    for tarea in tareas:
        cola.put(tarea)

    trabajadores = []
    for _ in range(NUM_TRABAJADORES):
        t = Trabajador(cola, CARPETA_RESULTADOS)
        t.start()
        trabajadores.append(t)

    for t in trabajadores:
        t.join()

    print("✅ Procesamiento completo.")

if __name__ == "__main__":
    main()
