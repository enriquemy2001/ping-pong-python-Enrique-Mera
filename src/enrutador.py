"""import pygame
from src.controllers.PingPongController import PingPongController
from src.controllers.PingPongController import PaginaPrincipalController


def Iniciador(pantalla_config):
    pygame.init()
    controlador = PaginaPrincipalController(pantalla_config)
    controlador.ejecutar()"""

import pygame
import sys
from src.controllers.PaginaPrincipalController import PaginaPrincipalController
from src.controllers.PingPongController import PingPongController
#from src.controllers.PantallaFinController import PantallaFinController

class Enrutador:
    def __init__(self, pantalla_config):
        pygame.init()
        self.pantalla_config = pantalla_config
        self.estado = "inicio"
        self.ventana = pygame.display.set_mode((pantalla_config["ancho"], pantalla_config["alto"]))
        pygame.display.set_caption(pantalla_config["nombreJuego"])
        self.clock = pygame.time.Clock()
        self.fps = pantalla_config["fps"]
        self.inicio_controller = PaginaPrincipalController(self)
        self.juego_controller = PingPongController(self)
        #self.fin_controller = PantallaFinController(self)

    def cambiar_pantalla(self, nueva_pantalla):
        self.estado = nueva_pantalla

    def ejecutar(self):
        while True:
            if self.estado == "inicio":
                self.inicio_controller.ejecutar()
            elif self.estado == "juego":
                self.juego_controller.ejecutar()
            elif self.estado == "fin":
                self.fin_controller.ejecutar()
            else:
                pygame.quit()
                sys.exit()

    

