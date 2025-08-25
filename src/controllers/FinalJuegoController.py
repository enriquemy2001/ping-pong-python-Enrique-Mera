# Importamos los servicios que contienen la lógica de la pantalla final
from src.services.FinalJuegoService import FinalJuegoServices


class FinalJuegoController:
    """
    Controlador de la Pantalla Final del juego.
    Se encarga de inicializar los servicios correspondientes
    y de ejecutar su lógica cuando el enrutador cambia al estado "fin".
    """

    def __init__(self, pantalla_config):
        """
        Inicializa el controlador de la pantalla final.

        Args:
            pantalla_config (dict): Configuración de la pantalla (ancho, alto, fps, etc.).
        """
        # Creamos una instancia de los servicios de la pantalla final
        self.Services = FinalJuegoServices(pantalla_config)

    def ejecutar(self):
        """
        Ejecuta la lógica de la pantalla final llamando a los servicios correspondientes.
        """
        self.Services.ejecutar()