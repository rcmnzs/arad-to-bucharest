from abc import ABC, abstractmethod

class VetorOrdenado(ABC):
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_pos = -1
        self.lista_de_vertices = [None] * capacidade

    @abstractmethod
    def chave(self, elemento):
        pass

    @abstractmethod
    def formatar(self, elemento):
        pass

    def inserir(self, novo):
        if self.ultima_pos + 1 == self.capacidade:
            raise ValueError("O vetor está cheio!")

        i = self.ultima_pos
        while i >= 0 and self.chave(self.lista_de_vertices[i]) > self.chave(novo):
            self.lista_de_vertices[i + 1] = self.lista_de_vertices[i]
            i -= 1

        self.lista_de_vertices[i + 1] = novo
        self.ultima_pos += 1

    def imprimir(self):
        for i in range(0, self.ultima_pos + 1):
            print(f"{i} - {self.formatar(self.lista_de_vertices[i])}")

# baseado na heurística
class VetorGuloso(VetorOrdenado):
    def chave(self, adj):
        return adj.vertice.dist_obj

    def formatar(self, adj):
        return f"{adj.vertice.rotulo} - {adj.vertice.dist_obj}"

# baseado na distância pela estrada + heurística
class VetorAEstrela(VetorOrdenado):
    def chave(self, adj):
        return adj.vertice.dist_obj + adj.custo

    def formatar(self, adj):
        h = adj.vertice.dist_obj
        return f"{adj.vertice.rotulo} | h: {h} | estrada: {adj.custo} | A*: {h + adj.custo}"
    
# baseado na distância pela estrada
class VetorCusto(VetorOrdenado):
    def chave(self, adj):
        return adj.custo

    def formatar(self, adj):
        return f"{adj.vertice.rotulo} - estrada: {adj.custo}"