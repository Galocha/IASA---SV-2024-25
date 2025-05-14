from abc import ABC, abstractmethod #import necessário pois Operador() é uma interface

class Operador(ABC):
    """
    Interface abstrata que define o contrato para operadores de transição de estado em problemas de procura

    Fundamentação teórica:
    - P3-iasa-proj.pdf, página 3: o diagrama de classes mostra Operador como 
    interface com métodos abstratos aplicar() e custo()
    - 09-rac-aut.pdf, página 13: operadores representam ações que geram
    transformações de estado

    Esta é uma interface (todos métodos são abstratos) que deve ser implementada para cada problema concreto
    """
    @abstractmethod
    def aplicar(self, estado):
        """
        Aplica o operador a um estado, gerando um novo estado

        Parâmetros:
        - estado - estado atual ao qual o operador será aplicado

        Retorno:
        - Estado - novo estado resultante da aplicação do operador, 
        ou None se a aplicação não for possível

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 3: método aplicar definido na interface Operador
        - 10-pee-1.pdf, página 5: operadores geram estados sucessores quando aplicados
        - 09-rac-aut.pdf, página 10: exemplo de operador 'pegar(C)' que modifica o estado 
        dos blocos, que neste caso, no primeiro estado temos os blocos parados, e no seguinte,
        devido ao operador, foi pegado o bloco c
        """
        pass

    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Calcula o custo da transição de um estado para seu sucessor

        Parâmetros:
        - estado - estado atual
        - estado_suc - estado sucessor gerado pela aplicação do operador

        Retorno:
        - float - custo da transição entre os estados (deve ser ≥ 0)

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 3: método custo definido na interface Operador
        - Segundo os pdfs, existem muitas maneiras para calcular o custo, daí
        esta classe ser abstrata, permitindo as diferentes implementações nas
        classes concretas
        """
        pass