from abc import ABC, abstractmethod

class Plano(ABC):
    """
    Classe abstrata que define a interface para um plano de ação 
    em sistemas de agentes deliberativos
    Um plano representa uma sequência de ações (ou ação) que leva o agente do 
    estado atual até um estado objetivo

    Fundamentação teórica:
    - 14-plan-pee.pdf, página 2: um plano é definido como uma sequência de ações 
    para alcançar objetivos
    - P4-iasa-proj.pdf, página 7: mostra que Planeador depende de Plano
    - 13-arq-delib.pdf, página 11: um plano é resultado do raciocínio sobre
    meios, ou seja, é resultado do planeamento do agente perante o ambiente
    """
    @abstractmethod
    def obter_accao(self, estado):
        """
        Obtém a próxima ação a ser executada dado um estado atual

        Parâmetros:
        - estado: estado atual do agente/ambiente

        Retorno:
        - Operador: a próxima ação a ser executada (None se o plano estiver completo)

        Funcionamento:
        1. Consulta a sequência de ações do plano
        2. Retorna a ação correspondente ao estado atual
        3. Pode implementar diferentes estratégias de execução

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 7: necessidade de um método para obter a próxima ação
        """
        pass

    @abstractmethod
    def mostrar(self, vista):
        """
        Apresenta visualmente o plano através de uma interface gráfica

        Parâmetros:
        - vista: componente de visualização que implementa métodos de renderização

        Funcionamento:
        1. Converte a representação interna do plano para formato visual
        2. Utiliza a vista fornecida para renderização

        Fundamentação teórica:
        - P4-iasa-proj.pdf, páginas 3 e 7: este método pertence a várias classes
        que sejam necessárias para mostrar informações importantes acerca do sistema,
        neste caso, servirá para mostrar o plano do agente para chegar ao(s) objetivo(s)
        """
        pass