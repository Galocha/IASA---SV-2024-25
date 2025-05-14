from pee.melhor_prim.aval.avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):
    """
    Implementa um avaliador para a procura de custo uniforme, que utiliza
    apenas o custo acumulado do nó (g(n)) para determinar sua prioridade de expansão
    
    Fundamentação teórica:
    - 12-pee-3.pdf, página 19: o custo uniforme é um caso especial de procura melhor-primeiro
      onde f(n) = g(n), garantindo valores ótimos para problemas com custos de ação positivos
    - P3-iasa-proj.pdf, página 13: diagrama de classes mostra AvaliadorCustoUnif como
      implementação concreta para o algoritmo de custo uniforme
    """
    def prioridade(self, no):
        """
        Retorna o custo acumulado do nó como prioridade, implementando a estratégia
        de procura de custo uniforme
        
        Parâmetros:
        - no (No) - Nó da árvore de procura contendo estado, custo acumulado e antecessor
        
        Retorno:
        - float - Custo acumulado g(n) do nó, que determina sua posição na fronteira de procura
        
        Funcionamento:
        - A procura custo uniforme prioriza nós com menor custo acumulado (g(n)), garantindo que o primeiro
        nó objetivo encontrado seja o de menor custo total
        
        Fundamentação teórica:
        - 12-pee-3.pdf, página 17: minimização do custo acumulado até cada
        nó explorado
        - P3-iasa-proj.pdf, página 13: mostra a integração deste avaliador com
          a classe ProcuraCustoUnif para implementar esta procura
        """
        return no.custo