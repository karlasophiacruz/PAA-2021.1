def caminho_maximo(G, s, t): # Será usado o algoritmo de Bellman-Ford de maneira inversa para achar o caminho
                                # máximo. Como Bellman-Ford encontra o caminho mínimo, basta aplicar os pesos
                                # opostos ao originais e aplicar o oposto ao resultado.

    dist = [float("-Inf")] * G.v() # Inicializar as distâncias em -infinito
    dist[s] = 0

    # O caminho mínimo entre dois vértices possui no máximo |V| - 1 arestas
    for _ in range(G.v() - 1): # Para todos os vértices, ... (Custo: O(|V|))
        for u, v in G.e(): # ..., Para cada u e v de uma aresta, ... (Custo: O(|E|))
            if dist[u] != float("-Inf") and dist[u] >= dist[v]: # Checa os vértices que não foram visitados e se
                                                                # a distância de u é maior ou igual a v, ...                                       
                dist[v] = dist[u] + 1 # ... se for, soma a distância de u a v, de modo a formar o caminho entre eles

    # Retorna a distância na posição de t, o qual indica o caminho máximo entre s e t.
    # Custo de tempo: O(|V|*|E|)
    # Custo de memória: O(|V|)
    return dist[t]