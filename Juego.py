import pygame
import time
from GameOver import GameOver
import Juego
from Zonas import Zonas

class Juego:
    
    def __init__(self):
        
        self.RoomBa_speed = 5
        self.score = 0
        self.zona_spawn = True

        #Tamaño de ventana de juego
        self.window_x = 720
        self.window_y = 480

        #Definimos colores
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)

        #Declaramos la unidad de tiempo
        self.fps = pygame.time.Clock()

        #Declaramos la posición de la estación de carga
        self.RoomBa_position = [10, 10]

    def crear_ventana(Window_X, Window_Y):
        pygame.display.set_mode((Window_X, Window_Y))
    
    #Inicializamos pygame y la ventana de juego
    def iniciar_juego():
        ClaseJuego = Juego()
        pygame.init()
        pygame.display.set_caption('RoomBa')
        ClaseJuego.crear_ventana(print(ClaseJuego.window_x), print(ClaseJuego.window_y))

    def show_score():
        ClaseJuego = Juego()
        #Creamos la fuente
        score_font = pygame.font.SysFont("times new roman", 14)
        #Renderizamos el texto
        score_surface = score_font.render("Score : " + str(print(ClaseJuego.score)), True, print(ClaseJuego.blue))
        #Creamos el espacio del texto
        score_rect = score_surface.get_rect()
        #Mostramos el texto
        pygame.display.set_mode((print(ClaseJuego.window_x), print(ClaseJuego.window_y))).blit(score_surface, score_rect)

    def play_music():
        #Iniciamos el reproductor
        pygame.mixer.init()
        #Cargamos el archivo
        pygame.mixer.music.load("Background.mp3")
        #Reproducimos el archivo en bucle
        pygame.mixer.music.play(-1)
        
    def Game_Loop(R_position):
        
        #Empieza el bucle de juego
        while True:
            
            ClaseZonas = Zonas()
            ClaseJuego = Juego()

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

            #Condiciones del score
            if R_position[0] == print(ClaseZonas.Zona_1[0]) and R_position[1] == print(ClaseZonas.Zona_1[1]):
                ClaseJuego.score += 10
                ClaseJuego.zona_spawn = False

            #Condiciones de Game Over    
            ClaseGameOver = GameOver()
                
            if R_position[0] < 0 or R_position[0] > print(ClaseJuego.window_x-10):
                ClaseGameOver.game_over()
                pygame.mixer.music.pause
            if R_position[1] < 0 or R_position[1] > print(ClaseJuego.window_y-10):
                ClaseGameOver.game_over()
                pygame.mixer.music.pause
            
            #Dibujamos la RoomBa
            for pos in R_position:
                pygame.draw.rect((ClaseJuego.crear_ventana(print(ClaseJuego.window_x), print(ClaseJuego.window_y))), print(ClaseJuego.green), pygame.Rect(pos[0], pos[1], 10, 10))
                    
            #Dibujamos las zonas a limpiar
            pygame.draw.rect((ClaseJuego.crear_ventana(print(ClaseJuego.window_x), print(ClaseJuego.window_y))), print(ClaseJuego.white), pygame.Rect(print(ClaseZonas.Zona_1[0]), print(ClaseZonas.Zona_1[1]), 10, 10))
            
            #Mostramos el score
            ClaseJuego.show_score()

            #Refrescamos la pantalla y la unidad de tiempo
            pygame.display.update()
            print(ClaseJuego.fps.tick(print(ClaseJuego.RoomBa_speed)))