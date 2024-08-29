# Escreva uma função que retorne todos os subconjuntos de um conjunto de números. 
# A função deve permitir os seguintes parâmetros opcionais:

# max_size (inteiro): Limita o tamanho máximo dos subconjuntos.
# min_size (inteiro): Define o tamanho mínimo dos subconjuntos.
# distinct_only (booleano): Se definido como True, a função deve garantir que os subconjuntos não contenham elementos duplicados.
# sort_subsets (booleano): Se definido como True, os subconjuntos e os elementos dentro dos subconjuntos devem ser retornados em ordem crescente.

from itertools import combinations

def todos_subconjuntos(conjunto: list, max_size: int = None, min_size: int = 0, distinct_only: bool = True, sort_subsets: bool = False) -> list:
    """
    Retorna todos os subconjuntos possíveis de um conjunto de números com base em parâmetros opcionais.

    Parâmetros:
    -----------
    conjunto : list
        Uma lista de números inteiros.
    max_size : int, opcional
        Limita o tamanho máximo dos subconjuntos (padrão é None, o que significa sem limite).
    min_size : int, opcional
        Define o tamanho mínimo dos subconjuntos (padrão é 0).
    distinct_only : bool, opcional
        Se True, garante que os subconjuntos não contenham elementos duplicados (padrão é True).
    sort_subsets : bool, opcional
        Se True, ordena os subconjuntos e os elementos dentro dos subconjuntos (padrão é False).

    Retorna:
    --------
    list
        Uma lista contendo todos os subconjuntos possíveis do conjunto de entrada, conforme os parâmetros fornecidos.
        Cada subconjunto é representado como uma lista.

    Exemplo:
    --------
    >>> todos_subconjuntos([1, 2, 2], max_size=2, min_size=1, distinct_only=True, sort_subsets=True)
    [[], [1], [1, 2], [2]]
    """
    if distinct_only:
        conjunto = list(set(conjunto))
    
    resultado = []
    
    for r in range(min_size, len(conjunto) + 1):
        if max_size is not None and r > max_size:
            break
        resultado.extend(combinations(conjunto, r))
    
    resultado = [list(subconjunto) for subconjunto in resultado]
    
    if sort_subsets:
        resultado = [sorted(subconjunto) for subconjunto in resultado]
        resultado.sort()
    
    return resultado


conjuntos = [[1, 2], [1, 2, 3], [1, 2, 2]]

for count, i in enumerate(conjuntos):
    print(f"{count} - no param - {todos_subconjuntos(i)}")
    print(f"{count} - max_size - {todos_subconjuntos(i, max_size=2)}")
    print(f"{count} - min_size, max_size, distinct_only - {todos_subconjuntos(i, min_size=1, max_size=2, distinct_only=True)}")
    print(f"{count} - sort_subsets - {todos_subconjuntos(i, sort_subsets=True)}")
    print(f"{count} - all params- {todos_subconjuntos(i, min_size=1, max_size=2, distinct_only=True, sort_subsets=True)}")
    print("\n\n")