from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

class EvitarObst(Hierarquia):
    """
    Classe de comportamento hierárquico para evitar obstáculos no ambiente

    Este comportamento combina várias instâncias de `EvitarDir` correspondendo às
    direções definidas em `Direccao`, organizando-as em uma estrutura hierárquica
    A classe permite ao agente reagir de forma coordenada ao detectar obstáculos em múltiplas direções

    Fundamentos teóricos:
    - Arquitetura de Subsunção (Slide 11, "08-arq-react-3.pdf"): Integra diferentes níveis de reações, cada um com um papel específico no controlo do agente
    - Hierarquia de Comportamentos (Slide 8, "07-arq-react-2.pdf"): Organiza reações com base em prioridade e relevância, permitindo decisões dinâmicas
    - Evitar Obstáculos (Slides 12 e 13, "P2-iasa-proj.pdf"): Implementa estímulos e respostas para desviar de obstáculos
    - Coordenação de Direções (Slide 16, "07-arq-react-2.pdf"): Cada direção (NORTE, SUL, ESTE, OESTE) é tratada como um estímulo independente
    """
    def __init__(self):
        """
        Inicializa o comportamento EvitarObst

        Funcionamento:
        - Gera uma reação `EvitarDir` para cada direção definida em `Direccao`
        - Organiza as reações numa hierarquia utilizando a classe base `Hierarquia`,
          garantindo que o agente reaja adequadamente com base nos estímulos detectados

        Baseado em:
        - Slide 11 (08-arq-react-3.pdf): Arquitectura de subsunção
        - Slide 13 (P2-iasa-proj.pdf): Diagrama de estímulos e reações ao evitar obstáculos
        """
        super().__init__([EvitarDir(direccao) for direccao in Direccao])