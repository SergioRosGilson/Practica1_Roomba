import pygame
import time
import GameOver

class Juego:
    
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

    #Inicializamos pygame y la ventana de juego
    pygame.init()
    pygame.display.set_caption('RoomBa')
    game_window = pygame.display.set_mode((window_x, window_y))

    #Declaramos la unidad de tiempo
    fps = pygame.time.Clock()

    #Declaramos la posición de la estación de carga
    RoomBa_position = [10, 10]

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
            RoomBa_position[1] -= 10
        if direction == 'DOWN':
            RoomBa_position[1] += 10
        if direction == 'LEFT':
            RoomBa_position[0] -= 10
        if direction == 'RIGHT':
            RoomBa_position[0] += 10

        #Condiciones de Game Over
        
        ClaseGameOver = GameOver()
        
        if RoomBa_position[0] < 0 or RoomBa_position[0] > window_x-10:
            ClaseGameOver()
        if RoomBa_position[1] < 0 or RoomBa_position[1] > window_y-10:
            ClaseGameOver()

        #Dibujamos la RoomBa
        for pos in RoomBa_position:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        #Dibujamos las zonas a limpiar
        pygame.draw.rect(game_window, white, pygame.Rect(zonas[0], zonas[1], 10, 10))

        #Refrescamos la pantalla y la unidad de tiempo
        pygame.display.update()
        fps.tick(RoomBa_speed)