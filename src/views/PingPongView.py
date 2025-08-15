import pygame

class PingPongView:
    def __init__(self, ventana):
        self.ventana = ventana

    def dibujar(self, model):
        self.ventana.fill(model.NEGRO)
        self.ventana.blit(model.contadorUser1, (model.ANCHO // 2 + 50, 2))
        self.ventana.blit(model.contadorUser2, (model.ANCHO // 2 - 50, 2))
        pygame.draw.rect(self.ventana, (255, 255, 255), model.medioCampo)
        pygame.draw.rect(self.ventana, (0, 255, 0), model.paleta1)
        pygame.draw.rect(self.ventana, (0, 0, 255), model.paleta2)   
        pygame.draw.ellipse(self.ventana, model.color_pelota, model.pelota)
        pygame.display.flip()

