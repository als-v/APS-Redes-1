from . import start as st

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


# calcula o Ip da rede
def calc_ipRede(ipAddr_Dlist, netMask_Dlist):
    ipRede = []
    i = 0 & 1
    print(i)
    #for i in range(4):
    #ipRede.append(ipAddr_Dlist[i] & netMask_Dlist[i])
    # return ipRede

    return True

def ip_redebroadcast(endereco1, endereco2, flag):
    ip_rede = []
    ip_broadcast = []
    ip_rede.append(endereco1[0:3])
    ip_broadcast.append(endereco1[0:3])
    count_pos = 0
    ultimo_um = 0
    count = 0

    # acho o ultimo numero 1
    for i in endereco2[3]:
        if (i == "1"):
            ultimo_um = count_pos
        count_pos = count_pos + 1

    # faco uma copia ate o ultimo 1
    for j in endereco1[3]:
        if (count != ultimo_um):
            ip_rede.append(j)
            ip_broadcast.append(j)
            count = count + 1

    # seto tudo que vem depois em 0
    for j in range(8 - ultimo_um):
        ip_rede.append("0")
    
    # seto tudo que vem depois em 1
    for j in range(8 - ultimo_um):
        ip_broadcast.append("1")

    # verifico a flag que vem por parametro, flag == 0: IP da rede || flag == 1: IP broadcast
    if(flag == 0):
        ip_rede = st.formatar(ip_rede)
        return ip_rede
    if(flag == 1):
        ip_broadcast = st.formatar(ip_broadcast)
        return ip_broadcast