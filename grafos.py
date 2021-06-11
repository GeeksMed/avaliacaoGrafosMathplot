# Exemplo grafo em python
from collections import defaultdict as dd
import networkx as nx
import matplotlib.pyplot as plt

class Grafo(object):
    """    Implementando básica de um grafo    """

    def __init__(self, arestas, direcionado = False):
        """        Inicializar a estrutura base do grafo        """
        self.__adj = dd(set)
        self.__direcionado = direcionado
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        return list(self.__adj.keys())

    def get_arestas(self):
        return [(k,v) for k in self.__adj.keys() for v in self.__adj[k]]

    def get_adj(self):
        return self.__adj

    def adiciona_arestas(self, arestas):
        for u,v in arestas:
            self.adiciona_arco(u, v)

    def adiciona_arco(self, u, v):
        self.__adj[u].add(v)
        if not self.__direcionado:
            self.__adj[v].add(u)

    def existe_aresta(self, u, v):
        return u in self.__adj and v in self.__adj[u]

    def __len__(self):
        return len(self.__adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.__adj))

    def __getitem__(self, v):
        return self.__adj[v]

    def mostra_grafo(self):
        """     Trabalhando com networkx    """
        g = nx.Graph()
        g.add_nodes_from(self.get_vertices())
        g.add_edges_from(self.get_arestas())
        """
        print(g.nodes)
        print(g.number_of_nodes())
        print(g.edges)
        print(g.number_of_edges())
        """
        nx.draw(g, with_labels=1)
        plt.show()
    

def menu():
    opcao = input(f"""
-----------------------------------------------
            Algoritmos de Grafos
-----------------------------------------------
                Menu Principal
-----------------------------------------------
1 - Criar um Grafo
2 - Exibir um Grafo
3 - Finalizar o programa
-----------------------------------------------
Informe a opção: """)
    return opcao


def submenu():
    opcao = input("""
-----------------------------------------------
                Menu Grafo
-----------------------------------------------
1 - Adicionar Aresta
2 - Voltar Menu Principal
-----------------------------------------------
Informe a opção: """)
    return opcao


def avaliacao():
    while True:
        opcao = menu()
        try:
            if int(opcao) == 1:
                arestas = []
                # Criando nosso grafo
                grafo = Grafo(arestas, True)
                while True:
                    op = submenu()
                    try:
                        if int(op) == 1:
                            aresta = []
                            u = input('\nFavor informar primeiro vertice da aresta: ')
                            v = input('Favor informar segundo vertice da aresta: ')
                            aresta.append((u, v))
                            grafo.adiciona_arestas(aresta)
                        elif int(op) == 2:
                            print("\nVoltando ao Menu Principal.")
                            break
                        else:
                            print("Opção informada com erro. Favor informar novamente.")
                    except:
                        print("Opção informada com erro. Favor informar novamente.")
            elif int(opcao) == 2:
                grafo.mostra_grafo()
            elif int(opcao) == 3:
                print("\nObrigado por utilizar o programa.")
                break
            else:
                print("Opção informada com erro. Favor informar novamente.")
        except:
            print("Opção informada com erro. Favor informar novamente.")


if __name__ == '__main__':
    avaliacao()