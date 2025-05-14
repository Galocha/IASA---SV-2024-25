from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

class ProcuraCustoUnif(ProcuraMelhorPrim):
    """
    Implementação do algoritmo de Procura de Custo Uniforme,
    que expande sempre o nó com menor custo acumulado desde o estado inicial

    Fundamentação teórica:
    - 12-pee-3.pdf, página 19: define esta procura como um caso especial de melhor-primeiro
    onde f(n) = g(n), minimizando o custo acumulado a cada nó explorado. Esta não tira
    partido do conhecimento do domínio do problema expresso através de h(n)
    - P3-iasa-proj.pdf, páginas 13 e 14: os diagramas explicitam que ProcuraCustoUnif
    herda de ProcuraMelhorPrim, ou seja, é uma implementação de ProcuraMelhorPrim, e
    ainda dependende do AvaliadorCustoUnif
    """
    def __init__(self):
        """
        Inicializa o mecanismo de procura com um AvaliadorCustoUnif,
        que prioriza nós exclusivamente pelo custo acumulado até um certo
        estado n (g(n))

        Funcionamento:
        1. Cria uma instância de AvaliadorCustoUnif (que implementa f(n) = g(n))
        2. Passa o avaliador para a superclasse ProcuraMelhorPrim
        3. Configura automaticamente uma FronteiraPrioridade

        Fundamentação teórica:
        - 12-pee-3.pdf, página 19: mostra que a procura custo uniforme é equivalente 
        a A* com h(n) = 0
        - P3-iasa-proj.pdf, página 14: segundo o diagrama, esta classe conta
        apenas com o construtor
        """
        super().__init__(AvaliadorCustoUnif())