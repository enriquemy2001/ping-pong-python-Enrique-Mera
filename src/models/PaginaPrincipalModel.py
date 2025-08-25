import pygame

class PaginaPrincipalModel:
    """
    Modelo de la pantalla principal del juego Pong.
    Se encarga de manejar los datos visuales necesarios como:
    - Dimensiones de pantalla
    - Colores base
    - Fondo de la pantalla principal
    """

    def __init__(self, ancho, alto):
        """
        Inicializa el modelo con los parámetros de la pantalla.

        Args:
            ancho (int): Ancho de la ventana principal.
            alto (int): Alto de la ventana principal.
        """
        # Dimensiones de la pantalla
        self.ANCHO = ancho
        self.ALTO = alto

        # Colores base utilizados en la interfaz
        self.VERDE = (0, 128, 0)
        self.NEGRO = (0, 0, 0)

        # Cargar y escalar el fondo principal
        self.fondo = pygame.image.load("fondo.jpg").convert()
        self.fondoPantalla = pygame.transform.scale(
            self.fondo, (self.ANCHO, self.ALTO)
        )
    