from algoritmos import distancia_euclidiana, get_puntos

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_vertices_de_particulas(self, particulas):
        for particula in particulas:
            self.agregar_vertice((particula.origen_x, particula.origen_y))
            self.agregar_vertice((particula.destino_x, particula.destino_y))


    def agregar_aristas_entre_particulas(self, particulas):
        puntos = get_puntos(particulas)
        for i in range(len(puntos)):
            for j in range(i + 1, len(puntos)):
                punto_origen = (puntos[i][0], puntos[i][1])
                punto_destino = (puntos[j][0], puntos[j][1])
                peso = distancia_euclidiana(punto_origen[0], punto_origen[1], punto_destino[0], punto_destino[1])
                if punto_origen in self.vertices and punto_destino in self.vertices:
                    self.vertices[punto_origen].append((punto_destino, peso))
                    self.vertices[punto_destino].append((punto_origen, peso))






    def obtener_vertices(self):
        return list(self.vertices.keys())

    def obtener_aristas(self, vertice):
        return self.vertices[vertice]

    def __str__(self):
        return str(self.vertices)
