# Importamos los servicios que contienen la lógica de la página principal
from src.services.PaginaPrincipalService import PaginaPrincipalServices


class PaginaPrincipalController:
    """
    Controlador de la Página Principal.
    Se encarga de inicializar los servicios relacionados con la pantalla de inicio
    y de ejecutar su lógica cuando es llamado por el enrutador.
    """

    def __init__(self, pantalla_config):
        """
        Inicializa el controlador de la página principal.

        Args:
            pantalla_config (dict): Configuración de la pantalla (ancho, alto, fps, etc.).
        """
        # Creamos una instancia de los servicios de la página principal
        self.Services = PaginaPrincipalServices(pantalla_config)

    def ejecutar(self):
        """
        Ejecuta la lógica de la página principal llamando a los servicios correspondientes.
        """
        self.Services.ejecutar()
