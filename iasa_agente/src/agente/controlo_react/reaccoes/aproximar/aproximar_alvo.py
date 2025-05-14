from ecr.prioridade import Prioridade
from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from sae.ambiente.direccao import Direccao

class AproximarAlvo(Prioridade):
    """
    Classe de comportamento reativo para aproximar-se de um alvo

    Este comportamento utiliza um conjunto de reações direcionais (`AproximarDir`) baseadas nas direções do ambiente
    (`Direccao`). Cada instância de `AproximarDir` corresponde a uma direção específica (NORTE, SUL, ESTE, OESTE),
    permitindo ao agente reagir conforme o posicionamento do alvo detectado
    """
    def __init__(self):
        """
        Inicializa o comportamento AproximarAlvo com reações direcionais
        
        Atributos e funcionamento:
        - Utiliza a classe `Prioridade` para organizar e ativar as reações com base em níveis de importância
        - Cada direção disponível no ambiente é associada a uma instância de `AproximarDir`, criando um conjunto de
          reações que são geradas dinamicamente (utilizando compreensão de listas)

        Baseado nos conceitos teóricos:
            Esquemas Comportamentais Reativos: O uso de reações independentes permite modularidade e simplicidade no sistema reativo
            Comportamentos Compostos: A composição de múltiplas direções como subcomportamentos priorizados possibilita decisões rápidas e eficazes
            Aproximação Direcional: Cada direção é tratada como um estímulo específico, com resposta ajustada baseada no posicionamento relativo do alvo no ambiente

        Parâmetros:
        - AproximarDir: Define as respostas para as direções do alvo detectado.
        - Direccao: Enumeração que indica as direções disponíveis para o ambiente do agente.

        """
        super().__init__([AproximarDir(direccao) for direccao in Direccao]) #gerador de elementos