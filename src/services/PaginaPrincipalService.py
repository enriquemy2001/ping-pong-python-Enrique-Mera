import pygame
import sys
from src.models.PaginaPrincipalModel import PaginaPrincipalModel
from src.views.PaginaPrincipalView import PaginaPrincipalView


class PaginaPrincipalServices:
    """
    Servicio que gestiona la lógica de la pantalla principal del juego Pong.
    Se encarga de manejar los eventos, detectar la acción del usuario
    para iniciar el juego y renderizar los elementos gráficos en pantalla.
    """

    def __init__(self, enrutador):
        """
        Inicializa el servicio de la pantalla principal.

        Args:
            enrutador (Enrutador): Objeto encargado de manejar la navegación entre pantallas.
        """
        self.enrutador = enrutador
        # Modelo que define los elementos gráficos y la configuración inicial de la pantalla principal
        self.model = PaginaPrincipalModel(
            self.enrutador.pantalla_config["ancho"],
            enrutador.pantalla_config["alto"]
        )
        # Vista que se encarga de dibujar el contenido del modelo en la ventana
        self.view = PaginaPrincipalView(self.enrutador.ventana)

    def ejecutar(self):
        """
        Ejecuta el bucle principal de la pantalla de inicio.
        - Captura eventos como cerrar la ventana.
        - Detecta si el jugador presiona la tecla ESPACIO para comenzar el juego.
        - Renderiza la vista en pantalla.
        """
        # Revisión de eventos (cerrar ventana, etc.)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Captura el estado actual de las teclas presionadas
        teclas = pygame.key.get_pressed()

        # Si el jugador presiona la barra espaciadora, cambia a la pantalla de juego
        if teclas[pygame.K_SPACE]:
            self.enrutador.cambiar_pantalla("juego")
        
        # Renderiza el modelo usando la vista
        self.view.dibujar(self.model)

        # Controla la velocidad de actualización según los FPS configurados
        self.enrutador.clock.tick(self.enrutador.fps)
