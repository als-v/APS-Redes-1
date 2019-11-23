# DIRETÓRIO: FUNCT.PY
# ALUNOS: ALISSON E CAIO
# NESTE ARQUIVO TEMOS OS CODIGOS PARA RESOLUCAO DOS EXERCICIOS

from src import start as st

# funcao que verifica se a mascara da rede e valida


def mask_validation(endereco):
    for i in range(0, (len(endereco) - 1)):
        for j in range(i + 1, (len(endereco) - 1)):
            if(endereco[j] > endereco[i]):
                return False
    return True

# funcao que verifica se o ip da rede e valido


def ip_validation(enderecoB):
    # verifico se o endereco comeca em 0
    if (int(enderecoB[0]) == 0):
        return False

    # verifico se o endereco comeca com 127
    if (int(enderecoB[0]) == 127):
        return False

    # verifico se o endereco possui apenas o identificador 255
    if not ((classe_ip(enderecoB) == "A") or (classe_ip(enderecoB) == "B") or (classe_ip(enderecoB) == "C")):
        return False

    # verifico se o identificador possui 0's
    if (classe_ip(enderecoB) == "A"):
        if((enderecoB[1] == 0) and (enderecoB[2] == 0) and (enderecoB[3] == 0)):
            return False
    elif (classe_ip(enderecoB) == "B"):
        if((enderecoB[2] == 0) and (enderecoB[3] == 0)):
            return False

    # se o endereco for classe C ele nao pode terminar com 0 ou 255
    if (classe_ip(enderecoB) == "C"):
        if((enderecoB[3] == 255) or (enderecoB[3] == 0)):
            return False

    # caso passe por todas as validacoes, o ip e valido
    return True


# funcao que verifica a classe do IP
def classe_ip(endereco):
    A = False
    errA = False
    a = "A"
    errAA = "O endereço aparenta ser da classe A, porém é inválido!"
    B = False
    errB = False
    b = "B"
    errBB = "O endereço aparenta ser da classe B, porém é inválido!"
    C = False
    errC = False
    c = "C"
    errCC = "O endereço aparenta ser da classe C, porém é inválido!"
    err = "Endereco invalido"

    if ((endereco[0] <= 126) and (endereco[0] > 0)):
        A = True
        if(((endereco[1] == 0) and (endereco[2] == 0) and (endereco[3] == 0)) or ((endereco[1] == 255) and (endereco[2] == 255) and (endereco[3] == 355))):
            errA = True

    if ((endereco[0] <= 191) and (endereco[0] > 127)):
        B = True
        if(((endereco[2] == 255) and (endereco[3] == 255)) or ((endereco[2] == 0) and (endereco[3] == 0))):
            errB = True

    if ((endereco[0] <= 223) and (endereco[0] > 191)):
        C = True
        if((endereco[3] < 1) and (endereco[3] > 254)):
            errC = True

    if ((A == True) and (errA == False)):
        return a
    elif ((A == True) and (errA == True)):
        return errAA
    elif ((B == True) and (errB == False)):
        return b
    elif ((B == True) and (errB == True)):
        return errBB
    elif ((C == True) and (errC == False)):
        return c
    elif ((C == True) and (errC == True)):
        return errCC
    else:
        return err

# calcula o ip da rede e de broadcast
def ip_redebroadcast(netMask, flag):
    count_pos = 0
    count_zero = 0
    count_um = 0

    # acho a posicao do ultimo numero 1
    for i in netMask:
        for j in i:
            count_pos = count_pos + 1
            if (j == "1"):
                count_um = count_pos
            elif (j == "0"):
                count_zero = count_zero + 1

    if (count_um >= 0 and count_um < 9):        # caso esteja no na primeira parte do endereco
        if (flag == 0):                         # caso eu queira o ip da rede
            ip_rede = []
            for i in range(count_um):           # faco uma copia ate essa posicao
                ip_rede.append(netMask[0][i])
            for j in range(8 - count_um):       # seto tudo depois dela em 0
                ip_rede.append("0")
            for i in range(3):                  # como ainda tem 3 partes do endereco, seto em 0 para as demais partes
                for j in range(8):
                    ip_rede.append("0")
            ip_rede = st.formatar(ip_rede)      # formato o endereco
            return ip_rede                      # retorno o ip da rede
        elif (flag == 1):                       # caso eu queira o ip broadcast, sigo a mesma logica acima
            ip_broadcast = []
            for i in range(count_um):
                ip_broadcast.append(netMask[0][i])
            for j in range(8 - count_um):
                ip_broadcast.append("1")
            for i in range(3):
                for j in range(8):
                    ip_broadcast.append("1")
            ip_broadcast = st.formatar(ip_broadcast)
            return ip_broadcast
    elif (count_um >= 9 and count_um < 17):         # caso esteja na segunda parte do endereco
        if (flag == 0):                             # caso eu queira o ip da rede
            ip_rede = []
            for i in range(8):                      # faco uma copia da primeira parte
                ip_rede.append(netMask[0][i])
            sobra = count_um - 8                    # tenho a sobra, que recebe a posicao que o ultimo um esta nessa segunda parte do endereco
            for i in range(sobra):                  # copio tudo ate chegar nele
                ip_rede.append(netMask[1][i])
            sobra = 8 - sobra                       # logo apos, sobra recebe a quantidade que falta para terminar a segunda parte do endereco
            for i in range(sobra):                  # logo, seto tudo em 0
                ip_rede.append("0")
            for i in range(2):                      # apos isso, seto as 2 ultimas partes restantes em 0
                for j in range(8):
                    ip_rede.append("0")
            ip_rede = st.formatar(ip_rede)          # formato o endereco
            return ip_rede                          # retorno o ip da rede
        elif (flag == 1):                           # caso queira o ip broadcast, sigo a mesma logica acima
            ip_broadcast = []
            for i in range(8):                     
                ip_broadcast.append(netMask[0][i])
            sobra = count_um - 8                   
            for i in range(sobra):                 
                ip_broadcast.append(netMask[1][i])
            sobra = 8 - sobra                       
            for i in range(sobra):                  
                ip_broadcast.append("1")
            for i in range(2):                      
                for j in range(8):
                    ip_broadcast.append("1")            
            ip_broadcast = st.formatar(ip_broadcast)
            return ip_broadcast
    elif (count_um >= 17 and count_um < 25):        # caso esteja na terceira parte do endereco
        if (flag == 0):                             # caso queira ip da rede
            ip_rede = []
            for i in range(8):                      # faco uma copia da primeira parte
                ip_rede.append(netMask[0][i])
            for i in range(8):                      # faco uma copia da segunda parte
                ip_rede.append(netMask[1][i])
            sobra = count_um - 16                   # sobra recebe a posicao do ultimo 1
            for i in range(sobra):                  # copio tudo ate o ultimo 1
                ip_rede.append(netMask[2][i])
            sobra = 8 - sobra                       # sobra recebe a quantidade de elementos que precisa para terminar o endereco
            for i in range(sobra):                  # seto tudo apos isso em 0
                ip_rede.append("0")
            for i in range(8):                      # na ultima parte do endereco, seto tudo em 0
                ip_rede.append("0")
            ip_rede = st.formatar(ip_rede)          # formato o endereco
            return ip_rede                          # retorno ip da rede
        elif (flag == 1):                           # caso eu queira o ip broadcast, sigo a mesma logica acima
            ip_broadcast = []
            for i in range(8):
                ip_broadcast.append(netMask[0][i])
            for i in range(8):
                ip_broadcast.append(netMask[1][i])
            sobra = count_um - 16
            for i in range(sobra):
                ip_broadcast.append(netMask[2][i])
            sobra = 8 - sobra
            for i in range(sobra):
                ip_broadcast.append("1")
            for i in range(8):
                ip_broadcast.append("1") 
            ip_broadcast = st.formatar(ip_broadcast)
            return ip_broadcast              
    elif (count_um >= 25 and count_um < 33):            # caso ele esteja na ultima parte do endereco
        if (flag == 0):                                 # caso eu queira o ip da rede
            ip_rede = []
            for i in range(8):                          # faco uma copia da primeira parte do endereco
                ip_rede.append(netMask[0][i])
            for i in range(8):                          # faco uma copia da segunda parte do endereco   
                ip_rede.append(netMask[1][i])           
            for i in range(8):                          # faco uma copia da terceira parte do endereco
                ip_rede.append(netMask[2][i])
            sobra = 32 - count_um                       # variavel sobra recebe o valor que falta para chegar no 1
            for i in range(8 - sobra):                  # copio tudo ate ele
                ip_rede.append(netMask[3][i])
            for i in range(sobra):                      # logo apos, seto tudo que vem depois do ultimo 1 em 0
                ip_rede.append("0")
            ip_rede = st.formatar(ip_rede)              # formato o endereco
            return ip_rede                              # retorno o ip da rede
        elif (flag == 1):                               # caso eu queira o ip broadcast, sigo a mesma logica acima
            ip_broadcast = []
            for i in range(8):
                ip_broadcast.append(netMask[0][i])
            for i in range(8):
                ip_broadcast.append(netMask[1][i])
            for i in range(8):
                ip_broadcast.append(netMask[2][i])
            sobra = 32 - count_um
            for i in range(8 - sobra):
                ip_broadcast.append(netMask[3][i])
            for i in range(sobra):
                ip_broadcast.append("1")  
            ip_broadcast = st.formatar(ip_broadcast)
            return ip_broadcast