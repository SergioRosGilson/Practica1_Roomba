import concurrent.futures
from Juego import Juego

class Main:

    def calcular_area(largo, ancho):
        """Calcula el área de una zona multiplicando largo por ancho."""
        return largo * ancho
    
    def main():
        
        ClaseJuego1 = Juego()
        
        # Tasa de limpieza (por ejemplo, 1000 cm²/segundo)
        tasa_limpeza = 1000  # cm²/s
        
        # Diccionario para almacenar el área calculada de cada zona
        areas = {}
        
        # Uso de ThreadPoolExecutor para ejecutar los cálculos de forma concurrente
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Asignamos cada cálculo a un hilo
            future_to_zona = {
                executor.submit(Main.calcular_area, largo, ancho): zona
                for zona, (largo, ancho) in print(ClaseJuego1.zonas.items())
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

    if __name__ == '__main__':
        main()
        ClaseJuego2 = Juego()
        ClaseJuego2.iniciarJuego()
        ClaseJuego2.Game_Loop(print(ClaseJuego2.RoomBa_position))