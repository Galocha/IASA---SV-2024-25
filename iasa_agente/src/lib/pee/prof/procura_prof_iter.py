from .procura_prof_lim import ProcuraProfLim

class ProcuraProfIter(ProcuraProfLim):
    """
    Classe que implementa o mecanismo de procura em profundidade iterativa

    Fundamentação teórica:
    - 11-pee-2.pdf, páginas 16 e 17: a procura em profundidade iterativa, faz procuras em profundidade sucessivas 
        com limites de profundidade incrementais
    - P3-iasa-proj.pdf, página 9: é descrito o diagrama de classes que inclui a implementação de tanto desta classe,
    como da classe ProcuraProfLim
    """
    def __init__(self, prof_max_inicial = 10):
        """
        Construtor da classe ProcuraProfIter

        Funcionamento:
        - Como a procura em profundidade iterativa é uma procura com limites de profundidade, então é chamado o construtor
        da superclasse ProcuraProfLim, passando como parâmetro um valor para a profundidade máxima inicial

        Parâmetros:
        - prof_max_inicial: valor da profundidade máxima inicial, que, por defeito, é 10

        Fundamentação teórica:
        - 11-pee-2.pdf, página 17: existe a possibilidade de limitar a procura a uma profundidade máxima
        - P3-iasa-proj.pdf, página 9: mesmo não estando explícito, esta classe depende da ProcuraProfLim, por isso
        o construtor, como já foi mencionado, chama o construtor da superclasse e passa como parâmetro a profundidade
        máxima inicial
        """
        super().__init__(prof_max_inicial)


    def procurar(self, problema, inc_prof = 1, limite_prof = 100):
        """
        Método que implementa a procura em profundidade iterativa para resolver um problema

        Funcionamento:
        - Realiza múltiplas procuras em profundidade limitada, incrementando progressivamente
        o limite de profundidade até encontrar uma solução ou atingir o limite máximo especificado
        - Em cada iteração, executa uma procura em profundidade até a profundidade atual
        - Se encontrar uma solução válida dentro do limite, retorna-a imediatamente

        Parâmetros:
        - problema: objeto que contém a definição do problema
        - inc_prof: incremento de profundidade entre iterações, por defeito tem como valor 1
        - limite_prof: profundidade máxima a explorar, por defeito tem como valor 100

        Fundamentação teórica:
        - 11-pee-2.pdf, página 17: esta função foi implementada segundo o pseudocódigo 'function procura_prof_iter'
        - P3-iasa-proj.pdf, página 9: este método está presente no diagrama de classes 'Procura em Profundidade"
        """
        for profundidade in range(0, limite_prof + 1, inc_prof): #itera de 0 a limite_prof, de inc_prof em inc_prof (sendo limite_prof = limite_prof+1, pois é necessário adicionar 1)
            self._prof_max = profundidade #atualiza a profundiade máxima como profundidade, para se poder iterar por cada limite
            solucao = super().procurar(problema) #realiza uma procura em profundidade com o limite de profundidade atual
            if solucao: #se existir solução
                return solucao #retorna a solução