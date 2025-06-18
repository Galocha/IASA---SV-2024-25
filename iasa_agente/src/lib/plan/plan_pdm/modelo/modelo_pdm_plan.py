from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan

class ModeloPDMPlan(ModeloPlan, ModeloPDM):
    """
    Classe que implementa um modelo de planeamento baseado em Processos de Decisão de Markov (PDM)
    para sistemas autónomos, integrando as interfaces `ModeloPlan` e `ModeloPDM`

    Descrição:
    A classe `ModeloPDMPlan` serve como uma ponte entre o modelo de planeamento genérico (`ModeloPlan`)
    e o modelo específico de PDM (`ModeloPDM`), adaptando um modelo de planeamento para o formato
    exigido por um processo de decisão de Markov. Ela define os estados, ações, transições e recompensas
    necessárias para o planeamento automático com PDM, utilizando um modelo de planeamento subjacente
    e uma lista de estados objetivo. A classe suporta a geração de políticas ótimas, fornecendo as
    funções de transição (T(s, a, s')) e recompensa (R(s, a, s')) conforme descrito nos documentos
    de referência

    Fundamentação teórica:
    - P4-iasa-proj.pdf, página 8: A classe `ModeloPDMPlan` é descrita no diagrama UML como parte
    do pacote `plan.pdm.modelo`, integrando o modelo de planeamento com o PDM
    - 15-pds.pdf, página 8: Um modelo de PDM é definido por um conjunto de estados (S), ações (A(s)),
    probabilidades de transição (T(s, a, s')) e recompensas (R(s, a, s'))
    - 16-plan-pdm.pdf, página 3: O planeamento automático com PDM requer um modelo interno que
    especifique estados, operadores, transições e recompensas, que esta classe implementa
    """
    def __init__(self, modelo_plan, objectivos, rmax = 1000.0):
        """
        Inicializa o modelo de PDM com base no modelo de planeamento e objetivos fornecidos

        Parâmetros:
        - modelo_plan: objeto que implementa a interface `ModeloPlan`, fornecendo estados,
        operadores e estado inicial do ambiente
        - objectivos: lista de estados objetivo que o agente deve alcançar
        - rmax: float, recompensa máxima para estados objetivo. Valor padrão: 1000.0

        Funcionamento:
        1. Armazena os parâmetros `rmax`, `objectivos` e `modelo_plan` como atributos privados
        2. Cria um dicionário de transições (`__transicoes`) que mapeia pares (estado, ação)
        para o estado seguinte (s'), calculado aplicando cada operador a cada estado
        3. Garante que as transições sejam deterministas, com T(s, a, s') = 1 se a transição
        for válida, e T(s, a, s') = 0 caso contrário

        Fundamentação teórica:
        - 15-pds.pdf, página 8: O modelo de PDM requer a definição de transições
        (T(s, a, s')) e recompensas (R(s, a, s')) para suportar o cálculo da utilidade
        - P4-iasa-proj.pdf, página 8: A classe `ModeloPDMPlan` adapta o `ModeloPlan` para
        o formato de PDM, fornecendo as funções necessárias para o planeador
        """
        self.__rmax = rmax
        self.__objectivos = objectivos
        self.__modelo_plan = modelo_plan
        self.__transicoes = {}
        for s in self.obter_estados():
            for a in self.obter_operadores():
                sn = a.aplicar(s)
                if sn:
                    self.__transicoes[(s, a)] = sn

    def obter_estado(self):
        """
        Obtém o estado inicial do modelo de planeamento

        Retorno:
        - Estado: estado inicial do ambiente, conforme definido no modelo subjacente

        Funcionamento:
        - Delega a chamada para o método `obter_estado` do objeto `modelo_plan`,
        retornando o estado inicial do ambiente

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 8: O método `obter_estado` é parte da interface
        `ModeloPlan`, fornecendo o estado inicial para o planeamento
        - 15-pds.pdf, página 8: O estado inicial é necessário para iniciar o processo
        de decisão no modelo de PDM
        """
        return self.__modelo_plan.obter_estado()

    def obter_estados(self):
        """
        Obtém todos os estados possíveis do modelo de planeamento

        Retorno:
        - Lista: conjunto de todos os estados possíveis do ambiente

        Funcionamento:
        - Delega a chamada para o método `obter_estados` do objeto `modelo_plan`,
          retornando o conjunto de estados disponíveis

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 8: O método `obter_estados` é parte da interface
        `ModeloPlan`, fornecendo o conjunto de estados (S) para o planeamento
        - 15-pds.pdf, página 8: O conjunto de estados (S) é um componente essencial
        do modelo de PDM
        """
        return self.__modelo_plan.obter_estados()

    def obter_operadores(self):
        """
        Obtém todos os operadores possíveis do modelo de planeamento

        Retorno:
        - Lista: conjunto de todos os operadores (ações) possíveis no ambiente

        Funcionamento:
        - Delega a chamada para o método `obter_operadores` do objeto `modelo_plan`,
        retornando o conjunto de operadores disponíveis

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 8: O método `obter_operadores` é parte da interface
        `ModeloPlan`, fornecendo as ações possíveis (A(s)) para o planeamento
        - 15-pds.pdf, página 8: O conjunto de ações (A(s)) é um componente essencial
        do modelo de PDM
        """
        return self.__modelo_plan.obter_operadores()

    def S(self):
        """
        Obtém o conjunto de estados do modelo de PDM

        Retorno:
        - Lista: conjunto de todos os estados possíveis (S)

        Funcionamento:
        - Retorna o resultado do método `obter_estados`, cumprindo o contrato da
        interface `ModeloPDM` para fornecer o conjunto de estados

        Fundamentação teórica:
        - 15-pds.pdf, página 8: O conjunto de estados (S) é uma componente fundamental
        do modelo de PDM, usado no cálculo da utilidade e da política
        """
        return self.obter_estados()

    def A(self, s):
        """
        Obtém as ações possíveis para um dado estado

        Parâmetros:
        - s: estado para o qual se deseja determinar as ações possíveis

        Retorno:
        - Lista: conjunto de ações possíveis (A(s)) para o estado fornecido.
        Retorna uma lista vazia se o estado for um objetivo

        Funcionamento:
        1. Verifica se o estado `s` está na lista de objetivos (`__objectivos`)
        2. Se for um estado objetivo, retorna uma lista vazia, indicando que não há
        ações a realizar
        3. Caso contrário, retorna o conjunto de operadores disponíveis através do
        método `obter_operadores`

        Fundamentação teórica:
        - 15-pds.pdf, página 8: O conjunto de ações (A(s)) depende do estado atual
        e é essencial para definir as transições no modelo de PDM
        - 16-plan-pdm.pdf, página 3: Estados objetivo não possuem ações associadas,
        pois representam o término do processo de planeamento
        """
        if s in self.__objectivos:
            return []
        return self.obter_operadores()

    def T(self, s, a, sn):
        """
        Calcula a probabilidade de transição de um estado para outro através de uma ação

        Parâmetros:
        - s: estado atual
        - a: ação aplicada
        - sn: estado seguinte

        Retorno:
        - float: probabilidade de transição T(s, a, s'), que é 1 se a transição for
        válida (s, a → s'), ou 0 caso contrário

        Funcionamento:
        1. Consulta o dicionário de transições (`__transicoes`) para verificar se o
        par (s, a) leva ao estado `sn`
        2. Retorna 1 se a transição for válida, ou 0 se não for

        Fundamentação teórica:
        - 15-pds.pdf, página 8: A função de transição T(s, a, s') define a probabilidade
        de alcançar o estado s' a partir de s com a ação a, sendo determinista
        neste caso (T = 1 ou T = 0)
        - 16-plan-pdm.pdf, página 3: A função de transição é essencial para o modelo
        de PDM usado no planeamento automático
        """
        sn = self.__transicoes.get((s, a))
        return 1 if sn is not None else 0

    def R(self, s, a, sn):
        """
        Calcula a recompensa associada a uma transição

        Parâmetros:
        - s: estado atual
        - a: ação aplicada
        - sn: estado seguinte

        Retorno:
        - float: recompensa R(s, a, s'), que é `rmax` se o estado seguinte for um
        objetivo, ou o negativo do custo da ação caso contrário

        Funcionamento:
        1. Verifica se o estado seguinte (`sn`) está na lista de objetivos
        2. Se for um objetivo, retorna a recompensa máxima (`__rmax`)
        3. Caso contrário, retorna o custo da ação (`a.custo(s, sn)`) com sinal
        negativo, representando uma penalidade

        Fundamentação teórica:
        - 15-pds.pdf, página 8: A função de recompensa R(s, a, s') define o valor
        imediato associado a uma transição, usado no cálculo da utilidade
        - 15-pds.pdf, página 20: No ambiente 4x3, recompensas negativas são usadas
        para estados não terminais (e.g., -0.04), enquanto estados objetivo têm
        recompensas positivas
        """
        if sn in self.__objectivos: #caso o estado seguinte seja objetivo
            return self.__rmax #retorna a recompensa máxima, pois já se alcançou o objetivo
        else: #caso o estado não seja objetivo
            return 0 #retorna o custo da ação com sinal negativo (pois recompensas negativas são usadas em estados não terminais)

    def suc(self, s, a):
        """
        Obtém os estados sucessores de um estado após a aplicação de uma ação

        Parâmetros:
        - s: estado atual
        - a: ação aplicada

        Retorno:
        - Lista: lista com o estado seguinte (s') se a transição for válida, ou
        uma lista vazia caso contrário

        Funcionamento:
        1. Consulta o dicionário de transições (`__transicoes`) para obter o estado
        seguinte associado ao par (s, a)
        2. Retorna uma lista contendo o estado seguinte, se existir, ou uma lista
        vazia, se a transição não for válida

        Fundamentação teórica:
        - 15-pds.pdf, página 8: A função de sucessores é usada para identificar os
        estados alcançáveis a partir de um estado e uma ação, suportando o cálculo
        das transições no modelo de PDM
        """
        sn = self.__transicoes.get((s, a)) #tem que ser com get, se não dá uma exceção
        return [sn] if sn else [] #retorna uma lista com o estado sucessor se existir, ou uma lista vazia se não existir
        #retorna-se uma lista e não um único estado, porque o ambiente pode ser não determinista
        #caso geral, return [sn] if sn is not None else []
    
    @property
    def rmax (self):
        return self.__rmax
    
    @property
    def objetivos (self):
        return self.__objectivos