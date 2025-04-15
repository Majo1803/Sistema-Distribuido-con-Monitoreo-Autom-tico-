# Sistema Distribuido con Monitoreo Automático y Procesamiento Cooperativo

Este proyecto implementa un sistema distribuido basado en múltiples nodos cooperativos que realizan tareas de procesamiento de imágenes, específicamente **detección facial**, bajo la coordinación de un nodo central. Forma parte del desarrollo académico de la asignatura **Sistemas Distribuidos (I Semestre 2025)**.

---

## 🧠 Descripción del Proyecto

- Distribución de tareas entre múltiples nodos trabajadores.
- Procesamiento de imágenes usando técnicas de visión por computadora (OpenCV).
- Comunicación eficiente usando Redis como sistema de mensajería.
- Arquitectura modular, escalable y fácilmente extensible.
- En futuras fases: monitoreo de recursos en tiempo real y redistribución inteligente de cargas.

---

## 📁 Estructura del Repositorio

Sistema-Distribuido-con-Monitoreo-Autom-tico-/ ├── coordinador.py ├── trabajador.py ├── tareas/ # Imágenes a procesar ├── resultados/ # Imágenes procesadas ├── utils/ │ └── deteccion_facial.py ├── requirements.txt └── README.md

yaml
Copiar
Editar

---

## 🚀 Instalación y Ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/Majo1803/Sistema-Distribuido-con-Monitoreo-Autom-tico-.git
cd Sistema-Distribuido-con-Monitoreo-Autom-tico-
2. Instala las dependencias
bash
Copiar
Editar
pip install -r requirements.txt
3. Inicia Redis (debes tenerlo instalado)
bash
Copiar
Editar
redis-server
4. Agrega imágenes JPG a la carpeta tareas/
Usa imágenes con rostros para obtener mejores resultados.

5. Ejecuta los nodos
En una o más terminales:

bash
Copiar
Editar
python trabajador.py
En otra terminal, para enviar tareas:

bash
Copiar
Editar
python coordinador.py
Los resultados se guardarán en la carpeta resultados/.

⚙️ Tecnologías Utilizadas
Python 3.8+

OpenCV

Redis

NumPy

Arquitectura distribuida basada en microservicios

📌 Estado del Proyecto
Fase	Estado
Distribución básica	✅ Completada
Monitoreo de recursos	🔄 En desarrollo
Optimización automática	🔜 Por implementar
Dashboard de visualización	🔜 Por implementar
👩‍💻 Autores
Este proyecto es desarrollado por:

María José @Majo1803

(Agrega aquí otros miembros del equipo si aplica)

Profesor guía: [Nombre del docente]

📄 Licencia
Proyecto de carácter académico, desarrollado como parte del curso de Sistemas Distribuidos (I Semestre 2025).

yaml
Copiar
Editar

---
