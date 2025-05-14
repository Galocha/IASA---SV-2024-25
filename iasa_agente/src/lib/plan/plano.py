from abc import ABC, abstractmethod

class Plano(ABC):

    @abstractmethod
    def obter_accao(self, estado):
        pass

    @abstractmethod
    def mostrar(self, vista):
        pass