from abc import ABC
from pee.mec_proc.no import No
from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade

class ProcuraMelhorPrim(ProcuraGrafo, ABC):
    """
    Classe abstrata que implementa o padrão de procura melhor-primeiro,
    utilizando uma fronteira com prioridade para explorar os nós mais promissores primeiro.
    Serve como base para algoritmos como A*, Procura de Custo Uniforme e Procura Sôfrega

    Fundamentação teórica:
    - P3-iasa-proj.pdf, página 14: diagrama de classes mostra
    ProcuraMelhorPrim como classe base para algoritmos que implementem
    procuras informadas
    - 11-pee-2.pdf, página 20: descreve o algoritmo genérico de melhor-primeiro
    """
    def __init__(self, avaliador):
        """
        Inicializa o mecanismo de procura com um avaliador específico

        Parâmetros:
        - avaliador (Avaliador) - Objeto que calcula prioridades para os nós

        Funcionamento:
        1. Armazena o avaliador para uso posterior
        2. Inicializa a superclasse ProcuraGrafo com uma FronteiraPrioridade
        configurada com o avaliador

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 12: o diagrama mostra a utilização de um
        avaliador por parte da FronteiraPrioridade e ProcuraMelhorPrim. Também
        é percetível que ProcuraMelhorPrim especializa de ProcuraGrafo
        - 12-pee-3.pdf, página 2: esta procura utiliza um avaliador de modo a
        perceber se o custo num nó n é menor, e se for, torna-se mais promissor a
        ser explorado
        """
        self._avaliador = avaliador
        super().__init__(FronteiraPrioridade(self._avaliador))
    
    def _manter(self, no):
        """
        Determina se um nó deve ser mantido na fronteira de acordo com a estratégia
        de melhor-primeiro, eliminando caminhos ineficientes para estados já visitados

        Parâmetros:
        - no (No) - Nó a ser avaliado

        Retorno:
        - bool - True se o nó deve ser mantido, False caso contrário

        Funcionamento:
        1. Mantém o nó se seu estado nunca foi explorado
        2. Se o estado já tivesse sido explorado, mantém-se apenas se o novo caminho
        tiver custo menor que o anterior (self._explorados[no.estado].custo)

        Fundamentação teórica:
        - 12-pee-3.pdf, página 26: para garantir otimismo durante a procura,
        em algoritmos como, por exemplo, ProcuraA* (que herda de ProcuraInformada, que por sua vez,
        especializa de ProcuraMelhorPrim), é necessário manter os nós anteriormente
        explorados para fazer comparações
        - P3-iasa-proj.pdf, página 8: descreve o método _manter como parte
        do contrato para procura em grafos
        """
        return no.estado not in self._explorados or \
               no.custo < self._explorados[no.estado].custo