import pygame

class PingPongView:
    def __init__(self, ventana):
        self.ventana = ventana

    def dibujar(self, model):
        self.ventana.fill(model.VERDE)
        pygame.draw.rect(self.ventana, model.BLANCO, model.paleta1)
        pygame.draw.rect(self.ventana, model.BLANCO, model.paleta2)
        pygame.draw.ellipse(self.ventana, model.color_pelota, model.pelota)
        pygame.display.flip()

