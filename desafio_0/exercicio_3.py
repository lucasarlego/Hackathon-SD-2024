# Escreva uma função que retorne todos os subconjuntos de um conjunto de números. 
# Por exemplo, se a entrada for [1, 2], a saída deve ser [[], [1], [2], [1, 2]].
# Observação: Utilize a linguagem de programação que você mais domina


from itertools import chain, combinations

def todos_subconjuntos(conjunto:list) -> list:
    """
    Retorna todos os subconjuntos possíveis de um conjunto de números.

    Parâmetros:
    -----------
    conjunto : list
        Uma lista de números inteiros.

    Retorna:
    --------
    list
        Uma lista contendo todos os subconjuntos possíveis do conjunto de entrada.
        Cada subconjunto é representado como uma lista.

    Exemplo:
    --------
    >>> todos_subconjuntos([1, 2])
    [[], [1], [2], [1, 2]]
    """
    # Gera todas as combinações possíveis para todos os tamanhos
    return [list(subconjunto) for subconjunto in chain.from_iterable(combinations(conjunto, r) for r in range(len(conjunto) + 1))]

# Exemplo de uso
conjuntos = [[1, 2], [1, 2, 3]]

for i in conjuntos:
    print(todos_subconjuntos(i))
