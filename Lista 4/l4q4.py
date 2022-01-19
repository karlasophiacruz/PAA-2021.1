def main():
    m = int(input()) # m é a quantidade de restrições
    n = int(input()) # n é a quantidade de variáveis

    restricoes = []  # lista com todas as restrições
    relacoes = []     # lista com as relações das variáveis

    for i in range(m): # Custo: O(m)
        restricoes.append(input()) # Lê-se as restrições e as adiciona na lista

    igualdades, desigualdades = ler_restricoes(restricoes) #Separa as restrições em igualdades e desigualdades

    for x in range(n): # Custo: O(n)
        relacoes.append(Relacao(x, 0)) # Inicialmente, adiciona na lista de relações as componentes conexas
                                       # com rank = 0

    for igualdade in igualdades: # Como tem-se uma relação de igualdade, é feito um union, a fim de construir a 
        union(relacoes, igualdade[0], igualdade[1]) # componente conexa, tendo um custo de aproximadamente O(1)

    for desigualdade in desigualdades: # Como tem-se uma relação de desigualdade, é feito um find, a fim de
        par_a = find(relacoes, desigualdade[0]) # validar a relação, tendo um custo de 0(log n). Isso é 
        par_b = find(relacoes, desigualdade[1]) # realizado ao checar o pai de cada termo da desigualdade, 
                                                # pois, como foi realizado um union na igualdade...

        if par_a == par_b: # ... se ambos possuirem o mesmo pai, significa que eles são iguais, o que é falso,
            return False # consequentemente invalidando as restrições
    
    return True # ... se todos as desigualdades forem validadas, ou seja, não foi encontrado nenhum pai em
                # comum nas relações de desigualdade, significa que são diferentes, o que é verdadeiro,
                # consequentemente validando as restrições


