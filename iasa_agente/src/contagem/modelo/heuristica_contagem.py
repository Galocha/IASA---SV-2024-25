from pee.melhor_prim.heuristica import Heuristica

class HeuristicaContagem(Heuristica):
    """
    Implementação de uma heurística para problemas de contagem, onde o objetivo é alcançar
    um valor final a partir de um valor inicial através de incrementos
    
    Fundamentação teórica:
    - 12-pee-3.pdf, página 20: heurísticas admissíveis são aquelas que nunca estimam o custo acima
      do custo real até ao objetivo, garantindo que algoritmos como A*, tenham resultados ótimos
    - 12-pee-3.pdf, página 22: heurísticas baseadas em distância absoluta são consistentes quando 
      o custo de transição ≥ 1
    - P3-iasa-proj.pdf, página 15: Diagrama de classes mostra a integração da heurística
      com avaliadores como AvaliadorAA e AvaliadorSofrega
    """
    def __init__(self, valor_final):
        """
        Inicializa a heurística com o valor objetivo final
        
        Parâmetros:
        - valor_final (int) - Valor alvo que define o estado objetivo
        
        Fundamentação teórica:
        - 10-pee-1.pdf, página 29: Destaca a necessidade de armazenar informação do objetivo
          para cálculo de heurísticas em problemas de planeamento.
        """
        super().__init__()
        self.valor_final = valor_final

    def h(self, estado):
        """
        Calcula a estimativa heurística do custo restante usando distância linear
        
        Parâmetros:
        - estado (Estado): Estado atual com atributo 'valor' (int)
        
        Retorno:
        - int: Distância absoluta |valor_final - valor_atual|
        
        Fundamentação teórica:
        - 12-pee-3.pdf, página 27: esta heurística é consistente (monótona),
          pois satisfaz h(n) ≤ c(n,n') + h(n') para qualquer transição n → n'
          (onde n é um nó e n' é o seu sucessor)
        - P3-iasa-proj.pdf, página 14: mostra o uso desta heurística em ProcuraAA,
          onde f(n) = g(n) + h(n) deve usar uma h(n) admissível.
        """
        return abs(self.valor_final - estado.valor)