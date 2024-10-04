# Clase que define una actividad con su tiempo de inicio y finalización
class Actividad:
    def __init__(self, inicio, final):
        self.inicio = inicio
        self.final = final

# Función para resolver el problema de selección de actividades
def seleccion_actividades(actividades):
    # Ordenar las actividades por tiempo de finalización
    actividades.sort(key=lambda x: x.final)
    
    # Lista para almacenar las actividades seleccionadas
    actividades_seleccionadas = []
    
    # La primera actividad siempre se selecciona
    ultima_actividad = actividades[0]
    actividades_seleccionadas.append(ultima_actividad)
    
    # Recorrer las actividades restantes
    for actividad in actividades[1:]:
        # Si la actividad comienza después de que la última actividad seleccionada ha terminado
        if actividad.inicio >= ultima_actividad.final:
            actividades_seleccionadas.append(actividad)
            ultima_actividad = actividad  # Actualizar la última actividad seleccionada
    
    # Mostrar las actividades seleccionadas
    print("Actividades seleccionadas:")
    for actividad in actividades_seleccionadas:
        print(f"Actividad (Inicio: {actividad.inicio}, Fin: {actividad.final})")
    
    print(f"Total de actividades seleccionadas: {len(actividades_seleccionadas)}")

# Ejemplo de uso
actividades = [
    Actividad(1, 3),
    Actividad(2, 5),
    Actividad(4, 6),
    Actividad(5, 7),
    Actividad(6, 8),
    Actividad(3, 4)
]

seleccion_actividades(actividades)
