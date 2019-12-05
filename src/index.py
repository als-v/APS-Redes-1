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

    # lista do ipAddr binario
    ipAddr_Blist = []
    ipAddr_Blist = st.binario(ipAddr)
    print("IP binario: ", ipAddr_Blist)

    # lista do netMask decimal
    netMask_Dlist = []
    netMask_Dlist = st.decimal(netMask)
    print("Mascara decimal: ", netMask_Dlist)

    # lista do netMask binario
    netMask_Blist = []
    netMask_Blist = st.binario(netMask)
    print("Mascara binario: ", netMask_Blist)

    # ========== __________execucao__________ ==========
    # Verificar se IPs e máscaras são válidas:
    a = True
    b = False
    # ip valido
    ip_valido = fc.ip_validation(ipAddr_Dlist)
    letraAa = "ip_valido"
    arquivo.write("    ")
    json.dump(letraAa, arquivo)
    arquivo.write(": ")
    if (ip_valido == True):
        json.dump(a, arquivo)
        print("Ip valido: ", a)

    else:
        json.dump(b, arquivo)
        print("Ip valido: ", b)

    arquivo.write(",\n")

    # mascara valida
    mask_valida = fc.mask_validation(
        netMask_Dlist, fc.classe_ip(ipAddr_Dlist), netMask_Blist)
    letraAb = "mascara_valida"
    arquivo.write("    ")
    json.dump(letraAb, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        json.dump(a, arquivo)
        print("Mascara valida: ", a)

    elif (mask_valida == False):
        json.dump(b, arquivo)
        print("Mascara valida: ", b)

    arquivo.write(",\n")

    # Quantidade de bits da rede (netID) e quantidade de bits de host (hostID), da máscara:
    # netId
    classe = fc.classe_ip(ipAddr_Dlist)
    netId = fc.netid_hostid(classe, netMask_Blist, 0)
    letraBa = "net_id"
    arquivo.write("    ")
    json.dump(letraBa, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        json.dump(netId, arquivo)
        print("Net ID: ", netId)

    else:
        json.dump("Erro, mascara invalida", arquivo)
        print("Net ID:  Erro, mascara invalida")

    arquivo.write(",\n")

    # hostId
    hostId = fc.netid_hostid(classe, netMask_Blist, 1)
    letraBb = "host_id"
    arquivo.write("    ")
    json.dump(letraBb, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        json.dump(hostId, arquivo)
        print("Host ID: ", hostId)

    else:
        json.dump("Erro, mascara invalida", arquivo)
        print("Host ID:  Erro, mascara invalida")

    arquivo.write(",\n")

    # Classe do IP:
    classeIp = classe
    letraC = "classe_ip"
    arquivo.write("    ")
    json.dump(letraC, arquivo)
    arquivo.write(": ")
    json.dump(classeIp, arquivo)
    print("Classe IP: ", classeIp)

    arquivo.write(",\n")

    # IP da rede:
    letraD = "ip_da_rede"
    arquivo.write("    ")
    json.dump(letraD, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        ip_rede = []
        ip_rede = fc.ip_redebroadcast(netMask_Blist, ipAddr_Blist, 0)
        p1 = ip_rede[0]
        p2 = ip_rede[1]
        p3 = ip_rede[2]
        p4 = ip_rede[3]
        p0 = p1 + "." + p2 + "." + p3 + "." + p4
        print("IP da rede binario: ", p0)
        ip_rede2 = st.ultimo(p0, 0)
        p0 = st.ultimo(p0, 3)
        json.dump(p0, arquivo)
        print("IP da rede decimal: ", p0)
    else:
        err = "Mascara da rede invalida"
        json.dump(err, arquivo)
        print("IP da rede: ", err)

    arquivo.write(",\n")

    # IP de broadcast:
    letraE = "ip_broadcast"
    arquivo.write("    ")
    json.dump(letraE, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        ip_broadcast = []
        ip_broadcast = fc.ip_redebroadcast(netMask_Blist, ipAddr_Blist, 1)
        p1 = ip_broadcast[0]
        p2 = ip_broadcast[1]
        p3 = ip_broadcast[2]
        p4 = ip_broadcast[3]
        p0 = p1 + "." + p2 + "." + p3 + "." + p4
        print("IP de broadcast binario: ", p0)
        ip_broadcast2 = st.ultimo(p0, 1)
        p0 = st.ultimo(p0, 3)
        json.dump(p0, arquivo)
        print("Ip de broadcast decimal: ", p0)

    else:
        err = "Mascara de rede invalida"
        json.dump(err, arquivo)
        print("IP de boradcast: ", err)

    arquivo.write(",\n")

    # Quantidade de hosts na referida rede:
    letraF = "quantidade_de_hosts"
    arquivo.write("    ")
    json.dump(letraF, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        quantidade = fc.quantidadehosts(netMask_Blist)
        json.dump(quantidade, arquivo)
        print("Quantidade de hosts referida na rede: ", quantidade)

    else:
        err = "Erro, a mascara e invalida"
        json.dump(err, arquivo)
        print("Quantidade de hosts referida na rede: ", err)

    arquivo.write(",\n")

    # Faixa de máquinas válidas - que podem ser utilizadas pelos hosts
    letraG = "ip_valido_inicial"
    letraGa = "ip_valido_final"
    arquivo.write("    ")
    json.dump(letraG, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        json.dump(ip_rede2, arquivo)
        arquivo.write(",\n")
        arquivo.write("    ")
        json.dump(letraGa, arquivo)
        arquivo.write(": ")
        json.dump(ip_broadcast2, arquivo)
        quantidade = ip_rede2 + " - " + ip_broadcast2
        print(
            "Faixa de maquinas validas que podem ser utilizadas pelos hosts: ", quantidade)

    else:
        err = "Erro, a mascara e invalida"
        json.dump(err, arquivo)
        print("Faixa de maquinas validas que podem ser utilizadas pelos hosts: ", err)

    arquivo.write(",\n")

    # Se o IP é em questão é reservado (privado, loopback, etc)
    letraH = "ipStatus"
    arquivo.write("    ")
    json.dump(letraH, arquivo)
    arquivo.write(": ")
    if ((ip_valido != False) and (ip_valido != True)):
        json.dump(ip_valido, arquivo)
        print("Status do IP: ", ip_valido)

    else:
        err = "O ip e enderecavel"
        json.dump(err, arquivo)
        print("Status do IP: ", err)

    arquivo.write("\n}")
