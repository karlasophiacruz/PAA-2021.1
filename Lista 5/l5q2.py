def pegarMoedas(tabuleiro[n][m]):
    moedas = [n + 1][m + 1] # Matriz com o caminho a ser realizado pelo robô

    for i in range(n + 1): # Percorre a linha (Custo: O(n))
        for j in range(m + 1): # Percorre a coluna (Custo: O(m))
            moedas[i][j] = max(moedas[i + 1][j], moedas[i][j + 1]) + tabuleiro[i][j] 
            # Escolhe o caminho com mais moedas e soma se houver moeda na posição atual do tabuleiro

    # Retorna o caminho do robô e o número máximo de moedas que será recolhido.
    # Custo total do algoritmo: O(n*m)
    return moedas, moedas[n][m]