from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada

class ProcuraAA(ProcuraInformada):
    """
    Implementação do algoritmo A* para procura em espaços de estados
    Combina o custo acumulado g(n) com uma heurística admissível h(n) para garantir
    soluções ótimas de forma eficiente (f(n) = g(n) + h(n)), minimizando
    o custo global

    Fundamentação teórica:
    - 12-pee-3.pdf, página 20: apresenta o A* como algoritmo ótimo quando
    utiliza uma heurística admissível (0 ≤ h(n) ≤ h*(n), onde h*(n) é o custo mínimo
    do nó n até ao objetivo)
    - P3-iasa-proj.pdf, página 14: o diagrama de classes mostra ProcuraAA como
    especialização de ProcuraInformada, que por sua vez, herda de ProcuraMelhorPrim
    """
    def __init__(self):
        """
        Inicializa o mecanismo de procura A* com um AvaliadorAA configurado
        
        Funcionamento:
        1. Cria uma instância de AvaliadorAA (que implementa f(n) = g(n) + h(n))
        2. Passa o avaliador para a superclasse ProcuraMelhorPrim
        3. Configura a fronteira como FronteiraPrioridade para ordenação automática

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 15: diagrama mostra a dependência desta classe
        de AvaliadorAA, daí ter que se passar AvaliadorAA como parâmetro
        """
        super().__init__(AvaliadorAA())