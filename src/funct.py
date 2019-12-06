# =========================================
# DIRETÓRIO: FUNCT.PY
# Neste arquivo temos as funcoes para os 
# exercicios da aps em questao
# Ultima alteracao: 23/11/2019, by: Alisson
# ==========================================

from src import start as st

# funcao que testa o ip e a mascara
def teste(ip, mask):
    count_ponto = 0
    flag = True

    for i in ip:
        if (i == "."):
            count_ponto = count_ponto + 1
    
    if ((count_ponto < 3) or (count_ponto > 3)):
        return False
    
    count_ponto = 0

    for i in mask:
        if (i == "."):
            count_ponto = count_ponto + 1
    
    if ((count_ponto < 3) or (count_ponto > 3)):
        return False
    
    for i in ip:
        if (i != "0" and i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "."):
            flag = False

    for i in mask:
        if (i != "0" and i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "."):
            flag = False

    if (flag == False):
        return False

    for i in range(4):
        p0 = ip.split(".")[i]
        if ((int(p0) < 0) or (int(p0) > 255)):
            flag = False
    
    for i in range(4):
        p0 = mask.split(".")[i]
        if ((int(p0) < 0) or (int(p0) > 255)):
            flag = False
    
    if (flag == False):
        return False

    return True

# funcao que verifica se a mascara da rede e valida
def mask_validation(endereco, classe, endereco2):
    comecou_um = False
    comecou_zero = False
    nao_pode_ter_um = False
    if (classe == "A"):
        if (endereco[0] == 255):
            for i in endereco2[1:]:
                for j in i:
                    if ((j == "1") and (comecou_zero == False) and (comecou_um == False)):
                        comecou_um = True
                    elif ((j == "0") and (comecou_zero == False) and (comecou_um == False)):
                        nao_pode_ter_um = True
                        comecou_zero = True
                    elif ((j == "1") and (nao_pode_ter_um == True)):
                        return False
                    elif ((j == "0") and (comecou_um == True)):
                        nao_pode_ter_um = True
            return True
    elif (classe == "B"):
        if ((endereco[0] == 255) and (endereco[1] == 255)):
            for i in endereco2[2:]:
                for j in i:
                    if ((j == "1") and (comecou_zero == False) and (comecou_um == False)):
                        comecou_um = True
                    elif ((j == "0") and (comecou_zero == False) and (comecou_um == False)):
                        nao_pode_ter_um = True
                        comecou_zero = True
                    elif ((j == "1") and (nao_pode_ter_um == True)):
                        return False
                    elif ((j == "0") and (comecou_um == True)):
                        nao_pode_ter_um = True
            return True
    elif (classe == "C"):
        if ((endereco[0] == 255) and (endereco[1] == 255) and (endereco[2] == 255)):
            for i in endereco2[3:]:
                for j in i:
                    if ((j == "1") and (comecou_zero == False) and (comecou_um == False)):
                        comecou_um = True
                    elif ((j == "0") and (comecou_zero == False) and (comecou_um == False)):
                        nao_pode_ter_um = True
                        comecou_zero = True
                    elif ((j == "1") and (nao_pode_ter_um == True)):
                        return False
                    elif ((j == "0") and (comecou_um == True)):
                        nao_pode_ter_um = True
            return True
    return False

# funcao que verifica se o ip da rede e valido
def ip_validation(enderecoB):
    # verifico se o endereco comeca em 0
    if (int(enderecoB[0]) == 0):
        if ((int(enderecoB[1]) == 0) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
            return "Rede corrente"
        return False

    # verifico se o endereco e privado
    if ((int(enderecoB[0]) == 10) and (int(enderecoB[1]) == 0) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede privada"

    # verifico se o endereco e publico
    if ((int(enderecoB[0]) == 14) and (int(enderecoB[1]) == 0) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede publica"

    # verifico se o endereco e reservado
    if ((int(enderecoB[0]) == 39) and (int(enderecoB[1]) == 0) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede reservada"

    # verifico se o endereco e local
    if ((int(enderecoB[0]) == 127) and (int(enderecoB[1]) == 0) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede local (localhost)"

    # verifico se o endereco e reservado
    if ((int(enderecoB[0]) == 128) and (int(enderecoB[1]) == 0) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede reservada (IANA)"

    # verifico se o endereco e zeroconf
    if ((int(enderecoB[0]) == 169) and (int(enderecoB[1]) == 254) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Zeroconf"

    # verifico se o endereco e privado
    if ((int(enderecoB[0]) == 172) and (int(enderecoB[1]) == 16) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede privada"

    # verifico se o endereco e reservada
    if ((int(enderecoB[0]) == 191) and (int(enderecoB[1]) == 255) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede reservada (IANA)"

    # verifico se o endereco e de documentacao
    if ((int(enderecoB[0]) == 192) and (int(enderecoB[1]) == 0) and (int(enderecoB[2]) == 2) and (int(enderecoB[3]) == 0)):
        return "Documentacao"

    # verifico se o endereco e ipv6 para ipv4
    if ((int(enderecoB[0]) == 192) and (int(enderecoB[1]) == 88) and (int(enderecoB[2]) == 99) and (int(enderecoB[3]) == 0)):
        return "Rede ipv6 para ipv4"

    # verifico se o endereco e privado
    if ((int(enderecoB[0]) == 192) and (int(enderecoB[1]) == 168) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede privada"

    # verifico se o endereco e para testes de benchmark de redes
    if ((int(enderecoB[0]) == 198) and (int(enderecoB[1]) == 18) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede para testes de benchmark"

    # verifico se o endereco e reservado
    if ((int(enderecoB[0]) == 223) and (int(enderecoB[1]) == 255) and (int(enderecoB[2]) == 255) and (int(enderecoB[3]) == 0)):
        return "Rede privada"

    # verifico se o endereco e multicast
    if ((int(enderecoB[0]) == 224) and (int(enderecoB[1]) == 0) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede multicast (rede classe D)"

    # verifico se o endereco e classe E
    if ((int(enderecoB[0]) == 240) and (int(enderecoB[1]) == 0) and (int(enderecoB[2]) == 0) and (int(enderecoB[3]) == 0)):
        return "Rede reservada (classe E)"

    # verifico se o endereco e broadcast
    if ((int(enderecoB[0]) == 255) and (int(enderecoB[1]) == 255) and (int(enderecoB[2]) == 255) and (int(enderecoB[3]) == 255)):
        return "Rede Broadcast"

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
    errAA = "O endereco aparenta ser da classe A, porem e invalido!"
    B = False
    errB = False
    b = "B"
    errBB = "O endereco aparenta ser da classe B, porem e invalido!"
    C = False
    errC = False
    c = "C"
    errCC = "O endereco aparenta ser da classe C, porem e invalido!"
    err = "Endereco invalido"

    if ((endereco[0] <= 126) and (endereco[0] > 0)):
        A = True
        if(((endereco[1] == 0) and (endereco[2] == 0) and (endereco[3] == 0)) or ((endereco[1] == 255) and (endereco[2] == 255) and (endereco[3] == 255))):
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
def ip_redebroadcast(netMask, ipAddr, flag):
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

    if (count_um >= 0 and count_um < 9):                # caso esteja no na primeira parte do endereco
        if (flag == 0):                                 # caso eu queira o ip da rede
            ip_rede = []
            for i in range(count_um):                   # faco uma copia ate essa posicao
                ip_rede.append(ipAddr[0][i])
            for j in range(8 - count_um):               # seto tudo depois dela em 0
                ip_rede.append("0")
            for i in range(3):                          # como ainda tem 3 partes do endereco, seto em 0 para as demais partes
                for j in range(8):
                    ip_rede.append("0")
            ip_rede = st.formatar(ip_rede)              # formato o endereco
            return ip_rede                              # retorno o ip da rede
        elif (flag == 1):                               # caso eu queira o ip broadcast, sigo a mesma logica acima
            ip_broadcast = []
            for i in range(count_um):
                ip_broadcast.append(ipAddr[0][i])
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
                ip_rede.append(ipAddr[0][i])
            sobra = count_um - 8                    # tenho a sobra, que recebe a posicao que o ultimo um esta nessa segunda parte do endereco
            for i in range(sobra):                  # copio tudo ate chegar nele
                ip_rede.append(ipAddr[1][i])
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
                ip_broadcast.append(ipAddr[0][i])
            sobra = count_um - 8                   
            for i in range(sobra):                 
                ip_broadcast.append(ipAddr[1][i])
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
                ip_rede.append(ipAddr[0][i])
            for i in range(8):                      # faco uma copia da segunda parte
                ip_rede.append(ipAddr[1][i])
            sobra = count_um - 16                   # sobra recebe a posicao do ultimo 1
            for i in range(sobra):                  # copio tudo ate o ultimo 1
                ip_rede.append(ipAddr[2][i])
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
                ip_broadcast.append(ipAddr[0][i])
            for i in range(8):
                ip_broadcast.append(ipAddr[1][i])
            sobra = count_um - 16
            for i in range(sobra):
                ip_broadcast.append(ipAddr[2][i])
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
                ip_rede.append(ipAddr[0][i])
            for i in range(8):                          # faco uma copia da segunda parte do endereco   
                ip_rede.append(ipAddr[1][i])           
            for i in range(8):                          # faco uma copia da terceira parte do endereco
                ip_rede.append(ipAddr[2][i])
            sobra = 32 - count_um                       # variavel sobra recebe o valor que falta para chegar no 1
            for i in range(8 - sobra):                  # copio tudo ate ele
                ip_rede.append(ipAddr[3][i])
            for i in range(sobra):                      # logo apos, seto tudo que vem depois do ultimo 1 em 0
                ip_rede.append("0")
            ip_rede = st.formatar(ip_rede)              # formato o endereco
            return ip_rede                              # retorno o ip da rede
        elif (flag == 1):                               # caso eu queira o ip broadcast, sigo a mesma logica acima
            ip_broadcast = []
            for i in range(8):
                ip_broadcast.append(ipAddr[0][i])
            for i in range(8):
                ip_broadcast.append(ipAddr[1][i])
            for i in range(8):
                ip_broadcast.append(ipAddr[2][i])
            sobra = 32 - count_um
            for i in range(8 - sobra):
                ip_broadcast.append(ipAddr[3][i])
            for i in range(sobra):
                ip_broadcast.append("1")  
            ip_broadcast = st.formatar(ip_broadcast)
            return ip_broadcast

# funcao que calcula o netId e o hostId
def netid_hostid(classe, endereco, flag):
    err = "Erro, o endereco ip ou e invalido ou e reservado!!"
    if (classe != "A" and classe != "B" and classe != "C"):
        return err

    count_um = 0
    count_zero = 0
    for i in endereco:
        for j in i:
            if (j == "1"):
                count_um = count_um + 1
            elif (j == "0"):
                count_zero = count_zero + 1

    if (flag == 0):
        return count_um
    elif (flag == 1):
        return count_zero


# calcula a quantidade de hosts na rede
def quantidadehosts(endereco):
    count_zero = 0

    for i in endereco:
        for j in i:
            if (j == "0"):
                count_zero = count_zero + 1
    
    qtd_hosts = (2 ** count_zero)

    if (qtd_hosts == 1):
        return 0

    return qtd_hosts

# calcula a faixa de enderecos validos
def faixa(endereco, flag):
    p1 = int(endereco.split(".")[0])
    p2 = int(endereco.split(".")[1])
    p3 = int(endereco.split(".")[2])
    p4 = int(endereco.split(".")[3])

    p1 = st.converte(p1)
    p2 = st.converte(p2)
    p3 = st.converte(p3)
    p4 = st.converte(p4)

    if (flag == 0):
        p5 = str(p1) + "." + str(p2) + "." + str(p3) + "." + str(p4 + 1)
        return p5
    elif (flag == 1):
        p5 = str(p1) + "." + str(p2) + "." + str(p3) + "." + str(p4 - 1)
        return p5
    p5 = str(p1) + "." + str(p2) + "." + str(p3) + "." + str(p4)
    return p5    