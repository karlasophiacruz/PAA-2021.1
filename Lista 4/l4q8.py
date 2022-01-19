def main():
    v = int(input()) # v é a quantidade de vértices
    e = int(input()) # e é a quantidade de arestas

    g = Grafo(v) # g é o grafo criado com v vértices

    for i in range(e): # Para cada aresta i,
        v1 = int(input()); v2 = int(input());  p = int(input()) # lê-se os vértices e o peso dessa aresta

        g.addAresta(v1, v2, p) # Cria a aresta e a adiciona ao grafo g

    agm = kruskal_invertido(g) # Para ter um conjunto Feedback de arestas de peso total mínimo, é necessário
                               # encontrar uma Árvore Geradora Máxima (AGM). Para isso, aplica-se o algoritmo
                               # de Kruskal invertido, ou seja, ao invés de encontrar Árvore Geradora Mínima,
                               # ele encontrará uma Árvore Geradora Máxima. 
    
    f = g.arestas # O conjunto Feedback de arestas de peso total mínimo é um subconjunto de arestas do grafo...

    for aresta in agm.arestas: # ... subtraído de cada aresta de uma Árvore Geradora Máxima,
        f.remove(aresta) # pois G - F = AGM => G - AGM = F

    return f



    