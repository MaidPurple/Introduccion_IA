import numpy as np
import networkx as nx
import random

# Matriz de distancias (basada en la imagen proporcionada)
distancias = np.array([
    [0, 32.4, 121, 24.5, 144, 167, 66.3, 18],  # U
    [32.4, 0, 31, 149, 117, 140, 78, 37.7],    # Cajicá
    [121, 31, 0, 114, 262, 282, 180, 136],     # Villavicencio
    [24.5, 149, 114, 0, 165, 188, 83.1, 39.4], # Soacha
    [144, 117, 262, 165, 0, 28.3, 197, 138],   # Tunja
    [167, 140, 282, 188, 28.3, 0, 219, 159],   # Toca
    [66.3, 78, 180, 83.1, 197, 219, 0, 84.6],  # La Vega
    [18, 37.7, 136, 39.4, 138, 159, 84.6, 0]   # La Calera
])

# Parámetros de la Colonia de Hormigas
num_hormigas = 10
num_iteraciones = 100
evaporacion = 0.5  # Factor de evaporación de feromonas
alpha = 1.0  # Peso de la feromona
beta = 2.0  # Peso de la heurística (distancia)

# Inicialización de feromonas
num_ciudades = len(distancias)
feromonas = np.ones((num_ciudades, num_ciudades))

# Función de probabilidad de elección
def probabilidad_elegir(ciudad_actual, ciudades_disponibles, feromonas, distancias, alpha, beta):
    num = []
    denom = 0
    for ciudad in ciudades_disponibles:
        num.append((feromonas[ciudad_actual][ciudad] ** alpha) * ((1.0 / distancias[ciudad_actual][ciudad]) ** beta))
        denom += num[-1]
    probabilidades = [n / denom for n in num]
    return ciudades_disponibles[np.random.choice(len(ciudades_disponibles), p=probabilidades)]

# Algoritmo de colonia de hormigas
mejor_ruta = None
mejor_distancia = float('inf')

for _ in range(num_iteraciones):
    rutas = []
    distancias_rutas = []

    for _ in range(num_hormigas):
        ciudad_actual = 0  # Empezamos en la U
        ruta = [ciudad_actual]
        ciudades_disponibles = list(range(num_ciudades))
        ciudades_disponibles.remove(ciudad_actual)
        distancia_total = 0

        while ciudades_disponibles:
            siguiente_ciudad = probabilidad_elegir(ciudad_actual, ciudades_disponibles, feromonas, distancias, alpha, beta)
            ruta.append(siguiente_ciudad)
            distancia_total += distancias[ciudad_actual][siguiente_ciudad]
            ciudades_disponibles.remove(siguiente_ciudad)
            ciudad_actual = siguiente_ciudad
        
        # Volver a la U
        distancia_total += distancias[ciudad_actual][0]
        ruta.append(0)

        rutas.append(ruta)
        distancias_rutas.append(distancia_total)

        # Actualizar mejor solución
        if distancia_total < mejor_distancia:
            mejor_distancia = distancia_total
            mejor_ruta = ruta

    # Evaporación de feromonas
    feromonas *= (1 - evaporacion)

    # Depósito de feromonas (solo la mejor ruta)
    for i in range(len(mejor_ruta) - 1):
        feromonas[mejor_ruta[i]][mejor_ruta[i+1]] += 1.0 / mejor_distancia

# Convertir ruta óptima en nombres de ciudades
ciudades = ["U", "Cajicá", "Villavicencio", "Soacha", "Tunja", "Toca", "La Vega", "La Calera"]
ruta_final = [ciudades[i] for i in mejor_ruta]

# Mostrar resultados
print("🏆 Mejor Ruta:", " → ".join(ruta_final))
print("📏 Distancia Total:", mejor_distancia, "km")
