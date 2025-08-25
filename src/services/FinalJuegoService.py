import pygame
import sys
from src.models.FinalJuegoModel import FinalJuegoModel
from src.views.FinalJuegoView import FinalJuegoView


class FinalJuegoServices:
    """
    Servicio que gestiona la lógica de la pantalla final del juego Pong.
    - Determina el jugador ganador según los puntajes.
    - Renderiza el mensaje y los botones de interacción (reiniciar/salir).
    - Maneja los eventos del mouse y cierre de ventana.
    """

    def __init__(self, enrutador):
        """
        Inicializa el servicio de la pantalla final.

        Args:
            enrutador (Enrutador): Objeto que controla la navegación entre pantallas
                                   y almacena configuraciones globales.
        """
        self.enrutador = enrutador
        # Modelo que contiene la lógica visual del ganador y botones
        self.model = FinalJuegoModel(
            self.enrutador.pantalla_config["ancho"],
            enrutador.pantalla_config["alto"]
        )
        # Vista que dibuja en la ventana el estado del modelo
        self.view = FinalJuegoView(self.enrutador.ventana)

    def ejecutar(self):
        """
        Ejecuta el ciclo de la pantalla final:
        - Determina quién ganó.
        - Dibuja la vista con el modelo actualizado.
        - Procesa eventos de salida y de botones.
        """
        # Determinar jugador ganador según el puntaje
        if (
            self.enrutador.puntajeJugadores['punto1'] > 0 and 
            self.enrutador.puntajeJugadores['punto1'] > self.enrutador.puntajeJugadores['punto2']
        ):
            # Jugador 1 ganó
            self.model.JugadorGanador(
                self.enrutador.pantalla_config["Jugador2Nombre"],  # Nombre jugador 2
                (255, 140, 0)  # Color asociado al jugador 2
            )
        elif (
            self.enrutador.puntajeJugadores['punto2'] > 0 and 
            self.enrutador.puntajeJugadores['punto2'] > self.enrutador.puntajeJugadores['punto1']
        ):
            # Jugador 2 ganó
            self.model.JugadorGanador(
                self.enrutador.pantalla_config["Jugador1Nombre"],  # Nombre jugador 1
                (30, 144, 255)  # Color asociado al jugador 1
            )

        # Renderizar la vista
        self.view.dibujar(self.model)

        # Controlar la tasa de refresco
        self.enrutador.clock.tick(self.enrutador.fps)

        # Manejar eventos (cerrar, reiniciar o salir)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Evento de click con el mouse
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                # Si hace click en el botón de reiniciar
                if self.model.boton_reiniciar.collidepoint(evento.pos):
                    # Cambiar a la pantalla de juego, reseteando el puntaje
                    self.enrutador.cambiar_pantalla(
                        "juego", {"punto1": 0, "punto2": 0}, True
                    )

                # Si hace click en el botón de salir
                if self.model.boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()
