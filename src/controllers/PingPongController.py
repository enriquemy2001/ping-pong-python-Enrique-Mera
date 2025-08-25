# Importamos los servicios que contienen la lógica principal del juego Ping Pong
from src.services.PingPongServices import PingPongServices


class PingPongController:
    """
    Controlador del juego Ping Pong.
    Se encarga de comunicarse con los servicios del juego
    y ejecutar la lógica principal a través del enrutador.
    """

    def __init__(self, enrutador):
        """
        Inicializa el controlador del juego Ping Pong.

        Args:
            enrutador (Enrutador): Instancia del enrutador principal,
                                   que gestiona el flujo de pantallas/estados.
        """
        # Instancia de los servicios del juego, recibiendo el enrutador
        self.Services = PingPongServices(enrutador)

    def ejecutar(self):
        """
        Método principal que inicia la ejecución del juego.
        Llama al servicio encargado de manejar la lógica del Ping Pong.
        """
        self.Services.ejecutar()

