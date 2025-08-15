from src.services.PaginaPrincipalService import PaginaPrincipalServices

class PaginaPrincipalController:
    def __init__(self, pantalla_config):
        self.Services = PaginaPrincipalServices(pantalla_config)

    def ejecutar(self):
        self.Services.ejecutar()