from agente.controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar
from ecr.reaccao import Reaccao
from agente.controlo_react.reaccoes.evitar.estimulo_obst import EstimuloObst

class EvitarDir(Reaccao):
    """
    Classe de reação para evitar obstáculos numa direção específica

    Este comportamento reativo utiliza a deteção de obstáculos (`EstimuloObst`) e
    ativa uma resposta específica (`RespostaEvitar) quando um obstáculo é detectado
    na direção fornecida

    Fundamentos teóricos (P2-iasa-proj):
    - Modelo de Reação (Slide 3, "Reacção - Arquitectura"): As reações combinam estímulos e respostas para produzir ações direcionadas
    - Evitar Obstáculos (Slide 13): Este comportamento evita colisões de forma eficaz, adaptando-se às perceções do ambiente
    - Respostas a Estímulos (Slide 14): As respostas são ativadas com base na intensidade dos estímulos detectados
    """
    def __init__(self, direccao):
        """
        Inicializa a reação para evitar obstáculos numa direção específica

        Parâmetros:
        direccao (Direccao): Direção para a qual o obstáculo detectado deverá ser evitado

        Funcionamento:
        - EstimuloObst: Responsável por detectar a presença de obstáculos na direção especificada
        - RespostaEvitar: Gera a ação necessária para evitar o obstáculo
        """
        super().__init__(EstimuloObst(direccao), RespostaEvitar())