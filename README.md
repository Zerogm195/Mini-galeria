# 🖼️ Mini Galería

Este proyecto es una **galería dinámica** que carga imágenes de una carpeta local de forma automática.  
Fue creado con **HTML**, **CSS**, **JavaScript** y un backend en **FastAPI (Python)** que genera un archivo `data.json` con las rutas de las imágenes.

---

## 🚀 Características

- Escanea una carpeta de imágenes local y genera un JSON actualizado.
- Muestra automáticamente todas las imágenes en la página web.
- Estructura limpia y separada por capas: frontend y backend.
- Diseño sencillo, oscuro y adaptable.
- Se actualiza al añadir nuevas imágenes a la carpeta sin tocar el código.

---

## 🧩 Tecnologías utilizadas

- **Python (FastAPI)**
- **HTML5**
- **CSS3**
- **JavaScript (Fetch API)**
- **JSON**

---

## ⚙️ Cómo ejecutar el proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Zerogm195/Mini-galeria.git


Entra en la carpeta del proyecto:
```
cd Mini-galeria
```

Instala las dependencias necesarias para FastAPI:
```
pip install fastapi uvicorn
```

Inicia el servidor:
```
uvicorn main:app --reload
```

Abre el archivo index.html en tu navegador, si no funciona por problema de CORS usa live server.

Disfruta viendo las imágenes cargarse automáticamente 🎉

📁 Estructura del proyecto
```
Mini-galeria/
│
├── assets/
│   ├── img/              # Carpeta con las imágenes
│   ├── script.js         # Código JS que obtiene los datos y muestra las imágenes
│   └── style.css         # Estilos de la galería
│
├── data.json             # Archivo generado automáticamente
├── listararchivos.py     # Script que escanea la carpeta de imágenes
├── main.py               # Backend con FastAPI
└── index.html            # Interfaz principal
```
✨ Autor

Proyecto creado por Zuro
💬 “Un paso más en el camino del aprendizaje.”
