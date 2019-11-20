# DIRETÓRIO: FUNCT.PY
# ALUNOS: ALISSON E CAIO
# NESTE ARQUIVO TEMOS TODAS AS FUNCOES UTILIZADAS PARA O DESENVOLVIMENTO DA APS
# INCIALMENT: FUNCOES DE TRATAMENTO DE DADOS:

# funcao que auxilia na inicialização
from src import start as st
from src import funct as fc

# FUNCOES PARA AS IMPLEMENTACOES EM QUESTAO:

# motor do codigo

def replace(endereco, numero):
    return st.replace(endereco, numero)

def execucao(ipAddr, netMask):
    # variaveis para salvar no arquivo final
    arquivo = open("saida.txt", "w")

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

    arquivo.write("Classe do IP: ")
    # pega a classe do ip
    classeIp = fc.classe_ip(ipAddr_Dlist)
    print(classeIp)
    arquivo.write(classeIp + "\n")

    if ((fc.mask_validation(netMask_Blist) == True) & (fc.ip_validation(ipAddr_Blist) == True)):
        print("Ainda não concluído...")