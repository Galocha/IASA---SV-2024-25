from lib.mod.problema import Problema
from modelo.estado_contagem import EstadoContagem
from modelo.operador_incremento import OperadorIncremento

class ProblemaContagem(Problema):
    def __init__(self, valor_inicial, valor_final, incrementos):
        """
        Inicializa um problema de contagem numérica com configuração completa

        Funcionamento:
        1. Criação do estado inicial:
        - Instancia um EstadoContagem usando o valor_inicial fornecido

        2. Geração dos operadores de incremento:
        - Para cada valor na lista incrementos, cria um OperadorIncremento distinto

        3. Configuração do objetivo:
        - Armazena valor_final como atributo privado __valor_final
        
        Fundamentação teórica:
        - 10-pee-1.pdf, página 29: componentes de um problema: estado inicial e operadores
        """
        super().__init__(EstadoContagem(valor_inicial), [OperadorIncremento(incremento)for incremento in incrementos])
        self.__valor_final = valor_final


    def objectivo(self, estado):
        """
        Verifica se um estado atinge o objetivo do problema

        Parâmetros:
        estado - EstadoContagem a ser verificado (deve conter atributo 'valor')

        Retorno:
        bool - True se o valor do estado for >= valor_final, False caso contrário

        Funcionamento:
        - Compara o valor do estado com o valor_final armazenado
        - Considera qualquer valor igual ou superior como solução válida

        Fundamentação teórica:
        - 09-rac-aut.pdf, página 13: "Função objectivo: estado → {True, False}"
        - 10-pee-1.pdf, página 5: Verificar se estado atual corresponde ao objetivo
        - P3-iasa-proj.pdf, página 3: Método objectivo() na classe abstrata
        """
        return estado.valor >= self.__valor_final
        