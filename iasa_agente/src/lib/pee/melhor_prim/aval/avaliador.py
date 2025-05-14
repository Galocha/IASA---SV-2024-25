from abc import ABC, abstractmethod

class Avaliador(ABC):
    """
    Interface que possibilita a definição de avaliadores de nós em mecanismos 
    de procura informada. Atua como contrato para implementações concretas como
    AvaliadorAA, AvaliadorSofrega e AvaliadorCustoUnif
    
    Fundamentação teórica:
    - P3-iasa-proj.pdf, página 15: o diagrama de classes mostra Avaliador como 
      classe base para estratégias de avaliação de nós
    - 12-pee-3.pdf, página 17: introduz o conceito de funções de avaliação
      como componente central de algoritmos
    """

    @abstractmethod
    def prioridade(self, no):
        """
        Método abstrato que calcula a prioridade de um nó para expansão
        
        Parâmetros:
        - no (No) - Nó contendo estado, custo acumulado e referência ao operador
        
        Retorno:
        - float - Valor que determina a ordem de processamento na fronteira
        
        Funcionamento:
        - Classes concretas devem implementar a maneira de como a prioridade é calculada,
          seja usando custo acumulado (custo uniforme), heurística (sôfrega) ou ambas (A*)
        
        Fundamentação teórica:
        - 12-pee-3.pdf, página 17: Detalha como diferentes funções de avaliação
          (f(n) = g(n), f(n) = h(n), f(n) = g(n)+h(n)) influenciam o comportamento
          da procura
        - P3-iasa-proj.pdf, página 15: Exige que todos os avaliadores concretos
          implementem este método para integração com mecanismos de procura
        """
        pass