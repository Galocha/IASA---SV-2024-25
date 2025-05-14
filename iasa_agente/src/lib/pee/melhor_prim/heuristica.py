from abc import ABC, abstractmethod

class Heuristica(ABC):
    """
    Classe abstrata que define a interface para funções heurísticas utilizadas
    em algoritmos de procura informada como A* e Procura Sôfrega
    
    Fundamentação teórica:
    - 12-pee-3.pdf, página 15: uma função heurística h(n) representa uma
    estimativa do custo de um percurso desde um nó n até ao nó objetivo
    Esta reflete o conhecimento acerca do domínio do problema. O seu valor
    é independente do percurso até ao nó n, apenas depende do estado associado
    a n e o objetivo
    - P3-iasa-proj.pdf, páginas 14 e 15: os diagramas indicam que heurística é
    utilizada por algoritmos de procura informada e seus respetivos avaliadores
    """
    @abstractmethod
    def h(self, estado):
        """
        Método abstrato que calcula a estimativa heurística do custo restante
        desde um estado até o estado objetivo

        Parâmetros:
        - estado (Estado) - Estado atual do problema a ser avaliado

        Retorno:
        - float - Valor não-negativo representando a estimativa de custo mínimo
          para alcançar o objetivo a partir do estado atual

        Funcionamento:
        - A implementação será feita por parte das classes que utilizem
        heurística

        Fundamentação teórica:
        - 12-pee-3.pdf, página 20: heurísticas admissíveis devem satisfazer 
        0 ≤ h(n) ≤ h*(n), onde h*(n) é o custo real mínimo, ou seja, um percurso
        ótimo
        - 12-pee-3.pdf, página 27: em heurísticas consistentes ou monótonas,
        para cada nó n, o seu sucessor n' e o custo de transição c(n,n'): 
            - h(n) ≤ c(n,n') + h(n'), para qualquer transição n→n'
        """
        pass