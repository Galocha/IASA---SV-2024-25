from abc import ABC, abstractmethod #import necessário, pois a classe é abstrata

class Problema(ABC):
    """
    Classe abstrata que representa um problema a ser resolvido através de procura em espaço de estados

    Fundamentação teórica:
    - P3-iasa-proj.pdf, página 3: o diagrama de classes mostra a estrutura básica de um Problema
    - 09-rac-aut.pdf, página 13 e 10-pee-1.pdf, página 29: definem e especificam os conceitos 
    principais de estado, operador, problema e função objetivo
    """
    def __init__(self, estado_inicial, operadores):
        """
        Inicializa um problema com estado inicial e operadores

        Parâmetros:
        - estado_inicial-  estado inicial do problema
        - operadores - lista de operadores disponíveis para transição de estados

        Validações:
        - verifica se há pelo menos um operador (assert)
        - o estado inicial e operadores são armazenados como atributos privados

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 3: o construtor do Problema recebe estado_inicial, 
        proveniente da associação a Estado, e uma lista de operadores, utilizando
        a classe Operador para a criação dos mesmos
        """
        self.__estado_inicial = estado_inicial
        assert(len(operadores) >= 1) #verifica se a lista de operadores tem pelo menos um operador
        #O assert em Python é uma instrução de verificação (ou "afirmação") que serve para 
        #testar se uma determinada condição é verdadeira durante a execução do programa
        self.__operadores = operadores
    
    @abstractmethod
    def objectivo(self, estado):
        """
        Método abstrato que deve ser implementado para testar se um estado é objetivo

        Parâmetros:
        - estado - estado a ser verificado

        Retorno:
        - bool - True se o estado for objetivo, False caso contrário

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 3: método abstrato objectivo() definido na classe Problema
        - 10-pee-1.pdf, página 29: segundo este slide, é necessário uma função de teste de objetivo
        """
        pass

    #As propriedades abaixo (estado_inicial e operadores) foram assim definidas, segundo o diagrama do slide 3 do P3-iasa-proj
    #A restrição {read-only} indica que o acesso a um determinado atributo é apenas para leitura (propriedade de leitura), por isso
    #foram defindas nos returns como privadas
    @property
    def estado_inicial(self):
        return self.__estado_inicial

    @property
    def operadores(self):
        return self.__operadores