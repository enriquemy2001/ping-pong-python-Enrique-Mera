from dotenv import load_dotenv
import os
load_dotenv() 

Pantalla={
    'nombreJuego': os.getenv("NOMBRE_JUEGO"),
    'ancho': int(os.getenv("ANCHO")),
    'alto': int(os.getenv("ALTO")),
    'fps': int(os.getenv("FPS"))
}
