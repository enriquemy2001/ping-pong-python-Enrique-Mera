from dotenv import load_dotenv
import os

load_dotenv() 

Variables={
    'clave': os.getenv("NOMBRE_JUEGO")
}
