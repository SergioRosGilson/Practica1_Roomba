import pygame
import time
from GameOver import GameOver
import Juego

class Juego:
    
    def __init__(self):
        # Definición de las zonas con sus dimensiones (largo, ancho)
        self.zonas = {
            'Zona 1': (500, 150),
            'Zona 2': (480, 101),
            'Zona 3': (309, 480),
            'Zona 4': (90, 220)
        }
    
    RoomBa_speed = 5

    #Tamaño de ventana de juego
    window_x = 720
    window_y = 480

    #Definimos colores
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    def crear_ventana(Window_X, Window_Y):
        pygame.display.set_mode((Window_X, Window_Y))
    
    #Inicializamos pygame y la ventana de juego
    def iniciar_juego():
        ClaseJuego = Juego()
        pygame.init()
        pygame.display.set_caption('RoomBa')
        ClaseJuego.crear_ventana(print(Juego.window_x), print(Juego.window_y))

    #Declaramos la unidad de tiempo
    fps = pygame.time.Clock()

    #Declaramos la posición de la estación de carga
    RoomBa_position = [10, 10]

    # Definición de las zonas con sus dimensiones (largo, ancho)
    zonas = {
        'Zona 1': (500, 150),
        'Zona 2': (480, 101),
        'Zona 3': (309, 480),
        'Zona 4': (90, 220)
    }

        
    def Game_Loop(R_position):
        
        #Empieza el bucle de juego
        while True:
            
            #Establecemos el movimiento inicial de la RoomBa
            direction = 'RIGHT'
            change_to = direction
                
            #Asociamos el movimiento a las teclas
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'

            #Optimizar el movimiento
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'

            #Movemos la RoomBa
            if direction == 'UP':
                R_position[1] -= 10
            if direction == 'DOWN':
                R_position[1] += 10
            if direction == 'LEFT':
                R_position[0] -= 10
            if direction == 'RIGHT':
                R_position[0] += 10

            #Condiciones de Game Over
                
            ClaseGameOver = GameOver()
                
            if R_position[0] < 0 or R_position[0] > print(Juego.window_x-10):
                ClaseGameOver.game_over()
            if R_position[1] < 0 or R_position[1] > print(Juego.window_y-10):
                ClaseGameOver.game_over()
            
            #Dibujamos la RoomBa
            for pos in R_position:
                pygame.draw.rect((Juego.crear_ventana(print(Juego.window_x), print(Juego.window_y))), print(Juego.green), pygame.Rect(pos[0], pos[1], 10, 10))
                    
            #Dibujamos las zonas a limpiar
            pygame.draw.rect((Juego.crear_ventana(print(Juego.window_x), print(Juego.window_y))), print(Juego.white), pygame.Rect(print(Juego.zonas[0]), print(Juego.zonas[1]), 10, 10))
            
                
            #Refrescamos la pantalla y la unidad de tiempo
            pygame.display.update()
            print(Juego.fps.tick(print(Juego.RoomBa_speed)))