from warnings import warn
import heapq
from math import exp

class No:
    def __init__(self, posicao=None, pai=None):
        self.posicao = posicao
        self.pai = pai
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.posicao == other.posicao

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __repr__(self):
        return print(f'Posição:{self.posicao},Custo:{self.f}')


def retorna_caminho(no_atual):
    path = []
    current = no_atual
    while current is not None:
        path.append(current.posicao)
        current = current.pai
    return path[::-1]


def aestrela(sala, inicio, fim, diagonal=False):
    no_inicial = No(inicio)
    no_final = No(fim)
    lista_aberta = []
    lista_fechada = []
    heapq.heapify(lista_aberta)
    heapq.heappush(lista_aberta, no_inicial)
    it = 0
    max_it = (len(sala[0]) * len(sala) // 2)
    quad_ad = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if diagonal:
        quad_ad = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)
    while len(lista_aberta) > 0:
        it += 1

        if it > max_it:
            return retorna_caminho(no_atual)

        no_atual = heapq.heappop(lista_aberta)
        lista_fechada.append(no_atual)

        if no_atual == no_final:
            return retorna_caminho(no_atual)

        filhos = []

        for new in quad_ad:

            posicao_no = (no_atual.posicao[0] + new[0], no_atual.posicao[1] + new[1])

            if posicao_no[0] > (len(sala) - 1) or posicao_no[0] < 0 or posicao_no[1] > (
                    len(sala[len(sala) - 1]) - 1) or posicao_no[1] < 0:
                continue

            if sala[posicao_no[0]][posicao_no[1]] == 0:
                continue

            novo = No(posicao_no, no_atual)

            filhos.append(novo)

        # Loop through children
        for filho in filhos:
            # Child is on the closed list
            if len([closed_child for closed_child in lista_fechada if closed_child == filho]) > 0:
                continue

            # Create the f, g, and h values
            filho.g = no_atual.g + 1
            filho.h = ((filho.posicao[0] - no_final.posicao[0]) ** 2) + (
                        (filho.posicao[1] - no_final.posicao[1]) ** 2) + exp(sala[filho.posicao[0]][filho.posicao[1]])
            filho.f = filho.g + filho.h

            # Child is already in the open list
            if len([open_node for open_node in lista_aberta if
                    filho.posicao == open_node.posicao and filho.g > open_node.g]) > 0:
                continue


            heapq.heappush(lista_aberta, filho)

    warn("não foi possível achar o caminho")
    return None


sala = [[0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 10, 0, 1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 10, 10, 10, 0, 1, 10, 10, 10, 10, 10, 10, 10, 10, 0, 1, 1, 1, 1, 0],
        [0, 10, 10, 10, 0, 1, 10, 10, 10, 10, 10, 10, 10, 10, 0, 1, 1, 1, 1, 0],
        [0, 10, 10, 10, 0, 1, 10, 10, 10, 10, 10, 10, 10, 10, 0, 1, 1, 1, 1, 0],
        [0, 10, 10, 10,10, 1, 10, 10, 10, 10, 10, 10, 10, 10, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 0],
        [0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 0],
        [0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 0],
        [0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0],
        [0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 5, 0],
        [0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 5, 0],
        [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (0, 4)
end = (13, 18)
print(aestrela(sala, start, end, True))