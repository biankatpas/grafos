
class Aresta:
    def __init__(self, origem, destino, peso=1):
        self.origem = origem
        self.destino = destino
        self.peso = peso
        self.color = 'black'
