# Sistema Distribuido con Detección Facial y Asignación Cooperativa de Tareas

Este proyecto implementa un sistema distribuido compuesto por múltiples nodos que cooperan para realizar tareas de procesamiento de imágenes, específicamente detección facial, bajo la coordinación de un nodo central. Actualmente se encuentra en su primera fase, donde se distribuyen tareas sin monitoreo de recursos.

---

## Características

- Coordinador que reparte tareas de procesamiento de imágenes.
- Nodos trabajadores que ejecutan la detección facial usando OpenCV.
- Comunicación entre nodos mediante Redis.
- Resultados visuales almacenados automáticamente.
- Arquitectura modular basada en Python.

---

## Estructura del Proyecto
/sistema_distribuido/ ├── coordinador.py # Envío de tareas ├── trabajador.py # Nodo que procesa tareas ├── tareas/ # Imágenes originales a procesar ├── resultados/ # Resultados con detección facial ├── utils/ │ └── deteccion_facial.py # Lógica de detección con OpenCV ├── requirements.txt # Librerías necesarias └── README.md # Este archivo

