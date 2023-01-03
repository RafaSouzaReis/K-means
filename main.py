from dado import Dado
from kMeans import KMeans
from visualizacao import Visualizacao
if __name__ == '__main__':
    conjunto_dados = []
    with open('.//r15.csv') as arquivo:
        for linha in arquivo.readlines():
            atributos = linha.rstrip().split(',')
            atributos = list(map(float, atributos))
            dado_arquivo = Dado(atributos)
            conjunto_dados.append(dado_arquivo)
    arquivo.close()
    k = int(input('Digite o valor de k: '))
    k_means = KMeans(k, conjunto_dados)
    agrupamento = k_means.executar()
    Visualizacao.plotar(agrupamento)

