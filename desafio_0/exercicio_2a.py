# Dado um array de números inteiros, escreva uma função que retorne o par de números com a menor diferença absoluta.
# Se houver mais de um par com a mesma diferença, retorne todos eles em uma lista.
# Além disso, a função deve permitir os seguintes parâmetros opcionais: 

# allow_duplicates (booleano)
# Se definido como False, os pares de números não podem conter valores duplicados.

# sorted_pairs (booleano)
# Se definido como True, os pares no resultado devem estar ordenados em ordem crescente.

# unique_pairs (booleano)
# Se definido como True, a função deve retornar apenas pares únicos (ou seja, (a, b) e (b, a) são considerados o mesmo par). 



import numpy as np

def pares_menor_abs_diff(lista: list, allow_duplicates: bool = True, sorted_pairs: bool = False, unique_pairs: bool = True) -> list:
    """
    Encontra os pares de números em uma lista que tem a menor diferença absoluta.

    Parâmetros:
    -----------
    lista : list
        Uma lista de números inteiros.
    allow_duplicates : bool, opcional
        Se False, pares não podem conter valores duplicados (padrão é True).
    sorted_pairs : bool, opcional
        Se True, os pares no resultado são ordenados em ordem crescente (padrão é False).
    unique_pairs : bool, opcional
        Se True, retorna apenas pares únicos (padrão é True).

    Retorna:
    --------
    list
        Uma lista de tuplas, onde cada tupla contém um par de números com a menor diferença absoluta na lista.

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

    if not allow_duplicates:
        pares = [p for p in pares if p[0] != p[1]]

    if unique_pairs:
        pares = list(set(tuple(sorted(p)) for p in pares))

    if sorted_pairs:
        pares.sort()

    return pares

# Testes
listas = [[3, 8, 50, 23, 5, 1], [16, 4, 8, 24, 56, 76, 90, 2]]

for i in listas:
    print(pares_menor_abs_diff(i))
    print(pares_menor_abs_diff(i, allow_duplicates=False))
    print(pares_menor_abs_diff(i, sorted_pairs=True))
    print(pares_menor_abs_diff(i, unique_pairs=False))
    print(pares_menor_abs_diff(i, allow_duplicates=False, sorted_pairs=True, unique_pairs=True))
