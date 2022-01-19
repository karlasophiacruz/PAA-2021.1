def main():
    c = int(input()) # c é a capacidade total da mochila
    n = int(input()) # n é a quantidade de itens possíveis

    v = [] # Lista do valor de cada item

    for i in range(n): # Custo: O(n)
        v.append(int(input())) # Para cada item, tem-se o seu valor correspondente

    mergeSortDecresc(v) # Custo: O(n log(n))
                        # Como o peso de todos os itens são iguais (unitário), para se ter o maior valor
                        # possível na mochila, basta ordenar de forma decrescente os itens pelo seu valor.
                        # Assim, a mochila sempre terá valor máximo, tornando a solução ótima e eficiente.

    peso = 0 # Valor atual do peso da mochila
    valor = 0 # Valor atual do valor total de itens na mochila

    for i in range(n): # Custo: O(n)
        if (peso < c): # Para cada item, checa-se se o peso atual da mochila é menor que o suportado ...
            valor += v[i] # ... se for, coloca o item na mochila, somando o seu valor ao valor atual e
            peso += 1 # aumentando o peso da mochila. Como o peso de todos os itens é unitário, basta
                      # incrementar o peso em 1 unidade.
    
    # Como considera-se o maior custo realizado no algoritmo, seu custo se dará na ordenação, nesse caso,
    # O(n log(n)). Porém, independente do algoritmo de ordenação escolhido, o problema da mochila pode ser
    # resolvido em tempo polinomial.
    return valor

