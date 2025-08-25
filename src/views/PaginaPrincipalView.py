import pygame

class PaginaPrincipalView:
    """
    Vista de la pantalla principal del juego.
    Se encarga de mostrar los elementos visuales de la página principal.
    """

    def __init__(self, ventana):
        """
        Inicializa la vista con la ventana del juego.
        
        Args:
            ventana (pygame.Surface): Superficie principal donde se dibujará todo.
        """
        self.ventana = ventana

    def dibujar(self, model):
        """
        Dibuja los elementos de la pantalla principal en la ventana.
        
        Args:
            model (PaginaPrincipalModel): Modelo que contiene los recursos visuales.
        """
        # Dibuja el fondo escalado de la pantalla principal
        self.ventana.blit(model.fondoPantalla, (0, 0))
        
        # Actualiza la pantalla para mostrar los cambios
        pygame.display.flip()

