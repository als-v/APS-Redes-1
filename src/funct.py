# funcao que verifica se a mascara da rede e valida


def mask_validation(endereco):
    for i in range(0, (len(endereco) - 1)):
        for j in range(i + 1, (len(endereco) - 1)):
            if(endereco[j] > endereco[i]):
                return False
    return True

# funcao que verifica se o ip da rede e valido


def ip_validation(endereco):
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
    #for i in range(4):
    #ipRede.append(ipAddr_Dlist[i] & netMask_Dlist[i])
    # return ipRede

    return True