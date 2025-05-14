from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan
from sae.ambiente.direccao import Direccao
import math
from sae.ambiente.elemento import Elemento

class ModeloMundo(ModeloPlan):
    def __init__(self):
        """
        Implementa a representação interna do ambiente (modelo do mundo) para um agente deliberativo
        
        Atributos:
        - __estado_agente: representa o estado atual do agente, contendo a sua posição
        - __estados: lista de todos os estados válidos no ambiente
        - __elementos: map de posições (x,y) para os elementos do ambiente
        - __operadores: lista de operadores de movimento disponíveis (um para cada direção)
        - __alterado: flag que indica se o modelo foi alterado desde a última atualização

        Funcionalidades:
        - Mantém um estado atualizado do ambiente
        - Fornece informações sobre estados, elementos e operadores disponíveis
        - Calcula distâncias entre estados
        - Atualiza o modelo com novas perceções
        
        Fundamentação teóricas:
        - 13-arq-delib.pdf, página 8: o modelo do mundo é a representação
        interna do ambiente
        - P4-iasa-proj.pdf, página 3: esta classe, no que toca a código estrutural,
        foi implementado a partir do diagrama
        - O código comportamental foi implementado a partir da explicação do docente
        """
        self.__estado_agente = None
        self.__estados = []
        self.__elementos = {}
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        #self - está a passar a própria instância do modelo de mundo, ou seja, os operadores
        #que estão a ser construídos são do próprio modelo
        self.__alterado = False
    
    def obter_estado(self):
        """
        Retorna o estado atual do agente no modelo do mundo
        """
        return self.__estado_agente
    
    def obter_estados(self):
        """
        Retorna a lista de estados válidos do ambiente
        """
        return self.__estados

    def obter_operadores(self):
        """
        Retorna os operadores de ação disponíveis no modelo atual
        """
        return self.__operadores

    def obter_elemento(self, estado): #estado:Estado
        """
        Obtém o elemento do ambiente numa posição específica
        
        Parâmetros:
        - estado - estado que contém a posição (x,y) a verificar
            
        Retorno:
        - Elemento - o tipo de elemento naquela posição (Elemento.ALVO, Elemento.OBSTACULO, etc.)
        """
        return self.__elementos.get(estado.posicao)

    #os métodos anteriores não são propriedades, pois estão
    #presentes em interfaces
    #os mesmos foram implementados com ajuda do docente

    #os próximos métodos foram também implementados com ajuda do docente
    def distancia(self, estado):
        """
        Calcula a distância euclidiana entre o estado atual do agente e outro estado
        
        Parâmetros:
        - estado - estado alvo para cálculo da distância
            
        Retorno:
        - float - distância euclidiana entre as posições dos dois estados
        """
        return math.dist(estado.posicao, self.__estado_agente.posicao)

    def actualizar(self, percepcao):
        """
        Atualiza o modelo do mundo com base nas novas informações 
        percebidas do ambiente (perceções)
        
        Parâmetros:
        - percepcao (Percepcao) - informação sensorial do agente
                
        Funcionamento:
        1. Atualiza a posição do agente (cria novo EstadoAgente)
        2. Compara os elementos percebidos com os atuais para detetar mudanças
        3. Se houve mudanças:
            - Atualiza o map de elementos
            - Reconstrói a lista de estados válidos
            - Marca o modelo como alterado
        """
        self.__estado_agente = EstadoAgente(percepcao.posicao)
        self.__alterado = self.__elementos != percepcao.elementos
        if self.__alterado:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao)
                              for posicao in percepcao.posicoes]

    def mostrar(self, vista):
        """
        Mostra o estado atual do modelo numa vista
        
        Parâmetros:
        - vista - componente de visualização
            
        Funcionamento:
        1. Mostra elementos (alvos e obstáculos) nas posições
        2. Marca a posição atual do agente na vista
        """
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado_agente.posicao)

    @property
    def elementos(self):
        """
        Retorna os elementos do modelo do mundo
                
        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 3: elementos é um atributo do tipo
        map e é read-only, daí ter-se criado esta property
        """
        return self.__elementos
    
    def __contains__(self, estado): #implementação do operador in
        #retorna True or False, caso o estado passado como parâmetro
        #esteja contido na lista de estados
        return estado in self.__estados

    @property
    def alterado(self):
        return self.__alterado