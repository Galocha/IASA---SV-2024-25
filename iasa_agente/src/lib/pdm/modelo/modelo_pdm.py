from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    """
    Classe abstrata que define a interface para um Modelo de Processo de Decisão de Markov (PDM)
    (representação do problema)
    
    Funcionamento:
    - Fornece os métodos essenciais para modelar um problema como um PDM
    - Define a estrutura necessária para o cálculo de utilidades e de políticas ótimas
    
    Fundamentação teórica:
    - 15-pds.pdf, página 36 - define os componentes essenciais de um PDM:
        - S: conjunto de estados possíveis
        - A(s): conjunto de ações possíveis num estado s
        - T(s, a, sn): função de transição de um estado s para um estado sn dado uma ação a
        - modelo de recompensa:
            - R(s, a, sn): recompensa geral
            - R(s, a): recompensa dependente do estado e da ação
            - R(s): recompensa dependente do estado
    - P4-iasa-proj.pdf, página 11: corresponde à interface ModeloPDM no diagrama de classes
    da package pdm, incluindo os métodos S(), A(), T(), R() e suc()

    Atributos implícitos:
    - Estados (S): representam configurações possíveis do ambiente (mundo)
    - Ações (A): operadores aplicáveis em cada estado
    - Transições (T): modelo dinâmico do ambiente (não determinista)
    - Recompensas (R): função que quantifica o desempenho local
    """

    @abstractmethod
    def S(self):
        """
        Obtém a lista de estados possíveis no PDM
        
        Retorno:
        - lista - conjunto de todos os estados possíveis no modelo
            
        Fundamentação teórica:
        - 15-pds.pdf, página 36: S representa o conjunto de estados do mundo
        - P4-iasa-proj.pdf, página 11: método S() da interface ModeloPDM
        """
        pass

    @abstractmethod
    def A(self, s):
        """
        Obtém as ações possíveis num determinado estado
        
        Parâmetros:
        - s (Estado): estado para o qual se quer obter as ações disponíveis
            
        Retorno:
        - lista - conjunto de ações possíveis no estado especificado
            
        Fundamentação teórica:
        - 15-pds.pdf, página 36: A() representa o conjunto de ações possíveis num estado s
        - P4-iasa-proj.pdf, página 11: método A() da interface ModeloPDM
        """
        pass

    @abstractmethod
    def T(self, s, a, sn):
        """
        Calcula a probabilidade de transição entre estados dada uma ação
        
        Parâmetros:
        - s (Estado): estado atual
        - a (Operador): ação a executar
        - sn (Estado): estado seguinte
            
        Retorno:
        - float - probabilidade de transição de s para sn através de a (T(s,a,sn))
            
        Fundamentação teórica:
        - 15-pds.pdf, página 8: T(s,a,s') representa a probabilidade de transição de s para sn através de a
        - P4-iasa-proj.pdf, página 11: método T() da interface ModeloPDM
        """
        pass

    @abstractmethod
    def R(self, s, a, sn):
        """
        Calcula a recompensa esperada por uma transição entre estados através de a
        
        Parâmetros:
        - s (Estado): estado atual
        - a (Operador): ação executada
        - sn (Estado): estado seguinte
            
        Retorno:
        - float - recompensa esperada pela transição (R(s,a,sn))
            
        Funcionamento:
        - Pode ser positivo (ganho) ou negativo (perda)
        - Reflete o benefício imediato da transição
            
        Fundamentação teórica:
        - 15-pds.pdf, página 8: R(s,a,s') representa a recompensa esperada
        - P4-iasa-proj.pdf, página 11: método R() da interface ModeloPDM
        """
        pass

    @abstractmethod
    def suc(self, s, a):
        """
        gera o estado sucessor que resulta de realizar a ação a no estado s
        """
        pass