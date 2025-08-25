import pygame

class FinalJuegoView:
    """
    Vista de la pantalla final del juego.
    Se encarga de mostrar los botones y el nombre del jugador ganador.
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
        Dibuja la pantalla final, incluyendo los botones y el nombre del ganador.
        
        Args:
            model (FinalJuegoModel): Modelo que contiene la información y recursos visuales.
        """
        # Fondo de la pantalla final
        self.ventana.fill((10, 10, 30))
        
        # Dibujar botones de reinicio y salir
        pygame.draw.rect(self.ventana, model.color_reiniciar, model.boton_reiniciar)
        pygame.draw.rect(self.ventana, model.color_salir, model.boton_salir)

        # Dibujar texto centrado en cada botón
        self.ventana.blit(
            model.texto_reiniciar,
            (model.boton_reiniciar.centerx - model.texto_reiniciar.get_width() // 2,
             model.boton_reiniciar.centery - model.texto_reiniciar.get_height() // 2)
        )
        self.ventana.blit(
            model.texto_salir,
            (model.boton_salir.centerx - model.texto_salir.get_width() // 2,
             model.boton_salir.centery - model.texto_salir.get_height() // 2)
        )

        # Mostrar título "¡GANADOR!" y nombre del jugador ganador
        self.ventana.blit(model.Ganador, (model.ANCHO // 2 - 250, model.ALTO / 2 - 180))
        self.ventana.blit(model.NombreJugadorGanador, (model.ANCHO // 2 - 110, model.ALTO / 2 - 50))

        # Actualizar pantalla
        pygame.display.flip()
