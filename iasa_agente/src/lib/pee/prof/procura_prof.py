from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):
    """
    Classe que implementa o mecanismo de procura em profundidade (Depth-First Search)

    O mecanismo de procura em profundidade utiliza uma fronteira LIFO para explorar os nós mais recentes primeiro
    Esta abordagem é útil para explorar profundamente um ramo do espaço de estados antes de retroceder e explorar outros ramos

    A procura em profundidade ocupa pouca memória, mas não é ótima nem completa

    Fundamentação teórica:
    - 10-pee-1.pdf, páginas 12 e 13: é apresentado o algoritmo de procura em profundidade, com destaque para o uso de uma fronteira LIFO
    - P3-iasa-proj.pdf, página 7 e 8: o diagrama de classes associa a ProcuraProfundidade diretamente ao uso de FronteiraLIFO
    """
    def __init__(self):  
        super().__init__(FronteiraLIFO()) 