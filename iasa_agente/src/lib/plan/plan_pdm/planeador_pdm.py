from pdm.pdm import PDM
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador

class PlaneadorPDM(Planeador):
    """
    Classe que implementa um planeador baseado em Processos de Decisão de Markov (PDM) para sistemas autónomos
    
    Descrição:
    - A classe `PlaneadorPDM` herda da interface `Planeador` e é responsável por gerar uma política ótima
    para um problema de planeamento automático utilizando a abordagem de PDM. Baseia-se na maximização
    da utilidade esperada, calculada iterativamente através da Equação de Bellman, considerando um fator
    de desconto (gama) e um limiar de convergência (delta_max). O planeador utiliza um modelo de planeamento
    (ModeloPDMPlan) e objetivos para gerar um plano (PlanoPDM) com a utilidade e política resultantes

    Fundamentação teórica:
    - P4-iasa-proj.pdf, página 12: A classe `PlaneadorPDM` é descrita no diagrama UML como parte do pacote `pdm`,
      gerando um `PlanoPDM` com base no modelo de planeamento
    - 15-pds.pdf, páginas 25-28, 35: O planeamento baseia-se na Equação de Bellman e no cálculo iterativo
      da utilidade, onde a política ótima é obtida maximizando a soma ponderada das recompensas e utilidades futuras
    - 16-plan-pdm.pdf, página 3: O planeador utiliza um modelo interno de PDM com estados, operadores, transições
      (T(s, a, s')) e recompensas (R(s, a, s')) para gerar a política de ação
    """
    def __init__(self, gama = 0.85, delta_max = 1.0):
        """
        Inicializa o planeador PDM com os parâmetros de desconto e convergência.

        Parâmetros:
        - gama: float, fator de desconto para recompensas futuras (γ ∈ [0,1]). Valor padrão: 0.85
        - delta_max: float, limiar máximo para a diferença de utilidade entre iterações, 
        determinando a convergência do cálculo. Valor padrão: 1.0

        Fundamentação teórica:
        - 15-pds.pdf, página 16: O fator de desconto (γ) é introduzido para refletir o efeito da passagem do tempo
        nas recompensas futuras, evitando somas infinitas
        - 15-pds.pdf, página 32: O limiar de convergência (`delta_max`) é usado como critério de paragem
        no cálculo iterativo da utilidade
        """
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objectivos):
        """
        Gera um plano baseado em PDM para o modelo de planeamento e objetivos fornecidos.

        Parâmetros:
        - modelo_plan: objeto que implementa a interface `ModeloPlan`, contendo informações sobre estados,
                      operadores, transições e recompensas do ambiente.
        - objectivos: lista de estados objetivo que o planeador deve alcançar.

        Retorno:
        - PlanoPDM: objeto contendo a utilidade calculada e a política ótima gerada pelo processo de PDM.

        Funcionamento:
        1. Cria um objeto `ModeloPDMPlan` com base no `modelo_plan` e `objectivos`, adaptando o modelo
        para o formato de PDM
        2. Instancia um objeto `PDM` com o modelo adaptado, o fator de desconto (`gama`) e o limiar de
        convergência (`delta_max`)
        3. Executa o método `resolver` do objeto `PDM` para calcular a utilidade e a política ótima
        4. Retorna um objeto `PlanoPDM` com a utilidade e a política resultantes

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 12: O método `planear` é a realização do contrato da interface `Planeador`,
        gerando um `PlanoPDM` com base no modelo de planeamento
        - 15-pds.pdf, página 35: O cálculo da utilidade segue o algoritmo iterativo descrito
        - 16-plan-pdm.pdf, página 3: O planeador requer um modelo de PDM interno com estados, operadores,
        transições e recompensas para suportar o cálculo da política ótima
        - Implementação baseada no main do teste_pdm.py, que demonstra o uso do PDM para resolver um problema de planeamento
        """
        modelo_pdm_plan = ModeloPDMPlan(modelo_plan, objectivos)
        pdm = PDM(modelo_pdm_plan, self.__gama, self.__delta_max)
        utilidade, politica = pdm.resolver()
        return PlanoPDM(utilidade, politica)

    #propriedades getter para os fator de desconto e limiar de convergência
    @property
    def gama(self):
        return self.__gama
    
    @property
    def delta_max(self):
        return self.__delta_max