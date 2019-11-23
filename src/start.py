# ==========================================
#  DIRETÓRIO: START.PY
# Este arquivo consta todas as funcoes 
# necessarias para o tratamento das variaveis
# Ultima alteracao: 23/11/2019, by: Alisson
# ===========================================

def replace(arquivo, posicao):
    variavel = arquivo[posicao][1]  # peega o valor
    variavel = variavel.replace('"', '')  # substitui as aspas por nada
    variavel = variavel.replace(',', '')  # substitui a vitgula por nada

    return variavel

# funcao que faz a passagem dos enderecos para decimal
def decimal(endereco):
    # corto o endereco em 4 partes, com o delimitador sendo o '.'
    endereco_decimal = [int(endereco.split(".")[0]), int(endereco.split(
        ".")[1]), int(endereco.split(".")[2]), int(endereco.split(".")[3])]

    return endereco_decimal

# funcao que faz a passagem dos enderecos para binario
def binario(endereco):
    endereco_binario = [int(endereco.split(".")[0]), int(endereco.split(
        ".")[1]), int(endereco.split(".")[2]), int(endereco.split(".")[3])]
    # passo os valores para binário e verifico caso algum seja igual a vazio, se for dou o valor 0 para ele
    p0 = d2b(int(endereco_binario[0]))
    if p0 == "":
        p0 = 0

    p1 = d2b(int(endereco_binario[1]))
    if p1 == "":
        p1 = 0

    p2 = d2b(int(endereco_binario[2]))
    if p2 == "":
        p2 = 0

    p3 = d2b(int(endereco_binario[3]))
    if p3 == "":
        p3 = 0

    contador = 0
    faltante = "0"

    # verifico se falta os 0 a esquerda
    if (len(str(p0)) < 8):
        contador = 8 - len(str(p0))
        for i in range(contador - 1):
            faltante = faltante + "0"
        aux = faltante + str(p0)
        p0 = str(aux)
    
    faltante = "0"

    if (len(str(p1)) < 8):
        contador = 8 - len(str(p1))
        for i in range(contador - 1):
            faltante = faltante + "0"
        aux = faltante + str(p1)
        p1 = str(aux)

    faltante = "0"

    if (len(str(p2)) < 8):
        contador = 8 - len(str(p2))
        for i in range(contador - 1):
            faltante = faltante + "0"
        aux = faltante + str(p2)
        p2 = str(aux)

    faltante = "0"

    if (len(str(p3)) < 8):
        contador = 8 - len(str(p3))
        for i in range(contador - 1):
            faltante = faltante + "0"
        aux = faltante + str(p3)
        p3 = str(aux)    

    # concateno todos em uma única variável
    endereco_binario = [str(p0), str(p1), str(p2), str(p3)]

    return endereco_binario

# funcao recursiva que passa um valor decimal para binario
def d2b(n):
    if n == 0:
        return ''
    else:
        return d2b(n//2) + str(n % 2)

def formatar(endereco):
    aux = []
    count = 0
    a = ""

    for i in endereco:              # passo por todo o endereco
        a = a + i                   # a recebe o valor do endereco 
        count = count + 1           # contador de posicoes
        if ((count + 1) == 9):      # caso seja a 1 posicao (8 posicao)
            aux.append(a)           # junto em aux
            a = ""                  # a recebe nada
        elif ((count + 1) == 17):   # caso seja a 2 posicao (16 posicao)
            aux.append(a)           # junto tudo em aux
            a = ""                  # a recebe nada
        elif ((count + 1) == 25):   # caso seja a 3 posicao (24 posicao)
            aux.append(a)           # junto tudo em aux
            a = ""                  # a recebe nada
        elif ((count + 1) == 33):   # caso seja a 4 posicao (32 posicao)
            aux.append(a)           # junto tudo em aux
            a = ""                  # a recebe nada

    return aux