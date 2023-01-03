from typing import List
from dado import Dado


class Grupo:
    def __init__(self, centroide: List[float]):
        self.__centroide__ = centroide
        self.__dados__: List[Dado] = []

    def get_centroide(self):
        return self.__centroide__

    def get_dados(self):
        return self.__dados__

    def adicionar_dado(self, novo_dado: Dado):
        self.__dados__.append(novo_dado)

    def __recalcular_centroide__(self):
        colunas: int = len(self.__centroide__)
        linhas: int = len(self.__dados__)
        novo_centroide = [0 for x in range(colunas)]
        for dado_atual in self.__dados__:
            atributos = dado_atual.get_atributos()
            for i in range(colunas):
                novo_centroide[i]+= atributos[i]/linhas
            #novo_centroide = [(atributo_x+atributo_y)/linhas for atributo_x, atributo_y in zip(atributos, novo_centroide)]
        return novo_centroide


    def centroide_alterado(self):
        novo_centroide = self.__recalcular_centroide__()
        if novo_centroide == self.__centroide__:
            return False
        else:
            self.__centroide__ = novo_centroide
            return True

    def zerar_grupo(self):
        self.__dados__.clear()

