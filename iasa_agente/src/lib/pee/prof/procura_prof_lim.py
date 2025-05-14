from pee.prof.procura_prof import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    """
    Classe que implementa o mecanismo de procura em profundidade limitada

    Fundamentação teórica:
    - 11-pee-2.pdf, página 15: descreve o algoritmo de procura em profundidade limitada
    - P3-iasa-proj.pdf, página 9: mostra a hierarquia de classes onde esta se insere, como especialização
      da ProcuraProfundidade
    - 10-pee-1.pdf, páginas 8 a 16: explica a estratégia de procura em profundidade que esta classe estende
    """
    def __init__(self, prof_max = 10):
        """
        Construtor da classe ProcuraProfLim

        Funcionamento:
        - Inicializa uma procura em profundidade com um limite máximo de exploração
        - Herda o comportamento base da procura em profundidade

        Parâmetros:
        - prof_max: profundidade máxima de exploração, por defeito o valor é 10

        Fundamentação teórica:
        - 11-pee-2.pdf, página 15: limita a procura a uma determinada profundidade máxima
        - P3-iasa-proj.pdf, página 9: indica a relação de herança com ProcuraProfundidade
        """
        super().__init__()
        self._prof_max = prof_max

    def _expandir(self, problema, no):
        """
        Método que expande um nó até a profundidade máxima configurada

        Funcionamento:
        - Só expande nós cuja profundidade seja inferior à profundidade máxima
        - Caso contrário, retorna lista vazia (não expande)

        Parâmetros:
        - problema: definição do problema a resolver
        - no: nó atual a ser expandido

        Retorno:
        - Lista de nós sucessores ou lista vazia se atingir o limite

        Fundamentação teórica:
        - 11-pee-2.pdf, página 15: condição "Se profundidade do nó for menor que profundidade máxima"
        - P3-iasa-proj.pdf, página 5 e 9: mostra a integração com o mecanismo de procura
        """
        if no.profundidade < self._prof_max:
            return super()._expandir(problema, no)
        else:
            return []