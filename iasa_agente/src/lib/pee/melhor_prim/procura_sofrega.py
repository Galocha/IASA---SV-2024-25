from pee.melhor_prim.aval.avaliador_sofrega import AvaliadorSofrega
from pee.melhor_prim.procura_informada import ProcuraInformada

class ProcuraSofrega(ProcuraInformada):
    """
    Implementação do algoritmo de Procura Sôfrega, que prioriza 
    a exploração de nós com menor valor heurístico h(n), ignorando 
    o custo acumulado do caminho g(n)

    Fundamentação teórica:
    - 12-pee-3.pdf, página 17: a procura sôfrega é uma estratégia
    puramente guiada por heurísticas, onde as soluções são sub-ótimas, 
    e há a minimização da estimativa do custo para atingir o objetivo
    """
    def __init__(self):
        """
        Inicializa o mecanismo de procura com um AvaliadorSofrega,
        que implementa a estratégia de priorizar apenas h(n)

        Funcionamento:
        1. Cria uma instância de AvaliadorSofrega (f(n) = h(n))
        2. Passa o avaliador para a superclasse
        3. Configura automaticamente uma FronteiraPrioridade

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 15: é percetível que esta classe
        herda de ProcuraInformada e que usa o AvaliadorSofrega
        """
        super().__init__(AvaliadorSofrega())