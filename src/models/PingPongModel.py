import pygame


class PingPongModel:
    """
    Modelo del juego Ping Pong.
    Contiene toda la lógica interna: posiciones, colisiones, puntajes y reinicio.
    """

    def __init__(self, ancho, alto, jugadores, velocidad):
        """
        Inicializa el modelo con los parámetros de pantalla, jugadores y velocidades.

        Args:
            ancho (int): Ancho de la ventana del juego.
            alto (int): Alto de la ventana del juego.
            jugadores (dict): Diccionario con nombres de los jugadores.
            velocidad (dict): Diccionario con velocidades de pelota y raquetas.
        """
        # Dimensiones del área de juego
        self.ANCHO = ancho
        self.ALTO = alto

        # Colores usados en el juego
        self.VERDE = (0, 128, 0)
        self.NEGRO = (0, 0, 0)
        self.BLANCO = (255, 255, 255)
        self.ColorJugador1 = (30, 144, 255)   # Azul
        self.ColorJugador2 = (255, 140, 0)    # Naranja

        # Fuentes para el texto (puntajes y nombres)
        self.fuente1 = pygame.font.Font(None, 50)  # Tamaño grande para puntajes
        self.fuente2 = pygame.font.Font(None, 30)  # Tamaño pequeño para nombres

        # Puntos iniciales de los jugadores
        self.puntos1 = 0
        self.puntos2 = 0

        # Renderizado inicial de texto
        self.contadorUser1 = self.fuente1.render(str(self.puntos1), True, self.BLANCO)
        self.User1 = self.fuente2.render(jugadores['jugador1'], True, self.ColorJugador1)

        self.contadorUser2 = self.fuente1.render(str(self.puntos2), True, self.BLANCO)
        self.User2 = self.fuente2.render(jugadores['jugador2'], True, self.ColorJugador2)

        # Paletas de jugadores (rectángulos)
        self.paleta1 = pygame.Rect(3, alto // 2 - 50, 15, 100)
        self.paleta2 = pygame.Rect(ancho - 18, alto // 2 - 50, 15, 100)

        # Pelota y línea central
        self.pelota = pygame.Rect(ancho // 2 - 15, alto // 2 - 15, 30, 30)
        self.medioCampo = pygame.Rect(ancho // 2, 0, 5, alto)

        # Velocidades iniciales
        self.pelota_vel_x = velocidad['VelocidadPelota']
        self.pelota_vel_y = velocidad['VelocidadPelota']
        self.velocidadRaqueta = velocidad['VelocidadRaquetas']

        # Color inicial de la pelota
        self.color_pelota = self.BLANCO


    def obtener_puntos(self):
        """
        Retorna el puntaje actual de los jugadores.
        """
        return {"punto1": self.puntos1, "punto2": self.puntos2}
    

    def mover_paletas(self, teclas):
        """
        Controla el movimiento de las paletas en función de las teclas presionadas.

        - Jugador 1: W (arriba), S (abajo).
        - Jugador 2: Flecha ↑ (arriba), Flecha ↓ (abajo).
        """
        if teclas[pygame.K_w] and self.paleta1.top > 0:
            self.paleta1.y -= self.velocidadRaqueta
        if teclas[pygame.K_s] and self.paleta1.bottom < self.ALTO:
            self.paleta1.y += self.velocidadRaqueta
        if teclas[pygame.K_UP] and self.paleta2.top > 0:
            self.paleta2.y -= self.velocidadRaqueta
        if teclas[pygame.K_DOWN] and self.paleta2.bottom < self.ALTO:
            self.paleta2.y += self.velocidadRaqueta


    def mover_pelota(self):
        """
        Actualiza la posición de la pelota y gestiona colisiones y puntajes.
        """
        # Movimiento básico
        self.pelota.x += self.pelota_vel_x
        self.pelota.y += self.pelota_vel_y

        # Rebote contra bordes superior e inferior
        if self.pelota.top <= 0 or self.pelota.bottom >= self.ALTO:
            self.pelota_vel_y *= -1

        # Rebote contra paletas → cambia dirección y color
        if self.pelota.colliderect(self.paleta1):
            self.pelota_vel_x *= -1
            self.color_pelota = self.ColorJugador1

        elif self.pelota.colliderect(self.paleta2):
            self.pelota_vel_x *= -1
            self.color_pelota = self.ColorJugador2

        # Si la pelota sale por los lados, se reinicia y aumenta el puntaje
        if self.pelota.left <= 0 or self.pelota.right >= self.ANCHO:
            self.contador()  # Actualiza puntajes
            # Reposiciona pelota en el centro
            self.pelota.center = (self.ANCHO // 2, self.ALTO // 2)
            # Cambia dirección en eje X
            self.pelota_vel_x *= -1
            # Vuelve a color blanco
            self.color_pelota = self.BLANCO


    def contador(self):
        """
        Aumenta el puntaje del jugador contrario cuando la pelota sale por un lado.
        """
        if self.pelota.left <= 0:  # Punto para Jugador 2
            self.puntos1 += 1
            self.contadorUser1 = self.fuente1.render(str(self.puntos1), True, self.BLANCO)

        elif self.pelota.right >= self.ANCHO:  # Punto para Jugador 1
            self.puntos2 += 1
            self.contadorUser2 = self.fuente1.render(str(self.puntos2), True, self.BLANCO)


    def contadorReinicio(self):
        """
        Reinicia el marcador de ambos jugadores a 0.
        """
        self.puntos2 = 0
        self.puntos1 = 0
        self.contadorUser1 = self.fuente1.render(str(self.puntos1), True, self.BLANCO)
        self.contadorUser2 = self.fuente1.render(str(self.puntos2), True, self.BLANCO)
