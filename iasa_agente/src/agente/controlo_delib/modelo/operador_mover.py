import math
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from mod.operador import Operador
from sae.agente.accao import Accao

class OperadorMover(Operador):
    """
    Implementa um operador de movimento para agentes em ambientes discretos 2D (espaços cartesianos),
    especializando a interface Operador
    Representa uma ação de deslocamento numa direção específica do ambiente

    Fundamentação teórica:
    - Segundo a classe Operador, um operador representa uma ação que gera
    uma transição de estado. Neste caso, esta classe representa
    a transição de uma posição do agente para outra, ou seja, representa
    um movimento do agente
    - P4-iasa-proj.pdf, página 3: o UML mostra a associação direta entre OperadorMover
    e ModeloMundo, e ainda que OperadorMover realiza o contrato da interface Operador
    - P4-iasa-proj.pdf, página 5: a simulação do movimento é feita por translação
    geométrica
    - Os métodos foram implementados com oritentação do professor
    """
    def __init__(self, modelo_mundo, direccao):
        """
        Inicializa um novo operador de movimento

        Parâmetros:
        - modelo_mundo - referência ao modelo do ambiente usado para validar movimentos
        - direccao - enumeração indicando a direção do movimento

        Atributos:
        - __modelo_mundo - modelo para verificar estados válidos
        - __direccao - direção do movimento
        - __ang - ângulo correspondente à direção
        - __accao - ação concreta associada ao operador
        """
        self.__modelo_mundo = modelo_mundo
        self.__direccao = direccao
        self.__ang = self.__direccao.value
        self.__accao = Accao(self.__direccao)
    
    def aplicar(self, estado):
        """
        Método para aplicar o operador, gerando o estado sucessor
        """
        nova_posicao = self.__translacao(estado.posicao, self.__accao.passo, self.__ang)
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo:
            return novo_estado

    def custo(self, estado, estado_suc):
        """
        Método para calcular custo de transição
        """
        return max(1, math.dist(estado.posicao, estado_suc.posicao))

    def __translacao(self, posicao, dist_desl, ang_desl):
        """
        Método para calcular a nova posição após uma translação

        Parâmetros:
        - posicao - posição atual (x, y)
        - dist_desl - distância a deslocar
        - ang_desl - ângulo de deslocamento

        Retorno:
        - nova_posicao - nova posição após a translação

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 5: o cálculo do movimento é feito
        por translação geométrica, onde:
            - dx = passo * cos(angulo)
            - dy = -passo * sin(angulo)
        """
        x, y = posicao
        dx = round(dist_desl * math.cos(ang_desl))
        dy = -round(dist_desl * math.sin(ang_desl))
        nova_posicao = x + dx, y + dy
        return nova_posicao
        

    @property
    def ang(self):
        """
        Propriedade que retornará o ângulo de movimento em radianos
        """
        return self.__ang
    
    @property
    def accao(self):
        """
        Propriedade que retornará a ação concreta associada
        """
        return self.__accao