from pee.mec_proc.fronteira import Fronteira
import heapq as hq #utilizada para estruturar dados de forma prioritária

class FronteiraPrioridade(Fronteira):
    """
    Implementa uma fronteira de prioridade para algoritmos de procura informada,
    onde os nós são ordenados dinamicamente conforme uma função de avaliação
    Utiliza a estrutura heap para eficiência nas operações de inserção/remoção

    Fundamentação teórica:
    - P3-iasa-proj.pdf, página 11 e 12: os diagramas de classes mostram FronteiraPrioridade
    como uma classe que precisa de um avaliador e que é usado em algoritmos de procura
    que utilizem o método Procura Melhor Primeiro. Este estende também de Fronteira
    - 12-pee-3.pdf, página 11 e 12: uma lista prioritária é necessária em métodos de
    Procura Informada, onde a procura é guiada, ou seja, o espaço de estados não é
    exaustivamente explorado
    """
    def __init__(self, avaliador):
        """
        Inicializa a fronteira com um avaliador de prioridades

        Parâmetros:
        - avaliador (Avaliador): Objeto que calcula a prioridade dos nós

        Funcionamento:
        1. Chama o construtor da superclasse Fronteira para inicializar a lista _nos
        2. Armazena o avaliador que será usado para calcular prioridades

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 11: Mostra a relação entre FronteiraPrioridade
          e os avaliadores no diagrama de arquitetura
        """
        super().__init__()
        self.__avaliador = avaliador

    def inserir(self, no):
        """
        Insere um nó na fronteira com prioridade calculada pelo avaliador

        Parâmetros:
        - no (No): Nó a ser inserido na fronteira.

        Funcionamento:
        1. Calcula a prioridade do nó usando self.__avaliador.prioridade(no).
        2. Atribui a prioridade ao nó (no.prioridade).
        3. Insere o nó no heap usando heapq.heappush para manter a ordem.

        Fundamentação teórica:
        - P3-iasa-proj, página 11: o diagrama mostra a necessidade de implementação
        deste método
        - 10-pee-1.pdf, página 28: o pseudocódigo, apesar de ser para o algoritmo
        de procura em largura, menciona a utilização deste método para inserir nós
        sucessores na fronteira, ou seja, expandir o(s) nó(s) anterior(es), e como 
        esta classe estende de Fronteira, este método teve de ser implementado
        """
        no.prioridade = self.__avaliador.prioridade(no) #alterar a prioridade do nó, consoante a avaliação do avaliador
        hq.heappush(self._nos, no)

    def remover(self):
        """
        Remove e retorna o nó com maior prioridade (menor valor numérico)

        Retorno:
        - No - Nó com maior prioridade na fronteira

        Funcionamento:
        1. Usa heapq.heappop para extrair eficientemente o nó mais prioritário
        2. Mantém a propriedade de heap após a remoção

        Fundamentação teórica:
        - 10-pee-1.pdf, página 28: tal como foi mencionado no método acima,
        o pseudocódigo deste slide não está diretamente a implementar este
        tipo de fronteira, mas menciona a utilização deste método para remover
        nós da fronteira
        - P3-iasa-proj.pdf, página 7: Mostra este método como parte da
        classe abstrata Fronteira
        """
        return hq.heappop(self._nos)