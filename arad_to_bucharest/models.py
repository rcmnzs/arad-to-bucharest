from dataclasses import dataclass

# Adjacente
@dataclass
class Adjacente:
    vertice: Vertice
    custo: int

# Vertice 
class Vertice:
    def __init__(self, rotulo, dist_obj):    
        self.rotulo = rotulo
        self.dist_obj = dist_obj
        self.visitado = False
        self.adjacentes = []
        
    def adicionar_adj(self, adjacente):
        self.adjacentes.append(adjacente)
    
    def exibir_adjacentes(self):
        for adjacente in self.adjacentes:
            print(f"Nome: {adjacente.vertice.rotulo} | Heurística: {adjacente.vertice.dist_obj} | Custo: {adjacente.custo}")