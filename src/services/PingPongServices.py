# Importamos librerías y módulos necesarios
import pygame
import sys

# Importamos el modelo (lógica del juego) y la vista (renderizado)
from src.models.PingPongModel import PingPongModel
from src.views.PingPongView import PingPongView


class PingPongServices:
    """
    Clase que contiene los servicios del juego Ping Pong.
    Se encarga de orquestar la interacción entre:
        - El modelo (lógica interna del juego).
        - La vista (dibujos/render en pantalla).
        - El enrutador (flujo entre pantallas y estados).
    """

    def __init__(self, enrutador):
        """
        Inicializa los servicios del juego.

        Args:
            enrutador (Enrutador): Instancia que gestiona estados y configuración general.
        """
        self.enrutador = enrutador

        # Almacenamos los nombres de los jugadores desde la configuración
        self.jugadores = {
            'jugador1': self.enrutador.pantalla_config["Jugador1Nombre"],
            'jugador2': self.enrutador.pantalla_config["Jugador2Nombre"],
        }

        # Velocidades configuradas desde el archivo .env
        self.velocidades = {
            'VelocidadPelota': self.enrutador.pantalla_config["VelocidadPelota"],
            'VelocidadRaquetas': self.enrutador.pantalla_config["VelocidadRaquetas"]
        }

        # Instanciamos el modelo del juego (lógica)
        self.model = PingPongModel(
            self.enrutador.pantalla_config["ancho"],
            enrutador.pantalla_config["alto"],
            self.jugadores,
            self.velocidades
        )

        # Instanciamos la vista, que dibuja en la ventana del enrutador
        self.view = PingPongView(self.enrutador.ventana)

        # Inicializamos el marcador en 0 para ambos jugadores
        self.puntos = {"punto1": 0, "punto2": 0}


    def ejecutar(self):
        """
        Bucle de ejecución de los servicios del juego.
        Maneja los eventos, actualiza el modelo, dibuja la vista y controla la lógica de puntuación.
        """
        # --- Gestión de eventos ---
        for evento in pygame.event.get():
            # Si se cierra la ventana, terminar el programa
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- Reinicio de juego ---
        if self.enrutador.reinicio == True:
            # Llamamos al modelo para reiniciar posiciones/estado
            self.model.contadorReinicio()
            # Restablecemos el flag de reinicio en el enrutador
            self.enrutador.cambiarEstadoReinicio()
        
        # --- Actualización de puntajes ---
        self.puntos = self.model.obtener_puntos()

        # Si algún jugador llega al puntaje máximo → cambiar a pantalla final
        if (self.puntos['punto1'] == self.enrutador.pantalla_config['maximoPuntaje'] or 
            self.puntos['punto2'] == self.enrutador.pantalla_config['maximoPuntaje']):
            self.enrutador.cambiar_pantalla("fin", self.puntos)

        # --- Controles del jugador ---
        teclas = pygame.key.get_pressed()          # Detectamos teclas presionadas
        self.model.mover_paletas(teclas)           # Movemos las paletas
        self.model.mover_pelota()                  # Movemos la pelota

        # --- Renderizado ---
        self.view.dibujar(self.model)              # Dibujamos el estado actual en pantalla

        # --- Control de FPS ---
        self.enrutador.clock.tick(self.enrutador.fps)
