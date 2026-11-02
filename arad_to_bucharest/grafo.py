from models import *

class Grafo:
    def __init__(self):
        self.vertices = {}      
        self._vertices_dict = {
            'Arad': 366, 
            'Bucharest': 0, 
            'Craiova': 160, 
            'Dobreta': 242, 
            'Eforie': 161, 
            'Fagaras': 178, 
            'Giurgiu': 77, 
            'Hirsova': 151, 
            'Iasi': 226, 
            'Lugoj': 244,
            'Mehadia': 241, 
            'Neamt': 234, 
            'Oradea':  380, 
            'Pitesti': 98, 
            'Rimnicu Vilcea': 193, 
            'Sibiu': 253, 
            'Timisoara': 329, 
            'Urziceni': 80, 
            'Vaslui': 199, 
            'Zerind': 374
        }
        
        arestas = [
                ("Arad", "Zerind", 75),
                ("Zerind", "Oradea", 71),
                ("Oradea", "Sibiu", 151),
                ("Arad", "Sibiu", 140),
                ("Arad", "Timisoara", 118),
                ("Timisoara", "Lugoj", 111),
                ("Lugoj", "Mehadia", 70),
                ("Mehadia", "Dobreta", 75),
                ("Dobreta", "Craiova", 120),
                ("Craiova", "Pitesti", 138),
                ("Craiova", "Rimnicu Vilcea", 146),
                ("Rimnicu Vilcea", "Sibiu", 80),
                ("Rimnicu Vilcea", "Pitesti", 97),
                ("Sibiu", "Fagaras", 99),
                ("Fagaras", "Bucharest", 211),
                ("Pitesti", "Bucharest", 101),
                ("Bucharest", "Giurgiu", 90),
                ("Bucharest", "Urziceni", 85),
                ("Urziceni", "Hirsova", 98),
                ("Hirsova", "Eforie", 86),
                ("Urziceni", "Vaslui", 142),
                ("Vaslui", "Iasi", 92),
                ("Iasi", "Neamt", 87)
            ]
        
        # criar as cidades do mapa
        for rotulo, heuristica in self._vertices_dict.items():
            self.vertices[rotulo] = Vertice(rotulo, heuristica)
        
        # criar as ligações (arestas) entre as cidades    
        for origem, destino, custo in arestas:
            self.ligar(origem, destino, custo)
            
    #ida e volta
    def ligar(self, origem, destino, custo):
        self.vertices[origem].adicionar_adj(Adjacente(self.vertices[destino], custo))
        self.vertices[destino].adicionar_adj(Adjacente(self.vertices[origem], custo))
        
    def reset(self):
        for vertice in self.vertices.values():
            vertice.visitado = False