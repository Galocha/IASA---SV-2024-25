from abc import ABC

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

class MecanismoProcura(ABC):
    """
    Classe abstrata que define o mecanismo genérico de procura em espaços de estados
    Implementa o algoritmo de procura conforme descrito no pdf 10-pee-1, nos slides 15 e 16
    
    De acordo com os slides 5 a 7 do pdf mencionado acima:
    - Um mecanismo de procura explora sistematicamente o espaço de estados
    - Utiliza uma fronteira para gerir nós a expandir
    - Opera sobre um modelo de problema (estado inicial, operadores, objetivo)
    """

    def __init__(self, fronteira):
        """
        Inicializa o mecanismo com uma estratégia de fronteira

        A fronteira determina a estratégia de procura, ou seja, a ordem de exploração dos nós
        """
        self._fronteira = fronteira

    def _iniciar_memoria(self):
        """
        Método para inicialização da fronteira
        
        Segundo os slides 26 e 27 do pdf 10-pee-1:
        - Alguns mecanismos necessitam de memória adicional para:
            - Evitar estados repetidos (procura em grafos)
            - Manter o histórico de nós explorados
        """
        self._fronteira.iniciar() # Iniciar a fronteira através do método iniciar

    def _memorizar(self, no):
        """
        Método para registo de nós que já foram explorados
        
        No slide 27 do pdf 10-pee-1:
        - Permite gerir nós "abertos" (fronteira) e "fechados" (já expandidos)
        - Essencial para evitar ciclos em problemas com ações reversíveis
        """
        self._fronteira.inserir(no) # Inserir nó a memorizar

    def procurar(self, problema):
        """
        Implementa o algoritmo geral de procura, presente em 10-pee-1.pdf, slide 15
        Explora o espaço de estados até encontrar uma solução
        
        Parâmetros:
        - problema: Objeto que implementa o modelo do problema
        
        Retorno:
        - Solucao: Sequência de nós do estado inicial ao objetivo
        - None: Se nenhuma solução for encontrada
        
        Funcionamento passo-a-passo do algoritmo:
        1. Inicialização da memória (iniciar a fronteira)
        2. Criação do nó inicial
        3. Memorizar o nó criado
        4. Enquanto existir nós na fronteira:
           a) Remove o primeiro nó da fronteira
           b) Verifica se o estado é objetivo
           c) Se for, retorna solução
           d) Senão, expande o nó e adiciona sucessores à fronteira
        5. Retorna None se fronteira esvaziar sem solução
        """
        self._iniciar_memoria() # Iniciar a memória
        no = No(problema.estado_inicial)
        self._memorizar(no) # Memorizar o no
        while not self._fronteira.vazia:
            no = self._fronteira.remover()
            if problema.objectivo(no.estado):
                return Solucao(no)
            for no_sucessor in self._expandir(problema, no):
                self._memorizar(no_sucessor)

    def _expandir(self, problema, no):
        """
        Gera nós sucessores aplicando operadores ao estado atual
        O método foi implementado a partir do algoritmo presente no slide
        16 do pdf 10-pee-1
        
        Parâmetros:
        - problema: Contém os operadores disponíveis
        - no: Nó atual a ser expandido
        
        Retorno:
        - Lista de nós sucessores válidos
        
        Funcionamento:
        1. Para cada operador do problema:
           a) Aplica operador ao estado sucessor
           b) Se gerar estado válido:
              - Calcula custo acumulado (custo do pai + custo da transição)
              - Cria um novo nó com estado, operador, antecessor e custo
        2. Retorna todos os sucessores gerados
        """
        sucessores = []
        estado = no.estado
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            if estado_suc != None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_sucessor = No(estado_suc, operador, no, custo)
                sucessores.append(no_sucessor)
        return sucessores
    
    @property
    def nos_processados(self):
        return No.nos_criados
    
    @property
    def nos_memoria(self):
        return No.max_nos_em_mem
    
    @property
    def nos_repetidos(self):
        return No.nos_repetidos