# ===========================================
# DIRETÓRIO: INDEX.PY
# Neste aquivo temos a funcao motor do 
# codigo, esta que executa o motor do codigo
# Ultima alteracao: 01/12/2019, by: Alisson
# ============================================

# importacoes
from src import start as st
from src import funct as fc
import json

# funcao auxiliar
def replace(endereco, valor):
    return st.replace(endereco, valor)

def execucao(ip, mask):
    flag = fc.teste(ip, mask)
    if (flag == True):
        execucaoAux(ip, mask)
    else:
        print("Erro, o ip e a mascara devem ser declarados corretamente no arquivo 'config.json'!!\nPor favor, verifique o arquivo e tente novamente.")
        arquivo = open("saida.json", "w")
        arquivo.write("{\n    ")
        err = "Arquivo nao formatado corretamente!!"
        erra = "FATAL_ERROR"
        json.dump(erra, arquivo)
        arquivo.write(": ")
        json.dump(err, arquivo)
        arquivo.write("\n}")

# motor do codigo
def execucaoAux(ipAddr, netMask):
    # ========== __________declaracoes__________ ==========
    # arquivo final
    arquivo = open("saida.json", "w")
    arquivo.write("{\n")

    # lista do ipAddr decimal
    ipAddr_Dlist = []
    ipAddr_Dlist = st.decimal(ipAddr)
    print("IP decimal: ", ipAddr_Dlist)
    print("\n")

    # lista do netMask decimal
    netMask_Dlist = []
    netMask_Dlist = st.decimal(netMask)
    print("Mascara decimal: ", netMask_Dlist)
    print("\n")

    # lista do ipAddr binario
    ipAddr_Blist = []
    ipAddr_Blist = st.binario(ipAddr)
    print("IP binario: ", ipAddr_Blist)
    print("\n")

    # lista do netMask binario
    netMask_Blist = []
    netMask_Blist = st.binario(netMask)
    print("Mascara binario: ",netMask_Blist)
    print("\n")

    # ========== __________execucao__________ ==========
    # Verificar se IPs e máscaras são válidas:
    a = True
    b = False
    # ip valido
    ip_valido = fc.ip_validation(ipAddr_Dlist)
    letraAa = "ipValidate"
    arquivo.write("    ")
    json.dump(letraAa, arquivo)
    arquivo.write(": ")
    if (ip_valido == True):
        json.dump(a, arquivo)
        print("Ip valido: ", a)
        print("\n")
    else:
        json.dump(b, arquivo)
        print("Ip valido: ", b)
        print("\n")
    arquivo.write(",\n")

    # mascara valida
    mask_valida = fc.mask_validation(netMask_Dlist, fc.classe_ip(ipAddr_Dlist))
    letraAb = "maskValidate"
    arquivo.write("    ")
    json.dump(letraAb, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        json.dump(a, arquivo)
        print("Mascara valida: ", a)
        print("\n")
    elif (mask_valida == False):
        json.dump(b, arquivo)
        print("Mascara valida: ", b)
        print("\n")
    arquivo.write(",\n")


    # Quantidade de bits da rede (netID) e quantidade de bits de host (hostID), da máscara:
    # netId
    classe = fc.classe_ip(ipAddr_Dlist)
    netId = fc.netid_hostid(classe, netMask_Blist, 0)
    letraBa = "netId"
    arquivo.write("    ")
    json.dump(letraBa, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        json.dump(netId, arquivo)
        print("Net ID: ", netId)
        print("\n")
    else:
        json.dump("Erro, mascara invalida", arquivo)
        print("Net ID:  Erro, mascara invalida")
        print("\n")
    arquivo.write(",\n")

    # hostId
    hostId = fc.netid_hostid(classe, netMask_Blist, 1)
    letraBb = "hostId"
    arquivo.write("    ")
    json.dump(letraBb, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        json.dump(hostId, arquivo)
        print("Host ID: ", hostId)
        print("\n")
    else:
        json.dump("Erro, mascara invalida", arquivo)
        print("Host ID:  Erro, mascara invalida")
        print("\n")
    arquivo.write(",\n")    

    # Classe do IP:
    classeIp = classe
    letraC = "ipClass"
    arquivo.write("    ")
    json.dump(letraC, arquivo)
    arquivo.write(": ")
    json.dump(classeIp, arquivo)
    print("Classe IP: ", classeIp)
    print("\n")
    arquivo.write(",\n")

    # IP da rede:
    letraD = "networkIP"
    arquivo.write("    ")
    json.dump(letraD, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        ip_rede = []
        ip_rede = fc.ip_redebroadcast(netMask_Blist, 0)
        p1 = ip_rede[0]
        p2 = ip_rede[1]
        p3 = ip_rede[2]
        p4 = ip_rede[3]
        p0 = p1 + "." + p2 + "." + p3 + "." + p4
        json.dump(p0, arquivo)
        print("IP da rede: ", p0)     
        print("\n")
    else:
        err = "Mascara da rede invalida"
        json.dump(err, arquivo)
        print("IP da rede: ", err)
        print("\n")
    arquivo.write(",\n")

    # IP de broadcast:
    letraE = "broadcastIP"
    arquivo.write("    ")
    json.dump(letraE, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        ip_broadcast = []
        ip_broadcast = fc.ip_redebroadcast(netMask_Blist, 1)
        p1 = ip_broadcast[0]
        p2 = ip_broadcast[1]
        p3 = ip_broadcast[2]
        p4 = ip_broadcast[3]
        p0 = p1 + "." + p2 + "." + p3 + "." + p4
        json.dump(p0, arquivo)
        print("IP de broadcast: ", p0)
        print("\n")
        arquivo.write(",\n")
    else:
        err = "Mascara de rede invalida"
        json.dump(err, arquivo)
        print("IP de boradcast: ", err)
        print("\n")
        arquivo.write(",\n")

    # Quantidade de hosts na referida rede:
    letraF = "qtdHosts"
    arquivo.write("    ")
    json.dump(letraF, arquivo)
    arquivo.write(": ")    
    if (mask_valida == True):
        quantidade = fc.quantidadehosts(ip_rede)
        json.dump(quantidade, arquivo)
        print("Quantidade de hosts referida na rede: ", quantidade)
        print("\n")
    else:
        err = "Erro, a mascara e invalida"
        json.dump(err, arquivo)
        print("Quantidade de hosts referida na rede: ", err)
        print("\n")
    arquivo.write(",\n")

    # Faixa de máquinas válidas - que podem ser utilizadas pelos hosts
    letraG = "qtdValidHosts"
    arquivo.write("    ")
    json.dump(letraG, arquivo)
    arquivo.write(": ")    
    if (mask_valida == True):
        quantidade = fc.quantidadehosts(ip_rede) - 2
        if (quantidade < 0):
            json.dump(0, arquivo)
            print("Faixa de maquinas validas que podem ser utilizadas pelos hosts:  0")
        else:
            json.dump(quantidade, arquivo)
            print("Faixa de maquinas validas que podem ser utilizadas pelos hosts: ", quantidade)
        print("\n")
    else:
        err = "Erro, a mascara e invalida"
        json.dump(err, arquivo)
        print("Faixa de maquinas validas que podem ser utilizadas pelos hosts: ", err)
        print("\n")
    arquivo.write(",\n")

    # Se o IP é em questão é reservado (privado, loopback, etc)
    letraH = "ipStatus"
    arquivo.write("    ")
    json.dump(letraH, arquivo)
    arquivo.write(": ")
    if ((ip_valido != False) and (ip_valido != True)):
        json.dump(ip_valido, arquivo)
        print("Status do IP: ", ip_valido)
        print("\n")
    else:
        err = "O ip e enderecavel"
        json.dump(err, arquivo)
        print("Status do IP: ", err)
        print("\n")

    arquivo.write("\n}")