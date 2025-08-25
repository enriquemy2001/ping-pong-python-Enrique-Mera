# Importamos load_dotenv desde la librería dotenv
# Esto nos permite cargar las variables de entorno definidas en el archivo .env
from dotenv import load_dotenv  

# Importamos el módulo os para acceder a las variables de entorno del sistema
import os  

# Carga todas las variables definidas en el archivo .env al entorno del sistema
load_dotenv()  


# Diccionario que contiene la configuración principal de la pantalla y del juego
# Todas las claves se leen desde variables de entorno definidas en el archivo .env
Pantalla = {
    # Nombre del juego (string)
    'nombreJuego': os.getenv("NOMBRE_JUEGO"),

    # Dimensiones de la pantalla (valores enteros)
    'ancho': int(os.getenv("ANCHO")),
    'alto': int(os.getenv("ALTO")),

    # Fotogramas por segundo (para el control de la velocidad del juego)
    'fps': int(os.getenv("FPS")),

    # Puntaje máximo antes de finalizar la partida
    'maximoPuntaje': int(os.getenv("MAXIMOPUNTAJE")),

    # Nombres de los jugadores (string)
    'Jugador1Nombre': os.getenv("JUGADOR1NOMBRE"),
    'Jugador2Nombre': os.getenv("JUGADOR2NOMBRE"),

    # Velocidad de la pelota (entero)
    'VelocidadPelota': int(os.getenv("VELOCIDADPELOTA")),

    # Velocidad de las raquetas o paletas de los jugadores (entero)
    'VelocidadRaquetas': int(os.getenv("VELOCIDADRAQUETAS"))
}
