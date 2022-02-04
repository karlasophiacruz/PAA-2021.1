def subsetsum(A, n, t):
    # Casos bases para a recursão:
    if t == 0: # Checa se a soma for 0...
        return True # ... será sempre verdadeiro

    if n == 0: # Se o tamanho for zero, então é um conjunto vazio, ...
        return False # ... logo, é Falso
    
    if A[n - 1] > t: # Checa se o último elemento é maior que a soma, ...
        return subsetsum(A, n - 1, t) # se for, é ignorado e retorna a recursão sem ele
    
    # Caso contrário, retorna a recursão checando com e sem o último elemento
    return subsetsum(A, n - 1, t) or subsetsum(A, n - 1, t - A[n - 1] )

def is_subset(A, t):
    # Valores de exemplo
    A = [3, 4, 5, 6, 8] # A é o conjunto que será checado
    t = 8 # t é a soma que tentará ser encontrada
    n = len(A) # n é o tamanho do conjunto

    # Retorna True se é um Subset Sum e False caso contrário
    return subsetsum(A, n, t)