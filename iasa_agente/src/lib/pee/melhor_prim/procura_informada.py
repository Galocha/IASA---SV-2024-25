from abc import ABC
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim, ABC):
    """
    Classe abstrata que estende de ProcuraMelhorPrim para implementar mecanismos
    de procura informada, que utilizam conhecimento específico do domínio do problema
    através de funções heurísticas

    Fundamentação teórica:
    - 12-pee-3.pdf, página 12: métodos de procura informada são estratégias de
    exploração do espaço de estados que tiram partido do conhecimento do domínio do
    problema, de modo a ordenar a fronteira de exploração
    - P3-iasa-proj.pdf, página 14: o diagrama de classes deste slide, contém a
    informação necessária para a implementação do código estrutural desta classe,
    onde é indicado que esta herda de ProcuraMelhorPrim e é diretamente associada
    à inferface Heuristica, que é passada como parâmetro no método procurar(), já
    que procuras informadas necessitam da função heurística
    - 12-pee-3.pdf, página 25: comparação de métodos de procura que utilizam
    procura informada e procura não informada, onde é percetível que métodos
    de procura que não utilizem heurística, exploram o espaço de estados
    exaustivamente
    """
    def procurar(self, problema, heuristica):
        """
        Executa a procura informada configurando a heurística antes de iniciar

        Parâmetros:
        - problema (Problema) - O problema a ser resolvido, contendo estado inicial,
        operadores e teste de objetivo
        - heuristica (Heuristica) - Função heurística que estima o custo a partir de
        um nó n até ao objetivo

        Retorno:
        - Solucao: Sequência de operadores do estado inicial ao objetivo,
        ou None se nenhuma solução for encontrada

        Funcionamento:
        1. Configura a heurística no avaliador (self._avaliador.heuristica = heuristica)
        2. A partir da superclasse, é feita a execução da procura
        3. Retorna a solução encontrada (ou None)

        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 14: no diagrama é indicada a implementação
        deste método
        """
        self._avaliador.heuristica = heuristica
        return super().procurar(problema)