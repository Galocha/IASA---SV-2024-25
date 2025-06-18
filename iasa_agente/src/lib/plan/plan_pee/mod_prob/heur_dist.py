import math

class HeurDist:
    """
    Implementa uma heurística admissível baseada na distância euclidiana entre a posição atual
    e a posição objetivo, para uso em algoritmos de procura informada como A*

    A heurística estima o custo mínimo para alcançar o objetivo a partir de um dado estado,
    assumindo movimento direto sem obstáculos, o que garante admissibilidade (nunca superestima
    o custo real)

    Fundamentação teórica:
    - 14-plan-pee.pdf, página 5: necessidade de heurística, caso seja necessário,
    o que é o caso, pois está-se a trabalhar com Procura A*
    - P4-iasa-proj.pdf, página 9: PlaneadorPEE utiliza esta classe para
    calcular a heurística de distância entre o estado atual e o estado final
    - 12-pee-3.pdf, página 21: o cálculo da distância euclidiana é uma
    heurística admissível, pois assume movimentos não diagonais
    """

    def __init__(self, estado_final):
        """
        Inicializa a heurística com o estado objetivo de referência

        Parâmetros:
        - estado_final: estado que contém a posição objetivo
        
        Funcionamento:
        - Armazena o estado final para cálculo posterior de distâncias

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 9: mostra o construtor a receber estado_final
        """
        self.__estado_final = estado_final

    def h(self, estado):
        """
        Calcula a distância euclidiana entre a posição atual e a posição objetivo

        Parâmetros:
        - estado: estado atual a ser avaliado

        Retorno:
        - float: distância linear entre as posições, servindo como estimativa heurística

        Funcionamento:
        1. Aceder às coordenadas de posição do estado atual e do objetivo
        2. Calcular a distância euclidiana usando math.dist()
        3. Retornar o valor como estimativa de custo mínimo

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 9: método h() implementado para avaliação de estados
        - 12-pee-3.pdf, página 21 e 22: comparando a distância euclidiana com a distância
        de Manhattan, a primeira é admissível ao contrário da segunda, pois não são possíveis,
        neste caso, movimentos diagonais, por isso, calcula-se a distância euclidiana, que é da
        forma: 
            - sqrt((Xn - Xobj)^2 + (Yn - Yobj)^2), onde:
                - Xn, Yn: coordenadas do estado atual
                - Xobj, Yobj: coordenadas do estado objetivo
        """
        dist = math.dist(estado.posicao, self.__estado_final.posicao)
        return dist