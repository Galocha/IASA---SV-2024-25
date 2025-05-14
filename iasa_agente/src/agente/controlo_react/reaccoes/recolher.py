from agente.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from agente.controlo_react.reaccoes.explorar.explorar_com_mem import ExplorarComMem
from ecr.hierarquia import Hierarquia
from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.explorar.explorar import Explorar

class Recolher(Hierarquia):
    def __init__(self):
        """
        Comportamento composto hierárquico para recolha de alvos
        
        Organiza os subcomportamentos por prioridade, baseado no princípio de Arquitetura de Subsunção:
        - Cada comportamento é ativado conforme a sua prioridade e pertinência para o contexto do agente
        - Inspirado por níveis de competência, onde comportamentos simples são "sobrepostos" por comportamentos mais complexos
        
        Subcomportamentos:
        1. AproximarAlvo:
            - Prioridade máxima. Este comportamento é acionado quando o agente detecta um alvo
            - Baseia-se em estímulos específicos de alvos, utilizando resposta direcional para se aproximar
        
        2. EvitarObst:
            - Prioridade média. É ativado para garantir que o agente evite obstáculos
            - Baseado na detecção de estímulos de obstáculos e na geração de respostas evasivas
        
        3. ExplorarComMem:
            - Prioridade baixa. Utilizado para exploração do ambiente com um histórico de posições visitadas
            - Auxilia na procura de alvos de forma mais eficiente, minimizando áreas repetidas
        
        4. Explorar:
            - Prioridade mínima. Comportamento de fallback quando nenhum estímulo específico é detectado
            - Movimento aleatório no ambiente, proporcionando uma base exploratória genérica
        """
        super().__init__([AproximarAlvo(), EvitarObst(), ExplorarComMem(), Explorar(0.7)])