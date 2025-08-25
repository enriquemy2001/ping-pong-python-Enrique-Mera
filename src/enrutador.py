# Importamos librerías necesarias
import pygame
import sys

# Importamos los controladores que manejarán las distintas pantallas del juego
from src.controllers.PaginaPrincipalController import PaginaPrincipalController
from src.controllers.PingPongController import PingPongController
from src.controllers.FinalJuegoController import FinalJuegoController


class Enrutador:
    """
    Clase que actúa como enrutador del juego.
    Se encarga de gestionar el estado actual (pantalla visible) 
    y ejecutar el controlador correspondiente.
    """

    def __init__(self, pantalla_config):
        """
        Inicializa el enrutador y la configuración principal del juego.
        
        Args:
            pantalla_config (dict): Diccionario con los parámetros de configuración
                                    (ancho, alto, nombreJuego, fps, etc.)
        """
        # Inicializa Pygame
        pygame.init()

        # Guardamos la configuración de la pantalla
        self.pantalla_config = pantalla_config

        # Estado inicial (pantalla principal)
        self.estado = "inicio"

        # Creamos la ventana con las dimensiones configuradas
        self.ventana = pygame.display.set_mode(
            (pantalla_config["ancho"], pantalla_config["alto"])
        )

        # Establecemos el título de la ventana (nombre del juego)
        pygame.display.set_caption(pantalla_config["nombreJuego"])

        # Reloj para controlar los FPS
        self.clock = pygame.time.Clock()
        self.fps = pantalla_config["fps"]

        # Inicialización de controladores
        self.inicio_controller = PaginaPrincipalController(self)  # Menú inicial
        self.juego_controller = PingPongController(self)          # Juego principal
        self.fin_controller = FinalJuegoController(self)          # Pantalla final

        # Diccionario para almacenar los puntajes de los jugadores
        self.puntajeJugadores = {}

        # Variable que indica si se requiere reiniciar el juego
        self.reinicio = False


    def cambiar_pantalla(self, nueva_pantalla, puntajeJugador={}, reinicio=False):
        """
        Cambia el estado actual del juego (pantalla).
        
        Args:
            nueva_pantalla (str): Estado al que se quiere cambiar ("inicio", "juego", "fin").
            puntajeJugador (dict): Puntajes de los jugadores (si aplica).
            reinicio (bool): Indica si se requiere reiniciar el juego.
        """
        self.estado = nueva_pantalla
        self.puntajeJugadores = puntajeJugador
        self.reinicio = reinicio
    

    def cambiarEstadoReinicio(self):
        """
        Restablece el estado de reinicio a False.
        """
        self.reinicio = False


    def ejecutar(self):
        """
        Bucle principal del enrutador.
        Según el estado actual, ejecuta el controlador correspondiente.
        """
        while True:
            if self.estado == "inicio":
                # Ejecuta el controlador del menú principal
                self.inicio_controller.ejecutar()
            elif self.estado == "juego":
                # Ejecuta el controlador del juego
                self.juego_controller.ejecutar()
            elif self.estado == "fin":
                # Ejecuta el controlador de la pantalla final
                self.fin_controller.ejecutar()
            else:
                # Si el estado es inválido, cierra el juego
                pygame.quit()
                sys.exit()


    

