from ecr.resposta import Resposta
from sae.agente.accao import Accao

"""
Esta classe representa a resposta do agente ao mover.
Esta especializa também da classe Resposta, que pertence à package ecr.
"""
class RespostaMover(Resposta):
    def __init__(self, direccao):
        """
        Inicializa a resposta de mover do agente em uma direção específica

        Parâmetros:
        direccao (Direccao): Direção na qual o agente irá se mover (NORTE, SUL, ESTE, OESTE)

        Funcionamento:
        - A classe base `Resposta` é especializada para incluir uma ação de movimento (`Accao`) com passo fixo
        - A intensidade do passo é definida como `1` para garantir que o movimento ocorra a cada ativação

        Fundamentos teóricos:
        - Slide 13 (P2-iasa-proj.pdf): Detalha como uma resposta reativa é ativada em resposta a estímulos detectados
        """
        super().__init__(Accao(direccao, 1))
