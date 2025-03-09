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

    def crear_ventana(Window_X, Window_Y):
        pygame.display.set_mode((Window_X, Window_Y))
    
    #Inicializamos pygame y la ventana de juego
    def iniciar_juego():
        pygame.init()
        pygame.display.set_caption('RoomBa')
        Juego.crear_ventana(print(Juego.window_x), print(Juego.window_y))

    iniciar_juego()

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

    #Empieza el bucle de juego
    while True:
        
        def movimiento_RoomBa(R_position):
        
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

        movimiento_RoomBa(print(RoomBa_position))

        #Condiciones de Game Over
        
        ClaseGameOver = GameOver()
        
        if RoomBa_position[0] < 0 or RoomBa_position[0] > window_x-10:
            ClaseGameOver()
        if RoomBa_position[1] < 0 or RoomBa_position[1] > window_y-10:
            ClaseGameOver()

        def dibujar_objetos(R_position):
    
            #Dibujamos la RoomBa
            for pos in R_position:
                pygame.draw.rect((Juego.crear_ventana(print(Juego.window_x), print(Juego.window_y))), print(Juego.green), pygame.Rect(pos[0], pos[1], 10, 10))
            
            #Dibujamos las zonas a limpiar
            pygame.draw.rect((Juego.crear_ventana(print(Juego.window_x), print(Juego.window_y))), print(Juego.white), pygame.Rect(print(Juego.zonas[0]), print(Juego.zonas[1]), 10, 10))

        dibujar_objetos(print(RoomBa_position))
       
        def update_juego():
        
            #Refrescamos la pantalla y la unidad de tiempo
            pygame.display.update()
            print(Juego.fps.tick(print(Juego.RoomBa_speed)))

        update_juego()