def subcontigua(a[]): # Entrada com a lista de números
    sequencia_max = [] # Lista com a subsequência contígua de soma máxima
    soma = 0 # Valor da soma atual
    soma_maxima = -1000 # Valor da soma máxima

    for i in len(a): # Percorrendo a lista (Custo: O(n))
        soma = max(a[i], soma + a[i]) # Pega o valor máxima entre a soma dos valores contíguos e o termo atual
        sequencia_max.append(a[i]) # Adiciona o termo atual na sequência máxima

        if soma == a[i]: # Checa se a soma é igual ao termo atual ...
            del sequencia_max[0 : i] # ... se for, então a sequência formada não é máxima. Dessa forma, remove
                                     # todos os termos até o atual para a sequência máxima ser reiniciada
        
        if soma > soma_maxima: # Checa se a soma atual é maior que a soma máxima ...
            soma_maxima = soma # ... se for, a soma atual é a nova soma máxima
    
    # Retorna a subsequência contígua de soma máxima e a soma máxima
    return sequencia_max, soma_maxima



