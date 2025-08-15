import pygame

class PaginaPrincipalModel:
    def __init__(self, ancho, alto):
        self.ANCHO = ancho
        self.ALTO = alto

        self.VERDE = (0, 128, 0)
        self.NEGRO = (0, 0, 0)

        """self.fuente1 = pygame.font.Font(None, 50) 
        self.fuente2 = pygame.font.Font(None, 40) """

        self.fondo = pygame.image.load("fondo.jpg").convert()
        self.fondoPantalla = pygame.transform.scale(self.fondo, (self.ANCHO, self.ALTO))
        """self.NombreJuego = self.fuente1.render("PING PONG UIDE", True, (255, 255, 255))
        self.avisoInicio = self.fuente2.render("Presione ESPACIO para empezar el juego", True, (255, 255, 255))"""
