from pdm.mec_util import MecUtil

class PDM:
    """
    Implementação de um Processo de Decisão de Markov (PDM)
    O Processo de Decisão de Markov (PDM) constitui um modelo matemático formal utilizado para representar 
    processos estocásticos (processos incertos, mas definidos com probabilidades bem definidas) de decisão 
    sequencial, caracterizados por um conjunto de estados, um conjunto de ações disponíveis e uma função de 
    recompensas associada às transições entre estados

    O PDM consiste em:
    1. Um conjunto de estados do ambiente (S)
    2. Ações possíveis em cada estado (A(s))
    3. Uma função de transição T(s,a,s') que define a probabilidade de chegar ao estado s'
    ao executar a ação a no estado s
    4. Uma função de recompensa R(s,a,s') que define o ganho imediato de cada transição
    5. Um fator de desconto "gama" que pondera recompensas futuras versus imediatas
    
    Funcionamento:
    - Resolve a política ótima e utilidade de cada estado presente nos estados disponíveis
    (calculada a partir do mecanismo de utilidade)
    
    Fundamentação teórica:
    - 15-pds.pdf, página 35: algoritmo de iteração de valor para cálculo da utilidade
    - P4-iasa-proj.pdf, página 11: corresponde à classe PDM no diagrama de classes
    - 15-pds.pdf, página 26: princípio da solução ótima e equações de Bellman
    """
    def __init__(self, modelo, gama, delta_max):
        """
        Inicialização de um Processo de Decisão de Markov com os parâmetros base

        Parâmetros:
        - modelo: instância que representa o modelo de PDM, contendo os estados (S), ações (A), 
        transições (T) e recompensas (R)
        - gama: fator de desconto [0,1], que pondera o valor das recompensas futuras (15-pds.pdf, página 16)
        - delta_max: critério de paragem para a iteração de valor; define o limiar de convergência 
        da diferença entre utilidades sucessivas (15-pds.pdf, página 35)

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 11: construtor da classe PDM com estes parâmetros
        """
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
        self.__mec_util = MecUtil(self.__modelo, self.__gama, self.__delta_max)

    def politica(self, U):
        """
        Cálculo da política ótima com base na utilidade de cada estado

        O que é a política?
        - A política π(s) é uma estratégia que define a ação a ser tomada em cada estado s para maximizar a 
        utilidade esperada. Esta pode ser:
            - Determinista - uma ação específica é escolhida para cada estado, onde:
            π : S → A(s)
            - Estocástica (não determinista) - uma distribuição de probabilidade sobre as ações é definida 
            para cada estado, onde: 
            π : S × A(s) → [0, 1]
        
        Qual é o objetivo?
        - A política ótima é calculada escolhendo, para cada estado, a ação que maximiza o valor esperado 
        da utilidade futura, considerando as probabilidades de transição, T(s,a,s′), e as recompensas descontadas,
        R(s,a,s′)

        Parâmetros:
        - U - dicionário com a utilidade calculada de cada estado (resultado da iteração de valor)

        Retorno:
        - dicionário - onde a chave é o estado e o valor é a ação ótima a tomar nesse estado

        Funcionamento:
        - Para cada estado `s`, seleciona a ação `a` que maximiza a utilidade esperada, calculada 
        pela soma ponderada das utilidades dos estados seguintes, de acordo com a função de transição 
        e o fator de desconto
        - A utilidade da ação é calculada através do método `util_accao` da classe `MecUtil`

        Fundamentação teórica:
        - 15-pds.pdf, página 26: utiliza as equações de Bellman para determinar a ação ótima.
        A equação de Bellman define a relação entre a utilidade de um estado e as utilidades dos estados
        sucessores, considerando as ações disponíveis e as probabilidades de transição
        - P4-iasa-proj.pdf, página 11: método `politica()` da classe PDM
        """
        S, A, util_accao = self.__modelo.S, self.__modelo.A, self.__mec_util.util_accao
        politica = {}
        for s in S():
            if A(s):
                politica[s] = max(A(s), key=lambda a: util_accao(s, a, U))
        return politica

    def resolver(self):
        """
        Resolve o PDM calculando utilidades ótimas e política correspondente
        
        Retorno:
        - tuplo: (utilidade, politica) onde:
            - utilidade: dicionário com a utilidade final de cada estado
            - politica: dicionário com a ação ótima para cada estado
        
        Funcionamento:
        1. Calcula utilidades ótimas usando iteração de valor (via MecUtil)
        2. Deriva a política ótima a partir das utilidades calculadas
        
        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 11: método resolver() da classe PDM
        - 15-pds.pdf, página 26: separação entre cálculo de utilidade e política
        """
        utilidade= self.__mec_util.utilidade()
        return utilidade, self.politica(utilidade)