def gerar_asteriscos(n:int) -> list:
    """
    Gera uma lista de strings, onde cada string contém um número crescente de asteriscos.

    Dado um número inteiro `n`, esta função retorna uma lista de comprimento `n`, onde
    o elemento na posição `i` contém exatamente `i` asteriscos.

    Parâmetros:
    -----------
    n : int
        O número de strings na lista a ser gerada. Cada string contém `i` asteriscos, 
        onde `i` varia de 1 até `n`.

    Retorna:
    --------
    list
        Uma lista de strings. Cada string contém um número crescente de asteriscos,
        começando com 1 asterisco na primeira string e aumentando até `n` asteriscos
        na última string.

    Exemplo:
    --------
    >>> gerar_asteriscos(5)
    ['*', '**', '***', '****', '*****']
    """

    return list(map(lambda i: '*' * i, range(1, n + 1)))


ns = [5, 7, 9] 
for i in ns:
    lista = gerar_asteriscos(i)
    print(lista)