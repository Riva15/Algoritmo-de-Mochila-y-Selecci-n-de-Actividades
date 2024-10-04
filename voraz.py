# Clase que define un artículo con su peso y valor
class Articulo:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.valor_por_peso = valor / peso

# Función para resolver el problema de la mochila fraccionaria
def mochila_fraccionaria(pesos, valores, capacidad_maxima):
    # Crear una lista de artículos con sus pesos y valores
    articulos = [Articulo(pesos[i], valores[i]) for i in range(len(pesos))]
    
    # Ordenar los artículos por su valor por unidad de peso de manera descendente
    articulos.sort(key=lambda x: x.valor_por_peso, reverse=True)
    
    capacidad_restante = capacidad_maxima
    valor_total = 0
    seleccion_articulos = []
    
    for articulo in articulos:
        if capacidad_restante >= articulo.peso:
            # Tomar el artículo completo si cabe en la mochila
            seleccion_articulos.append((articulo.peso, 1))  # Se toma el 100% del artículo
            capacidad_restante -= articulo.peso
            valor_total += articulo.valor
        else:
            # Tomar una fracción del artículo si no cabe completo
            fraccion = capacidad_restante / articulo.peso
            seleccion_articulos.append((articulo.peso, fraccion))  # Se toma una fracción del artículo
            valor_total += articulo.valor * fraccion
            capacidad_restante = 0
            break  # La mochila está llena
    
    # Mostrar los artículos seleccionados y el valor total
    for peso, fraccion in seleccion_articulos:
        print(f"Artículo con peso {peso} - Cantidad seleccionada: {fraccion * 100:.2f}%")
    print(f"Valor total obtenido en la mochila: {valor_total:.2f}")

# Ejemplo de uso
pesos = [10, 20, 30]
valores = [60, 100, 120]
capacidad_maxima = 50

mochila_fraccionaria(pesos, valores, capacidad_maxima)