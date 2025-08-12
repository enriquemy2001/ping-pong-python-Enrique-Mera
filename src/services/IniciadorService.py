import pygame
from src.controllers.PingPongController import PingPongController

def Iniciador(pantalla_config):
    pygame.init()
    controlador = PingPongController(pantalla_config)
    controlador.ejecutar()

