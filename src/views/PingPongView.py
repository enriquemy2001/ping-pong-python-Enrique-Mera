import pygame


class PingPongView:
    """
    Vista del juego Ping Pong.
    Se encarga de dibujar en la ventana todos los elementos gráficos del modelo:
    jugadores, puntajes, paletas, pelota y línea central.
    """

    def __init__(self, ventana):
        """
        Inicializa la vista con la ventana donde se renderizará el juego.

        Args:
            ventana (pygame.Surface): Superficie de la ventana creada en el enrutador.
        """
        self.ventana = ventana

    def dibujar(self, model):
        """
        Dibuja todos los elementos del juego en la ventana.

        Args:
            model (PingPongModel): Instancia del modelo que contiene
                                   el estado actual del juego.
        """
        # Fondo de la ventana
        self.ventana.fill(model.NEGRO)

        # Nombres de los jugadores
        self.ventana.blit(model.User1, (40, 2))
        self.ventana.blit(model.User2, (model.ANCHO - 200, 2))

        # Contadores de puntaje
        self.ventana.blit(model.contadorUser1, (model.ANCHO // 2 + 50, 2))
        self.ventana.blit(model.contadorUser2, (model.ANCHO // 2 - 50, 2))

        # Línea central
        pygame.draw.rect(self.ventana, (255, 255, 255), model.medioCampo)

        # Paletas de los jugadores
        pygame.draw.rect(self.ventana, (30, 144, 255), model.paleta1)   # Jugador 1
        pygame.draw.rect(self.ventana, (255, 140, 0), model.paleta2)    # Jugador 2

        # Pelota (cambia de color al golpear paletas)
        pygame.draw.ellipse(self.ventana, model.color_pelota, model.pelota)

        # Actualiza la pantalla con todos los elementos dibujados
        pygame.display.flip()


