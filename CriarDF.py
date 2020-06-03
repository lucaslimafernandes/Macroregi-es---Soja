#APP Ler txt e separar por linhas
import pandas as pd
#from sys import argv

#param = argv[1:]
#df = pd.read_excel('base_in/0502.xlsx')
#nome_arquivo = param[0]

base_in = ['101 - RS.txt','102 - PR.txt','102 - RS.txt','102 - SC.txt',
            '103 - PR.txt','103 - RS.txt','103 - SC.txt','103 - SP.txt',
            '104 - SC.txt','201 - PR.txt','201 - SP.txt','202 - MS.txt',
            '202 - PR.txt','202 - SP.txt','203 - SP.txt','204 - MS.txt',
            '301 - GO.txt','301 - MS.txt','302 - GO.txt','302 - MG.txt',
            '302 - SP.txt','303 - GO.txt','303 - MG.txt','304 - GO.txt',
            '304 - MG.txt','401 - GO.txt','401 - MT.txt','402 - AC.txt',
            '402 - MT.txt','402 - RO.txt','403 - MT.txt','404 - GO.txt',
            '404 - TO.txt','405 - BA.txt','501 - MA.txt','501 - PA.txt',
            '501 - PI.txt','501 - TO.txt','502 - MA.txt','502 - PA.txt',
            '503 - RR.txt']
print(f'Len {len(base_in)}')
listaCI = []
listaUF = []
listaRE = []
for nome_arquivo in base_in:
    #print(c)
    caminho = 'base_in/Macroregiões/'+ nome_arquivo
    arquivo = open(caminho, 'r')

#print(arquivo.readlines())

    lista = arquivo.read().split(',')

    for i in range(0, len(lista)):
        listaCI.append(lista[i].lstrip())
        listaRE.append(nome_arquivo[:3])
        listaUF.append(nome_arquivo[6:8])


col = {'UF':listaUF, 'Região':listaRE, 'Municipios':listaCI}


df = pd.DataFrame(col)
#df.to_excel('base_out/Macroregiões/'+nome_arquivo[:8]+'.xlsx')
df.to_excel('base_out/Macroregiões/Macro.xlsx')

arquivo.close()
