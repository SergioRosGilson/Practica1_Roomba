import concurrent.futures
import pygame
import time

RoomBa_speed = 5

#Tamaño de ventana de juego
window_x = 20
window_y = 40

#Inicializamos pygame y la ventana de juego
pygame.init()
pygame.display.set_caption('RoomBa')
game_window = pygame.display.set_mode((window_x, window_y))

#Declaramos la unidad de tiempo
fps = pygame.time.Clock()

#Declaramos la posición de la estación de carga
RoomBa_position = [10, 10]

#Establecemos el movimiento inicial de la RoomBa
direction = 'RIGHT'
change_to = direction
 
def calcular_area(largo, ancho):
    """Calcula el área de una zona multiplicando largo por ancho."""
    return largo * ancho
 
def main():
    # Definición de las zonas con sus dimensiones (largo, ancho)
    zonas = {
        'Zona 1': (500, 150),
        'Zona 2': (480, 101),
        'Zona 3': (309, 480),
        'Zona 4': (90, 220)
    }
    
    # Tasa de limpieza (por ejemplo, 1000 cm²/segundo)
    tasa_limpeza = 1000  # cm²/s
    
    # Diccionario para almacenar el área calculada de cada zona
    areas = {}
    
    # Uso de ThreadPoolExecutor para ejecutar los cálculos de forma concurrente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Asignamos cada cálculo a un hilo
        future_to_zona = {
            executor.submit(calcular_area, largo, ancho): zona
            for zona, (largo, ancho) in zonas.items()
        }
        
        # Recogemos los resultados a medida que se van completando
        for future in concurrent.futures.as_completed(future_to_zona):
            zona = future_to_zona[future]
            try:
                area = future.result()
            except Exception as exc:
                print(f"{zona} generó una excepción: {exc}")
            else:
                areas[zona] = area
                print(f"{zona}: {area} cm²")
                
    # Calcular la superficie total sumando las áreas parciales
    superficie_total = sum(areas.values())
    # Calcular el tiempo de limpieza
    tiempo_limpeza = superficie_total / tasa_limpeza
    
    print(f"\nSuperficie total a limpiar: {superficie_total} cm²")
    print(f"Tiempo estimado de limpieza: {tiempo_limpeza:.2f} segundos")

    #Empieza el bucle de juego
    while True:
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
    
        if direction == 'UP':
            RoomBa_position[1] -= 10
        if direction == 'DOWN':
            RoomBa_position[1] += 10
        if direction == 'LEFT':
            RoomBa_position[0] -= 10
        if direction == 'RIGHT':
            RoomBa_position[0] += 10

        #Refrescamos la pantalla y la unidad de tiempo
        pygame.display.update()
        fps.tick(RoomBa_speed)

if __name__ == '__main__':
    main()