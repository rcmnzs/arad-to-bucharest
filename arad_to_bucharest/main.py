from grafo import Grafo
from gulosa import Gulosa
from a_estrela import AEstrela
from largura import Largura

mapa = Grafo()

# Arad
# print("Busca Gulosa:")
# g = Gulosa(mapa.vertices["Bucharest"])
# g.busca(mapa.vertices["Arad"])
# g.exibir_caminho()
# mapa.reset()

# print("Busca A*:")
# a = AEstrela(mapa.vertices["Bucharest"])
# a.busca(mapa.vertices["Arad"])
# a.exibir_caminho()
# mapa.reset()

# print("Busca em Largura:")
# l = Largura(mapa.vertices["Bucharest"])
# l.busca(mapa.vertices["Arad"])
# l.exibir_caminho()
# mapa.reset()

# Lugoj
print("Busca Gulosa:")
g = Gulosa(mapa.vertices["Bucharest"])
g.busca(mapa.vertices["Lugoj"])
g.exibir_caminho()
mapa.reset()

print("Busca A*:")
a = AEstrela(mapa.vertices["Bucharest"])
a.busca(mapa.vertices["Lugoj"])
a.exibir_caminho()
mapa.reset()

print("Busca em Largura:")
l = Largura(mapa.vertices["Bucharest"])
l.busca(mapa.vertices["Lugoj"])
l.exibir_caminho()
mapa.reset()