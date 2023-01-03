from typing import List
class Dado:
    def __init__(self, atributos: List[float]):
        self.__atributos__ = atributos

    def get_atributos(self):
        return self.__atributos__