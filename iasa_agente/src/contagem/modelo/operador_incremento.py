from lib.mod.operador import Operador
from modelo.estado_contagem import EstadoContagem

class OperadorIncremento (Operador):
    """
    Implementação concreta de Operador que realiza incrementos numéricos em estados de contagem

    Fundamentação teórica:
    - P3-iasa-proj.pdf, página 3: Diagrama de classes mostra Operador como interface
    """
    def __init__(self, incremento):
        """
        Inicializa o operador com um valor de incremento fixo

        Parâmetros:
        incremento - Valor numérico (int/float) que será adicionado ao estado atual

        Funcionamento:
        - Armazena o valor de incremento como atributo da instância
        - Este valor será usado em todas as aplicações do operador

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 3: Padrão de implementação de operadores concretos
        """
        self.incremento = incremento

    def aplicar(self, estado):
        """
        Aplica o incremento ao estado atual, gerando um novo estado

        Parâmetros:
        estado - EstadoContagem atual (deve conter atributo 'valor')

        Retorno:
        EstadoContagem - Novo estado com valor incrementado

        Funcionamento:
        1. Soma o incremento ao valor do estado atual
        2. Cria um novo EstadoContagem com o valor resultante
        3. Retorna o novo estado

        Fundamentação teórica:
        - 09-rac-aut.pdf, página 13: "operador.aplicar: estado → estado"
        - 10-pee-1.pdf, página 16: Processo de geração de estados sucessores
        """
        novo_valor = estado.valor + self.incremento
        return EstadoContagem(novo_valor)
    
    def custo(self, estado, estado_suc):
        """
        Calcula o custo da transição como o quadrado do incremento

        Parâmetros:
        estado - Estado de origem (não utilizado no cálculo)
        estado_suc - Estado destino (não utilizado no cálculo)

        Retorno:
        float - Custo da transição (incremento ao quadrado)

        Funcionamento:
        - Implementa uma métrica de custo quadrática
        - O custo é fixo para este operador, independente dos estados
        - Custo calculado como incremento² para penalizar incrementos maiores

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 3: Contrato da interface Operador
        - 10-pee-1.pdf, página 29: Operador define custo de transição
        """
        return self.incremento ** 2