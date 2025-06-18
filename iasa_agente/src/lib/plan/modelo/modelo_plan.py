from abc import ABC, abstractmethod

class ModeloPlan(ABC):
    """
    Classe abstrata que define a interface para um modelo de planeamento
    O processo de planeamento exige um modelo que defina o essencial do problema a resolver

    Fundamentação teórica:
    - 14-plan-pee.pdf, página 2: um modelo de planeamento tem que definir:
        - o estado inicial
        - um conjunto de estados que sejam válidos
        - um conjunto de operadores definidos
    - P4-iasa-proj.pdf, página 7: a interface Planeador depende do ModeloPlan para
    o seu correto funcionamento
    - P4-iasa-proj.pdf, página 8: o ModeloMundo especializa desta interface
    """
    @abstractmethod
    def obter_estado(self):
        """
        Obtém o estado inicial do modelo de planeamento

        Retorno:
        - Estado: representação do estado inicial do problema

        Funcionamento:
        - Retorna uma representação simbólica do estado inicial
        - Estado deve conter toda a informação relevante para a tomada de decisão

        Fundamentação teórica:
        - 14-plan-pee.pdf, página 2: o estado inicial do problema é 
        uma componente essencial do modelo de planeamento
        - P4-iasa-proj.pdf, página 8: método obter_estado() na interface ModeloPlan
        """
        pass

    @abstractmethod
    def obter_estados(self):
        """
        Adquire todos os estados válidos do domínio de planeamento

        Retorno:
        - List[Estado]: lista de todos os estados possíveis no modelo

        Funcionamento:
        - Enumera os estados alcançáveis a partir do estado inicial
        - Essencial para algoritmos que necessitam do espaço de estados completo

        Fundamentação teórica:
        - 14-plan-pee.pdf, página 2: "Conjunto de estados válidos" como parte do modelo,
        que são necessários para processos de decisão de Markov
        - P4-iasa-proj.pdf, página 8: método obter_estados() na interface
        """
        pass

    @abstractmethod
    def obter_operadores(self):
        """
        Obtém os operadores disponíveis para transição entre estados

        Retorno:
        - List[Operador]: lista de operadores/ações aplicáveis

        Funcionamento:
        - Retorna as ações (deslocamentos) possíveis que o agente pode executar
        - Cada operador deve implementar uma maneira de aplicar a transição de estado

        Fundamentação teórica:
        - 14-plan-pee.pdf, página 2: "Conjunto de operadores definidos"
        - P4-iasa-proj.pdf, página 8: método obter_operadores() presente na arquitetura
        - 14-plan-pee.pdf, página 4: operadores são transições entre estados. No caso do
        projeto, são os deslocamentos do agente entre determinadas posições
        """
        pass