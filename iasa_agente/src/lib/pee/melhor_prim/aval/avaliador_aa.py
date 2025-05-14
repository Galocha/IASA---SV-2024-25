from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

class AvaliadorAA(AvaliadorHeur):
    """
    Implementa um avaliador para o algoritmo A* que combina:
    - Custo acumulado do nó (g(n))
    - Estimativa heurística do custo restante (h(n))
    
    Fundamentação teórica:
    - 12-pee-3.pdf, página 17: define a função de avaliação f(n) = g(n) + h(n) como
      a base do algoritmo A*, garantindo valores ótimos quando h(n) é admissível
    - P3-iasa-proj.pdf, páginas 14 e 15: o diagrama de classes mostra AvaliadorAA como
      implementação concreta de AvaliadorHeur para procura informada
    """
    def prioridade(self, no):
        """
        Calcula a prioridade do nó para expansão no algoritmo A*,
        usando a fórmula f(n) = g(n) + h(n), onde:
        - f(n) -> representa uma avaliação do custo da solução através do nó n
        - g(n) -> custo acumulado desde o estado inicial até ao estado n
        - h(n) -> heurística: estimativa do custo para a partir do estado n atingir o estado objetivo
        
        Parâmetros:
        - no (No): Nó da árvore de procura contendo estado, custo acumulado e antecessor.
        
        Retorno:
        - float: Valor da função de avaliação f(n) para o nó.
        
        Funcionamento:
        1. Obtém o custo acumulado do nó (g(n)) através de no.custo
        2. Calcula a heurística h(n) aplicando self.heuristica.h(no.estado)
        3. Retorna a soma g(n) + h(n), que prioriza nós com menor custo total estimado
        
        Fundamentação teórica:
        - 12-pee-3.pdf, página 24: demonstra que f(n) = g(n) + h(n) é ótima se
          h(n) for admissível (nunca passa o custo real)
        - 12-pee-3.pdf, página 26: prova que a consistência de h(n) garante
          que A* nunca reexpanda nós já explorados
        - P3-iasa-proj.pdf, página 14: Mostra a integração deste avaliador
          com a classe ProcuraAA para implementar o algoritmo A* completo
        """
        return no.custo + self.heuristica.h(no.estado)