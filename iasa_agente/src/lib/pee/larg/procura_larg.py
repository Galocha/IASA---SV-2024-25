from pee.larg.fronteira_fifo import FronteiraFIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

class ProcuraLargura(MecanismoProcura):
    """
    Classe que implementa a procura em largura (Breadth-First Search)

    Esta representa o mecanismo de procura em largura, baseado numa fronteira FIFO 
    (First In, First Out), que explora primeiro os nós mais antigos na estrutura de dados
    Esta estratégia é útil para garantir a exploração exaustiva de todos os nós de cada 
    nível antes de passar para níveis mais profundos no grafo de estados.

    Sendo este mecanismo exaustivo, significa que ocupa muita memória, 
    mesmo que a procura em largura seja ótima e completa

    Fundamentação teórica:
    - 10-pee-1.pdf, página 28: é apresentado o algoritmo de procura em largura e sua relação com a estrutura de fronteira FIFO
    - P3-iasa-proj.pdf, página 7: destaca-se a utilização de uma classe FronteiraFIFO para gerir os nós de maneira ordenada
    """
    def __init__(self):
        """
        Construtor da classe que inicializa o mecanismo de procura com uma fronteira FIFO

        Funcionamento:
        - Chama o construtor da classe base MecanismoProcura com a implementação de FronteiraFIFO
        - Prepara a classe para realizar a procura em largura, configurando a fronteira de exploração para operar no modo FIFO

        Fundamentação teórica:
        - 10-pee-1.pdf, página 28, é explicado como a fronteira FIFO é inicializada e utilizada para garantir o comportamento esperado da procura em largura
        - P3-iasa-proj.pdf, página 7: diagrama de classes, representa a associação da ProcuraLargura com a `FronteiraFIFO`
        """
        super().__init__(FronteiraFIFO())