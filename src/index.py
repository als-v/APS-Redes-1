# ===========================================
# DIRETÓRIO: INDEX.PY
# Neste aquivo temos a funcao motor do 
# codigo, esta que executa o motor do codigo
# Ultima alteracao: 23/11/2019, by: Alisson
# ============================================

# importacoes
from src import start as st
from src import funct as fc
import json

# funcao auxiliar
def replace(endereco, valor):
    return st.replace(endereco, valor)

# motor do codigo
def execucao(ipAddr, netMask):
    # ========== __________declaracoes__________ ==========
    # arquivo final
    arquivo = open("saida.json", "w")
    arquivo.write("{\n")

    # lista do ipAddr decimal
    ipAddr_Dlist = []
    ipAddr_Dlist = st.decimal(ipAddr)
    # print(ipAddr_Dlist)

    # lista do netMask decimal
    netMask_Dlist = []
    netMask_Dlist = st.decimal(netMask)
    # print(netMask_Dlist)

    # lista do ipAddr binario
    ipAddr_Blist = []
    ipAddr_Blist = st.binario(ipAddr)
    # print(ipAddr_Blist)

    # lista do netMask binario
    netMask_Blist = []
    netMask_Blist = st.binario(netMask)
    # print(netMask_Blist)

    # ========== __________execucao__________ ==========
    # Verificar se IPs e máscaras são válidas:
    a = "True"
    b = "False"
    # ip valido
    ip_valido = fc.ip_validation(ipAddr_Dlist)
    letraAa = "ipValidate"
    arquivo.write("    ")
    json.dump(letraAa, arquivo)
    arquivo.write(": ")
    if (ip_valido == True):
        json.dump(a, arquivo)
    elif (ip_valido == False):
        json.dump(b, arquivo)
    arquivo.write(",\n")

    # mascara valida
    mask_valida = fc.mask_validation(netMask_Blist)
    letraAb = "maskValidate"
    arquivo.write("    ")
    json.dump(letraAb, arquivo)
    arquivo.write(": ")
    if (mask_valida == True):
        json.dump(a, arquivo)
    elif (mask_valida == False):
        json.dump(b, arquivo)
    arquivo.write(",\n")


    # Quantidade de bits da rede (netID) e quantidade de bits de host (hostID), da máscara:
    # netId
    classe = fc.classe_ip(ipAddr_Dlist)
    netId = []
    netId = fc.netid_hostid(classe, ipAddr_Blist, 0)
    letraBa = "netId"
    arquivo.write("    ")
    json.dump(letraBa, arquivo)
    arquivo.write(": ")
    if (classe == "A"):
        p1 = ""
        for i in netId:
            p1 = p1 + i
        json.dump(p1, arquivo)
    elif (classe == "B"):
        p2 = ""
        for i in netId[0]:
            p2 = p2 + i
        p2 = p2 + "."
        for i in netId[1]:
            p2 = p2 + i
        json.dump(p2, arquivo)
    elif (classe == "C"):
        p3 = ""
        for i in netId[0]:
            p3 = p3 + i
        for i in range(2):
            p3 = p3 + "."
            for j in netId[i + 1]:
                p3 = p3 + j
        json.dump(p3, arquivo)
    arquivo.write(",\n")
    # hostId
    hostId = []
    hostId = fc.netid_hostid(classe, ipAddr_Blist, 1)
    letraBb = "hostId"
    arquivo.write("    ")
    json.dump(letraBb, arquivo)
    arquivo.write(": ")
    if (classe == "A"):
        p1 = ""
        for i in hostId[0]:
            p1 = p1 + i
        for i in range(2):
            p1 = p1 + "."
            for j in hostId[i + 1]:
                p1 = p1 + j
        json.dump(p1, arquivo)
    elif (classe == "B"):
        p2 = ""
        for i in hostId[0]:
            p2 = p2 + i
        p2 = p2 + "."
        for i in hostId[1]:
            p2 = p2 + i
        json.dump(p2, arquivo)
    elif (classe == "C"):
        p3 = ""
        for i in hostId[0]:
            p3 = p3 + i
        json.dump(p3, arquivo)
    arquivo.write(",\n")    

    # Classe do IP:
    classeIp = classe
    letraC = "ipClass"
    arquivo.write("    ")
    json.dump(letraC, arquivo)
    arquivo.write(": ")
    json.dump(classeIp, arquivo)
    arquivo.write(",\n")

    # IP da rede:
    ip_rede = []
    ip_rede = fc.ip_redebroadcast(netMask_Blist, 0)
    p1 = ip_rede[0]
    p2 = ip_rede[1]
    p3 = ip_rede[2]
    p4 = ip_rede[3]
    letraD = "networkIP"
    arquivo.write("    ")
    json.dump(letraD, arquivo)
    arquivo.write(": ")
    p0 = p1 + "." + p2 + "." + p3 + "." + p4
    json.dump(p0, arquivo)     
    arquivo.write(",\n")

    # IP de broadcast:
    ip_broadcast = []
    ip_broadcast = fc.ip_redebroadcast(netMask_Blist, 1)
    p1 = ip_broadcast[0]
    p2 = ip_broadcast[1]
    p3 = ip_broadcast[2]
    p4 = ip_broadcast[3]
    letraE = "broadcastIP"
    arquivo.write("    ")
    json.dump(letraE, arquivo)
    arquivo.write(": ")
    p0 = p1 + "." + p2 + "." + p3 + "." + p4
    json.dump(p0, arquivo)

    # Quantidade de hosts na referida rede:

    # Faixa de máquinas válidas - que podem ser utilizadas pelos hosts

    # Se o IP é em questão é reservado (privado, loopback, etc):
    arquivo.write("\n}")