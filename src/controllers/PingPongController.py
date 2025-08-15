from src.services.PingPongServices import PingPongServices

class PingPongController:
    def __init__(self, enrutador):
        self.Services = PingPongServices(enrutador)

    def ejecutar(self):
        self.Services.ejecutar()
