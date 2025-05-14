from abc import ABC, abstractmethod

class ModeloPlan(ABC):

    @abstractmethod
    def obter_estado(self):
        pass

    @abstractmethod
    def obter_estados(self):
        pass

    @abstractmethod
    def obter_operadores(self):
        pass