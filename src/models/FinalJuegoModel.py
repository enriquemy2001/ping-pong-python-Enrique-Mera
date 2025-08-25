import pygame

class FinalJuegoModel:
    """
    Modelo de la pantalla final del juego Pong.
    Se encarga de manejar:
    - Colores y fuentes
    - Botones (reiniciar y salir)
    - Textos de ganador
    - Estados visuales según la interacción del mouse
    """

    def __init__(self, ancho, alto):
        """
        Inicializa el modelo con las dimensiones de pantalla, estilos,
        textos y botones necesarios.

        Args:
            ancho (int): Ancho de la ventana del juego.
            alto (int): Alto de la ventana del juego.
        """
        # Dimensiones de pantalla
        self.ANCHO = ancho
        self.ALTO = alto

        # Colores
        self.BLANCO = (255, 255, 255)
        self.NEGRO = (0, 0, 0)
        self.VERDE = (0, 200, 0)
        self.VERDE_HOVER = (50, 255, 50)   # Hover sobre el botón Reiniciar
        self.ROJO = (200, 0, 0)
        self.ROJO_HOVER = (255, 50, 50)    # Hover sobre el botón Salir

        # Fuentes de texto
        self.fuente1 = pygame.font.Font(None, 140)  # Texto principal
        self.fuente2 = pygame.font.Font(None, 20)   # Texto botones
        self.fuente3 = pygame.font.Font(None, 50)   # Texto ganador

        # Botones
        self.boton_reiniciar = pygame.Rect(300, alto // 2 + 100, 300, 60)
        self.boton_salir = pygame.Rect(ancho // 2 + 50, alto // 2 + 100, 300, 60)

        # Datos del ganador
        self.ColorJugarGanador = (0, 0, 0)
        self.jugadorGanador = ""
        self.Ganador = self.fuente1.render("¡GANADOR!", True, (64, 224, 208))
        self.NombreJugadorGanador = self.fuente3.render(self.jugadorGanador, True, (255, 255, 255))

        # Posición del mouse
        self.mouse_evento = pygame.mouse.get_pos()

        # --- Configuración inicial de botones según posición del mouse ---
        # Reiniciar
        if self.boton_reiniciar.collidepoint(self.mouse_evento):
            self.color_reiniciar = self.VERDE_HOVER
        else:
            self.color_reiniciar = self.VERDE
        self.texto_reiniciar = self.fuente2.render("Comenzar de nuevo", True, self.NEGRO)

        # Salir
        if self.boton_salir.collidepoint(self.mouse_evento):
            self.color_salir = self.ROJO_HOVER
        else:
            self.color_salir = self.ROJO
        self.texto_salir = self.fuente2.render("Salir", True, self.NEGRO)

    def eventoMouseClick(self, puntosJugadores):
        """
        Almacena los puntos de los jugadores al hacer clic.
        Args:
            puntosJugadores (dict): Diccionario con el puntaje de cada jugador.
        """
        self.PuntosJugadores = puntosJugadores
    
    def JugadorGanador(self, Jugador, colorJugadorTexto=(0, 0, 0)):
        """
        Define al jugador ganador y renderiza su nombre en pantalla.

        Args:
            Jugador (str): Nombre del jugador ganador.
            colorJugadorTexto (tuple): Color del texto del nombre del ganador.
        """
        self.jugadorGanador = Jugador
        self.NombreJugadorGanador = self.fuente3.render(
            self.jugadorGanador, True, colorJugadorTexto
        )
