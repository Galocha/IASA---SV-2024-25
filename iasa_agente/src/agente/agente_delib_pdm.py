from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae.agente.agente import Agente
from sae.simulador import Simulador

class AgenteDelibPDM(Agente):
    """
    Classe que implementa um agente deliberativo baseado em Processos de Decisão de Markov (PDM)
    para sistemas autónomos

    A classe `AgenteDelibPDM` herda da classe base `Agente` e implementa um agente que utiliza
    controlo deliberativo baseado em PDM para tomar decisões em ambientes incertos. O agente
    integra um mecanismo de controlo (`ControloDelib`) que utiliza um planeador PDM (`PlaneadorPDM`)
    para gerar políticas ótimas, maximizando a utilidade esperada com base na Equação de Bellman.
    O agente percebe o ambiente, processa a percepção para determinar a ação a executar e atua
    no ambiente, exibindo o plano gerado através de uma vista

    Fundamentação teórica:
    - P4-iasa-proj.pdf, página 3: O controlo deliberativo é descrito como um processo que
    utiliza planeamento para gerar ações com base na percepção do ambiente
    - P4-iasa-proj.pdf, página 12: O `PlaneadorPDM` é usado para gerar um `PlanoPDM`, que
    contém a política e a utilidade para orientar o comportamento do agente
    - 15-pds.pdf, páginas 19, 25: A política ótima (π*) mapeia estados para ações,
    maximizando a utilidade esperada calculada pela Equação de Bellman
    - 16-plan-pdm.pdf, página 3: O planeamento com PDM gera políticas de ação baseadas em
    um modelo interno com estados, operadores, transições e recompensas
    """
    def __init__(self):
        """
        Inicializa o agente deliberativo com um controlo baseado em PDM

        Funcionamento:
        1. Chama o construtor da classe base `Agente` utilizando `super().__init__()`
        para inicializar os atributos herdados
        2. Cria uma instância de `ControloDelib` com um `PlaneadorPDM`, configurado
        com fator de desconto (padrão=0.85) e limiar de convergência (padrão=1.0)
        3. Armazena o objeto de controlo como atributo privado `__controlo` para uso
        no processamento de percepções

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 3: O controlo deliberativo é implementado pela classe
        `ControloDelib`, que utiliza um planeador para gerar planos baseados na percepção
        - P4-iasa-proj.pdf, página 12: O `PlaneadorPDM` é configurado com parâmetros como
        gama e delta_max para gerar políticas ótimas
        - 15-pds.pdf, página 16: O fator de desconto (γ) regula a importância das recompensas
        futuras, enquanto o limiar de convergência (δ_max) define a precisão do cálculo
        iterativo da utilidade (página 32)

        Porquê aumentar o gama para 0.95?
        - Se o gama for mais perto de 1, dá maior peso às recompensas futuras, incentivando o agente 
        a considerar o impacto a longo prazo das suas ações. Isso é crucial para alcançar objetivos 
        distantes ou múltiplos, especialmente em ambientes grandes

        Porquê não usar gama = 1?
        - as recompensas futuras não são descontadas, ou seja, têm o mesmo peso que as recompensas 
        imediatas, tratando todas as recompensas ao longo do tempo como igualmente 
        - isto leva a um cálculo infinito, pois a soma das recompensas futuras não converge, e assim o agente
        não consegue determinar uma política ótima, resultando em um comportamento indefinido/indeciso
        """
        super().__init__()  # Inicializa a classe base Agente
        self.__controlo = ControloDelib(PlaneadorPDM(gama = 0.95))
    
    def executar(self):
        """
        Executa o ciclo de decisão do agente: perceber, processar, exibir e atuar

        Funcionamento:
        1. Obtém a percepção atual do ambiente chamando o método herdado `_percepcionar`
        2. Processa a percepção utilizando o objeto `__controlo` para determinar a ação
        a executar, com base na política gerada pelo `PlaneadorPDM`
        3. Exibe o plano atual (utilidade e política) através do método `mostrar` do
        objeto `__controlo`, utilizando a vista associada ao agente (`self.vista`)
        4. Atua no ambiente executando a ação determinada, através do método herdado
        `_actuar`

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 3: O ciclo de decisão do agente deliberativo envolve
        perceber o ambiente, processar a percepção para gerar um plano e atuar com base
        na ação selecionada
        - P4-iasa-proj.pdf, página 9: O método `mostrar` da classe `Plano` (implementado
        por `PlanoPDM`) é usado para visualizar o plano gerado
        - 15-pds.pdf, página 19: A política gerada pelo PDM é usada para selecionar ações
        com base no estado percebido, suportando o controlo deliberativo
        """
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        self._actuar(accao)

if __name__ == "__main__":
    agente = AgenteDelibPDM()
    simulador = Simulador(4, agente, vista_modelo=True)
    simulador.executar()