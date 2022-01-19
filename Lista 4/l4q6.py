def main():
    n = int(input()) # n é a quantidade de usuários

    tempo = [] # Lista com o tempo de espera de cada usuário

    for i in range(n): # Para cada usuário i,
        tempo.append(input()) # lê-se o tempo de espera dele e o adiciona na lista
    
    usuarios_ord_tempo = ordenacao(tempo) # Dado o tempo de espera, ordena os usuários do menor ao maior
                                          # tempo de espera

    t = [] # Lista com o tempo de espera total gasto por cada usuário

    for i in range(usuarios_ord_tempo): # Para cada usuário ordenado por tempo i,
       t[usuarios_ord_tempo[i]] = processar(usuarios_ord_tempo, i) # calcula-se o tempo total de espera
                                                       # de cada usuário. Como os usuários estão ordenados
                                                       # crescentemente por tempo, esse algoritmo processa
                                                       # de forma ótima os usuários.
    
    return t


    