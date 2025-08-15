import pygame

class PaginaPrincipalView:
    def __init__(self, ventana):
        self.ventana = ventana

    def dibujar(self, model):
        self.ventana.blit(model.fondoPantalla,(0,0))
        """self.ventana.blit(model.NombreJuego, (model.ANCHO / 2 - 130, 40))
        self.ventana.blit(model.avisoInicio, (model.ANCHO / 2 - 250, model.ALTO - 100))"""
        pygame.display.flip()
