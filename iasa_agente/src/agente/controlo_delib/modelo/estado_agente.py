from mod.estado import Estado

class EstadoAgente(Estado):
    """
    Implementa a representação do estado de um agente no ambiente, especializando a classe base Estado
    
    Fundamentação teórica:
    - 13-arq-delib.pdf, página 4: a partir deste slide, percebe-se que o estado do agente
    no ambiente é a posição (x, y) do mesmo no ambiente | "Comportamentos de exploração: exploração
    com base em memória de posições anteriores"
    - P4-iasa-proj.pdf, página 3: o diagrama de classes indica que EstadoAgente está diretamente associado
    a ControloDelib e a ModeloMundo
    - P4-iasa-proj.pdf, página 4: este diagrama mostra que EstadoAgente herda de Estado e
    que está diretamente associado a Posicao, presente na package sae
    """
    def __init__(self, posicao):
        """
        Inicializa um novo estado do agente com uma posição específica
        
        Parâmetros:
        - posicao - par coordenado (x,y) representando a posição no ambiente
        """
        self.__posicao = posicao
    
    def id_valor(self):
        """
        Implementa o contrato da classe base Estado, gerando um identificador único para o estado
        
        Retorno:
        - int - valor hash calculado a partir da posição do agente
        """
        return hash(self.__posicao)
    
    @property
    def posicao(self):
        """
        Retorna a posição do estado atual do agente

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 4: o atributo posicao é read-only
        """
        return self.__posicao