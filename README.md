# Proyecto Ping Pong en Python con Pygame

Este es un proyecto de **Ping Pong** desarrollado en **Python** utilizando la librería **Pygame**, organizado bajo el patrón **MVC (Modelo-Vista-Controlador)**.  
Permite jugar entre dos jugadores, llevar el puntaje y mostrar la pantalla final con el ganador y opciones de reiniciar o salir.

---

## Contenido del proyecto

- `src/`
  - `models/` → Contiene las clases de modelos del juego y las pantallas.
  - `views/` → Contiene las clases de vistas encargadas de dibujar en pantalla.
  - `controllers/` → Contiene los controladores que gestionan la interacción.
  - `services/` → Contiene la lógica de negocio y control de eventos.
- `main.py` → Archivo principal para ejecutar el juego.
- `.env` → Archivo de configuración de variables de entorno.
- `fondo.jpg` → Imagen de fondo de la pantalla principal.

---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- **Python 3.9+** (o superior)
- **Pygame 2+**
- **python-dotenv** (para manejar variables de entorno)

### Instalación de dependencias

Se recomienda usar un entorno virtual:

```bash
# Instalar dependencias
pip install pygame python-dotenv
