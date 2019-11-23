# =========================================
# DIRETÓRIO: INDEX.PY
# Alunos: Alisson e Caio
# Este programa consiste na elaboracao da 
# APS 01 da desciplina de REDES 1!!
# Ultima ateracao: 23/11/2019, by Alisson
# =========================================

import sys
from src import index as ix

def main():
    with open((sys.argv[1]), "r") as f:
        arquivo = [line.strip().split(" ") for line in f]
    if arquivo == None:
        print("Erro ao abrir o arquivo!!\n")
    else:
        print("Arquivo aberto com sucesso!!\n")

        # pega o endereço IP do arquivo e salva em ipAddr
        ipAddr = ix.replace(arquivo, 1)

        # pega o endereço da Máscara e salva em netMasks
        netMask = ix.replace(arquivo, 2)

        # motor do codigo
        ix.execucao(ipAddr, netMask)


if __name__ == "__main__":
    main()
