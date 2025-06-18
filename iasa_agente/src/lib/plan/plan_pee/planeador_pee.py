from pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador

class PlaneadorPee(Planeador):
    """
    Esta classe implementa um planeador que utiliza o algoritmo de procura A* 
    para encontrar um plano que leva ao estado objetivo.
    
    Fundamentação teórica:
    - P4-iasa-proj.pdf, página 9: segundo a arquitetura, esta classe
    concretiza o contrato da interface Planeador
    - Este planeador irá utilizar o mecanismo de procura A*, pois esta procura
    é a mais eficiente para chegar a uma solução ótima
    - Todo o o código comportamental aqui implementado foi escrito com a ajuda do docente
    """
    def __init__(self):
        """
        Inicializa o planeador com o mecanismo de procura A*

        Atributos:
        - __mec_pee - mecanismo de procura A*

        Funcionamento:
        - Configura o mecanismo de procura A* que será usado para gerar planos
        - A* é escolhido por garantir optimalidade com heurísticas admissíveis

        Fundamentação teórica:
        - P4-iasa-proj.pdf, páginas 3 e 9: PlaneadorPee é uma especialização
        da interface Planeador, que por sua vez, é necessária no ControloDelib.
        PlaneadorPee precisa também de uma instância de ProcuraInformada, neste caso,
        ProcuraAA, que implementa o algoritmo A*
        """
        self.__mec_pee = ProcuraAA()

    def planear(self, modelo_plan, objetivos):
        """
        Utiliza o algoritmo de procura A* para encontrar o plano que leva ao objetivo

        Parâmetros:
        - modelo_plan - modelo do mundo
        - objetivos - lista de estados desejados

        Retorno:
        - plano - plano que leva ao estado desejado

        Funcionamento:
        1. Obter o estado final a partir da lista de objetivos (primeiro estado objetivo)
        2. Criar um problema de planeamento com o modelo do mundo e o estado final
        3. Configurar heurística de distância para o estado objetivo
        4. Utilizar o mecanismo de procura A* para encontrar a solução
        5. Criar um plano a partir da solução encontrada
        6. Retornar o plano

        Fundamentação teórica:
        - 14-plan-pee.pdf, página 5: se o planeador for baseado em procura
        em espaço de estados, é preciso ter em conta:
            - Modelo do problema de planeamento
            - Heurística a utilizar, se necessário. Neste caso é necessário
            devido à utilização do algoritmo A*
            - Mecanismo de procura a utilizar
        """
        estado_final = objetivos[0]
        problema = ProblemaPlan(modelo_plan, estado_final)
        heuristica = HeurDist(estado_final)
        solucao = self.__mec_pee.procurar(problema, heuristica)
        plano = PlanoPEE(solucao)
        return plano