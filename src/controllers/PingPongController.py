import pygame
import sys
from src.models.PingPongModel import PingPongModel
from src.views.PingPongView import PingPongView

class PingPongController:
    def __init__(self, pantalla_config):
        self.model = PingPongModel(pantalla_config["ancho"], pantalla_config["alto"])
        self.ventana = pygame.display.set_mode((pantalla_config["ancho"], pantalla_config["alto"]))
        pygame.display.set_caption(pantalla_config["nombreJuego"])
        self.view = PingPongView(self.ventana)
        self.clock = pygame.time.Clock()
        self.fps = pantalla_config["fps"]

    def ejecutar(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            teclas = pygame.key.get_pressed()
            self.model.mover_paletas(teclas)
            self.model.mover_pelota()

            self.view.dibujar(self.model)
            self.clock.tick(self.fps)
