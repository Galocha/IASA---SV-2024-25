from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

class AvaliadorSofrega(AvaliadorHeur):
    """
    Implementa um avaliador para a procura sôfrega, que utiliza
    exclusivamente a heurística h(n) para priorizar nós
    Ignora o custo acumulado g(n), focando-se apenas na proximidade 
    estimada ao objetivo

    Fundamentação teórica:
    - 12-pee-3.pdf, página 17: define a procura sôfrega como estratégia que
      minimiza apenas h(n), podendo levar a soluções sub-ótimas
    - P3-iasa-proj.pdf, página 15: diagrama de classes mostra AvaliadorSofrega
      como implementação concreta de AvaliadorHeur
    """
    def prioridade(self, no):
        """
        Calcula a prioridade do nó usando apenas a heurística h(n), 
        caracterizando o comportamento "sôfrego" da procura

        Parâmetros:
        - no (No) - Nó contendo o estado atual, custo acumulado e operador

        Retorno:
        - float - Valor heurístico h(n) que estima o custo restante até o objetivo

        Funcionamento:
        1. Obtém a heurística configurada no avaliador heurística (self._heuristica)
        2. Aplica h(n) = heuristica.h(no.estado) para estimar o custo restante
        3. Ignora completamente o custo acumulado no.custo

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 14: mostra o uso deste avaliador em
        ProcuraSofrega para implementar o algoritmo de procura sôfrega
        """
        return self.heuristica.h(no.estado)