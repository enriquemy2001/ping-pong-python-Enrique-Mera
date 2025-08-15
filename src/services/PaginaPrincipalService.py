import pygame
import sys
from src.models.PaginaPrincipalModel import PaginaPrincipalModel
from src.views.PaginaPrincipalView import PaginaPrincipalView

class PaginaPrincipalServices:
    def __init__(self, enrutador):
        self.enrutador = enrutador
        self.model = PaginaPrincipalModel(self.enrutador.pantalla_config["ancho"], enrutador.pantalla_config["alto"])
        self.view = PaginaPrincipalView(self.enrutador.ventana)

    def ejecutar(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_SPACE]:
            self.enrutador.cambiar_pantalla("juego")
        
        self.view.dibujar(self.model)
        self.enrutador.clock.tick(self.enrutador.fps)