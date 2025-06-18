from mod.problema import Problema

class ProblemaPlan(Problema):
    """
    Classe que representa um problema de planeamento concreto, especializando da classe
    Problema para o contexto de planeamento em sistemas autónomos

    Atributos:
    - __estado_final: estado objetivo que se pretende alcançar

    Fundamentação teórica:
    - 14-plan-pee.pdf, página 3: um problema de planeamento em sistemas autónomos refere-se 
    à determinação de uma sequência de ações que permite a um agente alcançar um estado objetivo 
    a partir de um estado inicial, dentro de um ambiente representado por um espaço de estados.
    Neste contexto:
        - Cada estado representa uma configuração possível do sistema
        - As ações são modeladas como operadores, que transformam um estado noutro
        - O espaço de estados é uma abstracção do domínio do problema, onde se representam todas as 
        possíveis configurações e transições
        - A solução consiste num percurso no espaço de estados, ou seja, uma sequência de operadores 
        que leva do estado inicial ao objetivo
    - P4-iasa-proj.pdf, página 10: mostra a implementação concreta de ProblemaPlan, indicando que
    o mesmo especializa a classe Problema e que precisa de uma instância de Estado (self.__estado_final)
    - Todo o código comportamental foi implementado de acordo com as instruções do professor
    """
    def __init__(self, modelo_plan, estado_final):
        """
        Constrói a representação formal do problema de planeamento como problema de procura

        Parâmetros:
        - modelo_plan: modelo de planeamento define o principal do problema a resolver
        - estado_final: estado objetivo que define a solução do problema

        Funcionamento:
        1. Obtém o estado inicial do modelo (ponto de partida no espaço de estados)
        2. Obtém os operadores/ações disponíveis (transições possíveis entre estados)
        3. Armazena o estado alvo que define a solução do problema

        Fundamentação teórica:
        - 14-plan-pee.pdf, página 3: "Estado inicial" e "Objetivo" como componentes essenciais
        - 14-plan-pee.pdf, página 4: operadores como meios para transição entre estados
        """
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final
    
    def objectivo(self, estado):
        """
        Determina se um estado corresponde ao estado objetivo do problema

        Parâmetros:
        - estado: estado atual a ser avaliado (configuração corrente do sistema)

        Retorno:
        - bool: True se o estado é o objetivo, False caso contrário

        Funcionamento:
        - Realiza uma comparação completa entre o estado fornecido e o estado final
        - A igualdade deve considerar todos os atributos relevantes da representação do estado

        Fundamentação teórica:
        - 14-plan-pee.pdf, página 3: "A solução de um problema corresponde a [...] um percurso [...] que liga
          um estado inicial a um estado objetivo"
        """
        return estado == self.__estado_final