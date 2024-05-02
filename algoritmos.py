import math
from random import randint

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
    return round (distancia,2)

def get_puntos(particulas):
    puntos=[]
    for particula in particulas:
        r = particula.red
        g = particula.green
        b = particula.blue

        x_origen = particula.origen_x
        y_origen = particula.origen_y

        x_destino = particula.destino_x
        y_destino = particula.destino_y
        puntos.append([x_origen, y_origen, r, g, b])
        puntos.append([x_destino, y_destino, r, g, b])

    return puntos

def fuerza_bruta(puntos_list):
    resultado = []
    for punto_i in puntos_list:
        x1, y1, _, _, _ = punto_i  # Solo necesitamos las coordenadas x e y de punto_i
        min_distancia = 10000
        punto_cercano = (0, 0)
        for punto_j in puntos_list:
            if punto_i != punto_j:
                x2, y2, _, _, _ = punto_j  # Solo necesitamos las coordenadas x e y de punto_j
                distancia = distancia_euclidiana(x1, y1, x2, y2)
                if distancia < min_distancia:
                    min_distancia = distancia
                    punto_cercano = (x2, y2)
        resultado.append((punto_i, punto_cercano))
    return resultado
