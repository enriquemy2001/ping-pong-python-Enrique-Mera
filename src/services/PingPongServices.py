import pygame
import sys
from src.models.PingPongModel import PingPongModel
from src.views.PingPongView import PingPongView


class PingPongServices:
    def __init__(self, enrutador):
        self.enrutador = enrutador
        self.model = PingPongModel(self.enrutador.pantalla_config["ancho"], enrutador.pantalla_config["alto"])
        self.view = PingPongView(self.enrutador.ventana)
        
    def ejecutar(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        self.model.mover_paletas(teclas)
        self.model.mover_pelota()

        self.view.dibujar(self.model)
        self.enrutador.clock.tick(self.enrutador.fps)