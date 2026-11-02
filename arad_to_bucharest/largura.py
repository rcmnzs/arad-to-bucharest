from vetor_ordenado import VetorCusto

class Largura:
    def __init__(self, destino):
        self.destino = destino
        self.status = False
        self.caminho = []
        self.dist_total = 0

    def busca(self, origem):
        print(f"\nCidade atual: {origem.rotulo}")
        origem.visitado = True
        self.caminho.append(origem.rotulo)

        if origem.rotulo == self.destino.rotulo or origem.dist_obj == 0:
            self.status = True
        else:
            vetor = VetorCusto(len(origem.adjacentes))

            for adjacente in origem.adjacentes:
                if not adjacente.vertice.visitado:
                    vetor.inserir(adjacente)

            vetor.imprimir()

            if vetor.ultima_pos != -1:
                escolhido = vetor.lista_de_vertices[0]
                self.dist_total += escolhido.custo
                self.busca(escolhido.vertice)

    def exibir_caminho(self):
        if not self.status:
            print("Nenhum caminho encontrado. Percurso feito: " + " -> ".join(self.caminho))
        else:
            print("Caminho: " + " -> ".join(self.caminho))
            print(f"Distância total: {self.dist_total}\n")
        print("----------\n")