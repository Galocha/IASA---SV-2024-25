from pee.mec_proc.fronteira import Fronteira #import necessário pois esta classe herda de Fronteira

class FronteiraLIFO(Fronteira): #Last In, First Out
    """
    Classe que implementa uma fronteira do tipo LIFO (Last In, First Out)

    Esta estrutura de dados é utilizada em mecanismos de procura onde os nós mais recentes inseridos na 
    fronteira são os primeiros a serem processados
    O comportamento desta classe é característico da procura em profundidade (Depth-First Search)

    Fundamentação teórica:
    - 10-pee-1.pdf, página 12: a estratégia de procura em profundidade utiliza a abordagem LIFO, 
    onde os nós mais recentes são removidos primeiro da fronteira
    - P3-iasa-proj.pdf, páginas 7 e 8: é descrito o diagrama de classes que inclui a implementação de fronteiras, 
    como FronteiraLIFO, para suportar estratégias específicas de controlo
    """
    def inserir(self, no):
        """
        Método que insere um nó na fronteira, seguindo a lógica LIFO

        Funcionamento:
        - O nó é inserido no início da lista de nós, garantindo que será processado antes dos restantes nós

        Parâmetros:
        - no: O nó a ser inserido na fronteira

        Fundamentação teórica:
        - 10-pee-1.pdf, página 13: descreve-se que inserir nós no início da fronteira é essencial para implementar o comportamento esperado de exploração
        - P3-iasa-proj.pdf, páginas 7 e 8: o método inserir é apresentado como parte crítica da interface da classe de fronteira
        """
        self._nos.insert(0, no)