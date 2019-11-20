# DIRETÓRIO: INDEX.PY
# ALUNOS: ALISSON E CAIO
# NESTE ARQUIVO TEMOS A FUNCAO MOTOR DO CODIGO

# importacoes
from . import start as st
from . import funct as fc
import json

# funcao auxiliar
def replace(endereco, numero):
    return st.replace(endereco, numero)

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

    # Classe do IP:
    classeIp = fc.classe_ip(ipAddr_Dlist)
    letraC = "ipClass"
    arquivo.write("    ")
    json.dump(letraC, arquivo)
    arquivo.write(": ")
    json.dump(classeIp, arquivo)
    arquivo.write(",\n")

    # IP da rede:
    ip_rede = []
    ip_rede = fc.ip_redebroadcast(ipAddr_Blist, netMask_Blist, 0)
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
    ip_broadcast = fc.ip_redebroadcast(ipAddr_Blist, netMask_Blist, 1)
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
    arquivo.write("\n}")
    # Quantidade de hosts na referida rede:

    # Faixa de máquinas válidas - que podem ser utilizadas pelos hosts

    # Se o IP é em questão é reservado (privado, loopback, etc):