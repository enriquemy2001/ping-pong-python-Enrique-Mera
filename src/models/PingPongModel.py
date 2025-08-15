import pygame

class PingPongModel:
    def __init__(self, ancho, alto):
        self.ANCHO = ancho
        self.ALTO = alto

        self.VERDE = (0, 128, 0)
        self.NEGRO = (0, 0, 0)

        self.fuente1 = pygame.font.Font(None, 50) 
        self.fuente2 = pygame.font.Font(None, 50) 

        self.puntos1=0
        self.puntos2=0
        self.contadorUser1 = self.fuente1.render(str(self.puntos1), True, (255, 255, 255))
        self.contadorUser2 = self.fuente1.render(str(self.puntos2), True, (255, 255, 255))
        

        self.paleta1 = pygame.Rect(3, alto // 2 - 50, 15, 100)
        self.paleta2 = pygame.Rect(ancho - 18, alto // 2 - 50, 15, 100)
        self.pelota = pygame.Rect(ancho // 2 - 15, alto // 2 - 15, 30, 30)
        self.medioCampo = pygame.Rect(ancho // 2, 0, 5, alto)

        self.pelota_vel_x = 6
        self.pelota_vel_y = 6

        self.color_pelota = (255, 255, 255)

    def mover_paletas(self, teclas):
        if teclas[pygame.K_w] and self.paleta1.top > 0:
            self.paleta1.y -= 7
        if teclas[pygame.K_s] and self.paleta1.bottom < self.ALTO:
            self.paleta1.y += 7
        if teclas[pygame.K_UP] and self.paleta2.top > 0:
            self.paleta2.y -= 7
        if teclas[pygame.K_DOWN] and self.paleta2.bottom < self.ALTO:
            self.paleta2.y += 7

    def mover_pelota(self):
        self.pelota.x += self.pelota_vel_x
        self.pelota.y += self.pelota_vel_y

        # Rebote arriba/abajo
        if self.pelota.top <= 0 or self.pelota.bottom >= self.ALTO:
            self.pelota_vel_y *= -1

        # Rebote con paletas y cambio de color
        if self.pelota.colliderect(self.paleta1):
            self.pelota_vel_x *= -1
            self.color_pelota = (0, 255, 0)  

        elif self.pelota.colliderect(self.paleta2):
            self.pelota_vel_x *= -1
            self.color_pelota = (0, 0, 255)  

        # Reinicio si sale de los lados
        if self.pelota.left <= 0 or self.pelota.right >= self.ANCHO:
            self.contador()
            self.pelota.center = (self.ANCHO // 2, self.ALTO // 2)
            self.pelota_vel_x *= -1
            self.color_pelota = (255, 255, 255)  
    
    def contador(self):
        if self.pelota.left <= 0:
            self.puntos1 = self.puntos1 + 1
            self.contadorUser1 = self.fuente1.render(str(self.puntos1), True, (255, 255, 255))
            
        elif self.pelota.right >= self.ANCHO:
            self.puntos2 = self.puntos2 + 1
            self.contadorUser2 = self.fuente1.render(str(self.puntos2), True, (255, 255, 255))
