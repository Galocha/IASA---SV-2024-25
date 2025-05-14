from abc import ABC
from pee.melhor_prim.aval.avaliador import Avaliador

class AvaliadorHeur(Avaliador, ABC):
    """
    Classe abstrata intermediária que estende Avaliador para incorporar
    funcionalidades relacionadas a heurísticas. Serve como base para
    avaliadores que utilizam funções heurísticas
    
    Fundamentação teórica:
    - P3-iasa-proj.pdf, página 15: o diagrama de classes mostra AvaliadorHeur
    como classe pai de AvaliadorAA e AvaliadorSofrega
    - 12-pee-3.pdf, página 16: menciona como h(n) (heurística) é uma maneira
    de avaliação de custo, daí ser necessário a criação de um avaliador
    """
    def __init__(self):
        """
        Inicializa o avaliador com heurística None, que deve ser definida
        posteriormente via property heuristica
        
        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 15: o diagrama indica que esta classe
        não contém construtor e que a heurística é adicionada em tempo de execução
        """
        self._heuristica = None

    #A propriedade e setter abaixo foram implementados porque no diagrama da página 15 do P3-iasa-proj, 
    #diz que AvaliadorHeur tem um atributo read/write
    @property
    def heuristica(self):
        """
        Getter para a heurística associada ao avaliador
        
        Retorno:
        - Heuristica - Objeto que implementa o método h(estado) para cálculo
        da estimativa heurística
        """
        return self._heuristica
    
    @heuristica.setter
    def heuristica(self, h):
        """
        Setter para configurar a heurística do avaliador
        
        Parâmetros:
        - h (Heuristica) - Objeto que implementa o método h(estado)
        """
        self._heuristica = h