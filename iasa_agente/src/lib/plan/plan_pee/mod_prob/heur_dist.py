import math

class HeurDist:
    """
    Classe que implementa uma heurística de distância para o problema de planeamento.
    Esta heurística calcula a distância entre o estado atual e o estado final.
    """

    def __init__(self, estado_final):
        """
        Inicializa a heurística com o estado final

        Parâmetros:
        - estado_final - estado alvo que se pretende alcançar
        """
        self.__estado_final = estado_final

    def h(self, estado):
        """
        Método que calcula a heurística de distância entre o estado atual e o estado final

        Parâmetros:
        - estado - estado atual do agente

        Retorno:
        - float - valor da heurística (distância) entre o estado atual e o estado final
        """
        dist = math.dist(estado.posicao, self.__estado_final.posicao)
        return dist