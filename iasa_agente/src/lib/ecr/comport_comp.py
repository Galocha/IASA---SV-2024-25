from abc import ABC, abstractmethod
from .comportamento import Comportamento  # Importa a classe base Comportamento de um módulo relativo

# A classe ComportComp é uma classe abstrata que herda de Comportamento.
# Representa um comportamento composto, que agrega e coordena múltiplos comportamentos.
# Segundo o slide 5 do pdf P2-iasa-proj, comportamentos compostos são essenciais para
# modularizar e organizar comportamentos complexos em agentes reactivos.
# Pelo slide 13 do pdf 06-arq-react-1, comportamentos compostos agregam
# conjuntos de comportamentos e requerem um mecanismo de seleção de ação.
class ComportComp(Comportamento):
    def __init__(self, comportamentos):
        """
        Construtor da classe ComportComp
        
        Parâmetros:
        - comportamentos: Uma lista de comportamentos que serão agregados por este comportamento composto
        
        Este método inicializa o comportamento composto com uma lista de comportamentos,
        permitindo que eles sejam ativados e coordenados de forma modular.
        Conforme o slide 13 do pdf 06-arq-react-1, um comportamento composto agrega
        conjuntos de comportamentos para produzir resultados específicos.
        """
        self._comportamentos = comportamentos  # Armazena a lista de comportamentos agregados

    def activar(self, percepcao):
        """
        Método para ativar os comportamentos agregados e selecionar uma ação com base na percepção recebida
        
        Parâmetros:
        - percepcao: A percepção atual do ambiente, que será passada para cada comportamento
        
        Retorno:
        - Uma ação selecionada a partir das ações geradas pelos comportamentos agregados
        
        Este método implementa o ciclo percepção-ação. Ativa cada comportamento na lista, 
        coleta as ações geradas e seleciona uma delas para execução.
        Conforme o slide 13 do pdf 06-arq-react-1, um comportamento composto deve selecionar
        uma ação a partir das respostas dos comportamentos internos.
        """
        accoes = []  # Lista para armazenar as ações geradas pelos comportamentos
        for comp in self._comportamentos:  # Itera sobre cada comportamento agregado
            accao = comp.activar(percepcao)  # Ativa o comportamento com a percepção atual
            if accao:  # Se o comportamento gerar uma ação válida
                accoes.append(accao)  # Adiciona a ação à lista de ações
        if accoes:  # Se houver ações geradas
            return self.seleccionar_accao(accoes)  # Seleciona e retorna uma ação

    @abstractmethod
    def seleccionar_accao(self, accoes): #polimorfismo - é possível implementar este método de diferentes maneiras
        """
        Método abstrato para selecionar uma ação a partir de uma lista de ações.
        
        Parâmetros:
        - accoes: Uma lista de ações geradas pelos comportamentos agregados.
        
        Retorno:
        - Uma ação selecionada para execução.
        
        Este método define a lógica de seleção de ação.
        No slide 5 do pdf P2-iasa-proj, a partir do diagrama, facilmente se percebe que
        este método irá escolher uma ação proveniente da lista das ações geradas pelos
        comportamentos agregados.
        """
        raise NotImplementedError
    
#prioridade dinâmica - seleciona a ação com maior prioridade | multiplexer