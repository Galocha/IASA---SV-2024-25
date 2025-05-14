class No:
    """
    Classe que representa um nó na árvore de procura 
    Foi implementada seguindo o diagrama da página 6 do P3-iasa-proj
    e utilizando as informações acerca de nós presente no pdf 10-pee-1

    Um nó é uma estrutura fundamental em algoritmos de procura que:
    1. Representa um estado (configuração específica do problema)
    2. Armazena informações sobre como esse estado foi alcançado:
       - Operador aplicado
       - Nó antecessor (estado anterior)
    3. Mantém métricas de procura:
       - Profundidade na árvore
       - Custo acumulado do caminho
    """
    #os seguintes atributos foram criados como estáticos, pois são comuns a todos os objetos da classe "No"
    nos_criados = 0
    nos_eliminados = 0
    max_nos_em_mem = 0
    nos_repetidos = 0
    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        """
        Construtor do nó de procura
        
        Parâmetros:
        - estado: Representação da configuração atual do problema
        - operador: Ação que gerou este estado (None para nó raiz)
        - antecessor: Nó pai na árvore de procura (None para nó raiz)
        - custo: Custo acumulado do caminho desde a raiz até este nó
        
        A árvore de procura é constituída por nós que mantêm:
        - Estado: Situação concreta do problema
        - Operador: Ação que levou a este estado
        - Antecessor: Ligação ao nó pai
        - Profundidade: Nível na árvore (distância da raiz)
        - Custo: Custo acumulado do percurso
        """
        self.__estado= estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        self.__prioridade = None #o construtor não tem prioridade como parâmetro, daí ser None

        if antecessor!= None:
            self.__profundidade = antecessor.__profundidade + 1
        else:
            self.__profundidade = 0
            No.nos_criados = 0
            No.nos_eliminados = 0
        
        No.nos_criados += 1
        var_aux = No.nos_criados - No.nos_eliminados

        if (var_aux > No.max_nos_em_mem):
            No.max_nos_em_mem = var_aux
    
    @property
    def profundidade(self):
        """
        Profundidade do nó na árvore de procura
        
        Retorno:
        - int: Nível do nó na árvore (0 para raiz)
        
        A profundidade é usada para:
        - Controlar limites em procura limitada
        - Implementar estratégias de procura
        """
        return self.__profundidade
    
    @property
    def custo(self):
        """
        Custo acumulado do caminho desde o estado inicial até este nó
        
        Retorno:
        - float: Custo total do percurso
        
        O custo é calculado como:
        custo(pai) + custo(operador)
        Essencial para algoritmos de custo uniforme
        """
        return self.__custo
    
    @property
    def estado(self):
        """
        Estado (configuração) do problema associado a este nó
        
        Retorno:
        - Estado: Representação da situação atual
        
        O estado é uma configuração válida do problema
        que pode ser gerada por aplicação de operadores
        """
        return self.__estado
    
    @property
    def operador(self):
        """
        Operador que foi aplicado para gerar este estado
        
        Retorno:
        - Operador: Ação que transformou o estado antecessor
        - None: Para o nó raiz

        O operador representa uma transição válida entre estados
        no espaço de estados do problema
        """
        return self.__operador
    
    @property
    def antecessor(self):
        """
        Nó que gerou este nó na árvore de procura
        
        Retorno:
        - No: Nó pai na árvore
        - None: Para o nó raiz
        
        Permite reconstruir o caminho solução retrocedendo
        até ao estado inicial
        """
        return self.__antecessor
    
    """
    A property e o setter seguintes, foram necessários ser implementados devido à classe FronteiraPrioridade
    """
    @property
    def prioridade(self):
        return self.__prioridade
    
    @prioridade.setter
    def prioridade(self, valor):
        self.__prioridade = valor

    """
    Função necessária para o avaliador poder comparar nós
    """
    def __lt__(self, outro_no):
        return self.prioridade < outro_no.prioridade
    
    def __del__(self):
        No.nos_eliminados += 1