from lib.mod. estado import Estado

class EstadoContagem(Estado):
    """
    Implementação concreta de Estado que representa um estado numérico contável

    Fundamentação teórica:
    - P3-iasa-proj.pdf, página 3: Diagrama de classes mostra Estado como superclasse
    - 09-rac-aut.pdf, página 13: Estado - representa uma configuração de um sistema ou problema
    """
    def __init__(self, valor):
        """
        Inicializa um estado de contagem com um valor numérico específico

        Parâmetros:
        valor - Valor numérico que representa o estado (int ou float)

        Funcionamento:
        - Armazena o valor como atributo do estado
        - O valor serve como identificador único do estado

        Fundamentação teórica:
        - 10-pee-1.pdf, página 29: estado contém um valor
        """
        self.valor = valor

    def id_valor(self):
        """
        Retorna o identificador único do estado

        Retorno:
        int/float - O valor numérico que identifica o estado

        Funcionamento:
        - Implementa o método abstrato da classe Estado
        - Usado para comparação e hash de estados

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 3: 
            Método id_valor() no diagrama de classes
            id_valor(): int - define id único do estado em função do valor do mesmo
        """
        return self.valor
