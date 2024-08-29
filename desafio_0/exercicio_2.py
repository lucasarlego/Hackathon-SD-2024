# 1st step - Dado um array de números inteiros, escreva uma função que retorne o par de números com a menor diferença absoluta.
# 2nd step - Se houver mais de um par com a mesma diferença, retorne todos eles em uma lista. 
import numpy as np

def pares_menor_abs_diff(lista:list) -> list:
    """
    Encontra os pares de números em uma lista que tem a menor diferença absoluta.

    Esta função recebe uma lista de números inteiros, ordena a lista e calcula as diferenças absolutas
    entre os elementos consecutivos. Em seguida, encontra a menor diferença e retorna todos os pares de
    números que possuem essa menor diferença.

    Parâmetros:
    -----------
    lista : list
        Uma lista de números inteiros.

    Retorna:
    --------
    list
        Uma lista de tuplas, onde cada tupla contém um par de números consecutivos que têm a menor
        diferença absoluta na lista ordenada.

    Exemplo:
    --------
    >>> pares_menor_abs_diff([3, 8, 50, 23, 5, 1])
    [(3, 5), (5, 8)]
    """
    sort_lista = np.sort(lista)

    diferencas = np.abs(np.diff(sort_lista))

    menor_diferenca = np.min(diferencas)

    indices = np.where(diferencas == menor_diferenca)[0]

    pares = [(sort_lista[i], sort_lista[i + 1]) for i in indices]

    return pares


listas = [[3, 8, 50, 23, 5, 1], [16, 4, 8, 24, 56, 76, 90, 2]]

for i in listas:
    print(pares_menor_abs_diff(i))