from plan.plano import Plano

class PlanoPDM(Plano):
    """
    Classe que implementa um plano baseado em Processos de Decisão de Markov (PDM) para sistemas autónomos

    Descrição:
    - A classe `PlanoPDM` herda da interface `Plano` e representa um plano gerado por um planeador PDM,
    contendo a utilidade associada a cada estado e a política ótima que define as ações a executar
    em cada estado. A política é representada como um mapeamento de estados para ações, enquanto
    a utilidade reflete o valor esperado a longo prazo de cada estado, calculado iterativamente
    com base na Equação de Bellman. Esta classe é utilizada no controlo deliberativo de sistemas
    autónomos para determinar a próxima ação a realizar com base no estado atual

    Fundamentação teórica:
    - P4-iasa-proj.pdf, página 12: A classe `PlanoPDM` é descrita no diagrama UML como parte do
    pacote `pdm`, sendo o resultado do planeamento realizado pelo `PlaneadorPDM`
    - 15-pds.pdf, páginas 19, 25: A política (π) define a estratégia de ação, sendo determinista
    (mapeia cada estado a uma única ação) ou não determinista. A utilidade (U(s)) é calculada
    usando a Equação de Bellman
    - 16-plan-pdm.pdf, página 3: O plano é baseado em um modelo de PDM, que inclui estados,
    operadores, transições (T(s, a, s')) e recompensas (R(s, a, s'))
    """
    def __init__(self, utilidade, politica):
        """
        Inicializa o plano PDM com a utilidade e a política fornecidas

        Parâmetros:
        - utilidade: dicionário que associa cada estado ao seu valor de utilidade (U(s)),
        calculado pelo planeador PDM
        - politica: dicionário que associa cada estado à ação ótima (π(s)) a ser executada

        Funcionamento:
        1. Armazena a `utilidade` e a `politica` como atributos privados para uso nos métodos
        de consulta e controlo
        2. Configura o plano para suportar a execução de ações com base no estado atual do agente

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 12: O `PlanoPDM` é gerado pelo `PlaneadorPDM` e contém
        a utilidade e a política resultantes do processo de planeamento
        - 15-pds.pdf, página 35: A utilidade e a política são obtidas pelo algoritmo iterativo
        de cálculo da utilidade, baseado na Equação de Bellman
        """
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_accao(self, estado):
        """
        Obtém a ação a executar para o estado fornecido com base na política do plano

        Parâmetros:
        - estado: estado atual do agente para o qual se deseja determinar a ação

        Retorno:
        - Operador: ação associada ao estado na política (π(s)), ou None se o estado
        não estiver presente na política

        Funcionamento:
        1. Consulta o dicionário da política (`__politica`) para obter a ação associada
        ao estado fornecido
        2. Retorna a ação correspondente, se existir, ou None, indicando que o estado
        não está mapeado na política

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 7: Este método implementa o contrato da interface `Plano`,
        que exige a obtenção da próxima ação com base no estado atual
        - 15-pds.pdf, página 26: A política ótima (π*) mapeia cada estado para a ação que
        maximiza a utilidade esperada, sendo usada para controlo deliberativo
        """
        return self.__politica.get(estado, None)

    def mostrar(self, vista):
        if self.__politica:
            #Mostrar utilidade
            for estado, valor in self.__utilidade.items(): #quando separamos duas variáveis em python, está implícito um tuplo
                #.items() retorna uma lista de tuplos (chave, valor) do dicionário
                vista.mostrar_valor_posicao(estado.posicao, valor)
            #Mostrar política
            for estado, acao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, acao.ang)


    #propriedades getter para a utilidade e política
    @property
    def utilidade(self):
        return self.__utilidade
    
    @property
    def politica(self):
        return self.__politica