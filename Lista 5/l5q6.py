def custominimo(m, n, i):
    if len(m) == 1: # Fim da recursão, caso só haja 1 corte...
        return n # retorna o próprio tamanho da String

    c_e = 0 # Custo do lado esquerdo
    c_d = 0 # Custo do lado direito

    # Aplica o algoritmo de dividir e conquistar para calcular o custo
    if i > 0: # Recursão para o lado esquerdo, caso seja positivo...
        c_e = 10000000
        m_e = m[0 : i]
        nl = m[i]

        for j in range(len(m_e)):
            c_e = min(custominimo(m_e, nl, j), c_e)
    
    if i < (len(m) - 1): # Recursão para o lado direito, caso seja menor que o tamanho...
        c_d = 10000000
        m_d = m[(i + 1) : len(m)]
        nr = n - m[i]

        for j in range(len(m_d)):
            m_d[j] -= m[i]

        for j in range(len(m_d)):
            c_d = min(custominimo(m_d, nr, j), c_d)

    # Retorna o custo total mínimo
    return n + c_e + c_d 

def cost(m, n):
    custo = n * len(m) # Custo máximo da divisão

    for i in range(len(m)): # Calcula e checa o menor custo entre o custo atual e o calculado
        custo = min(custominimo(m, n, i), custo)
    
    # Retorna o custo
    return custo

def main():
    # Valores da questão
    n = 20 # Tamanho da String
    m = [3, 10] # Lista com os cortes da string

    m.sort() # Para que o algoritmo funcione, é necessário que os cortes estejam ordenados

    # Retorna o custo mínimo, dado o tamanho da string e a lista com os cortes da string
    return cost(m, n)