from abc import ABC, abstractmethod
from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.mec_proc.no import No

class ProcuraGrafo(MecanismoProcura, ABC):
    """
    Classe abstrata que estende MecanismoProcura para implementar procura em grafos,
    evitando estados repetidos através de uma memória de nós explorados
    
    Fundamentação teórica:
    - 10-pee-1.pdf, página 27: existe a necessidade de haver memória de nós explorados
      para evitar ciclos em problemas com ações reversíveis
    - P3-iasa-proj.pdf, página 8: o diagrama de classes mostra ProcuraGrafo como base
      para mecanismos que necessitam de eliminação de estados repetidos
    """
    def _iniciar_memoria(self):
        """
        Inicializa as estruturas de memória para procura em grafos
        
        Funcionamento:
        - Chama a inicialização da superclasse (MecanismoProcura) para preparar a fronteira
        - Cria um dicionário vazio para armazenar nós explorados (estados já visitados)
        
        Fundamentação teórica:
        - 10-pee-1.pdf, página 27: estruturas de memória
          para nós abertos (fronteira) e fechados (explorados)
        - P3-iasa-proj.pdf, página 8: Mostra a relação entre MecanismoProcura e
          a necessidade de estruturas adicionais para procura em grafos
        """
        super()._iniciar_memoria()
        self._explorados = {}
    
    def _memorizar(self, no):
        """
        Armazena um nó na memória de procura, verificando se deve ser mantido
        
        Parâmetros:
        - no (No): Nó a ser memorizado
        
        Funcionamento:
        1. Verifica se o nó deve ser mantido através do método abstrato _manter(no)
        2. Se sim, adiciona o nó à fronteira (super()._memorizar(no))
        3. Armazena o nó no dicionário de explorados, indexado pelo estado
        
        Fundamentação teórica:
        - 10-pee-1.pdf, página 28: pseudocódigo mostra a inserção condicional
          de nós na fronteira e memória de explorados
        """
        if self._manter(no):
            super()._memorizar(no)
            self._explorados[no.estado] = no
        else:
            No.nos_repetidos += 1
    
    @abstractmethod
    def _manter(self, no):
        """
        Método abstrato que define critérios para manter ou descartar um nó
        
        Parâmetros:
        - no (No): Nó a ser avaliado
        
        Retorno:
        - bool: True se o nó deve ser mantido, False caso contrário
        
        Fundamentação teórica:
        - P3-iasa-proj.pdf, página 12: especifica que a implementação concreta
          deste método varia conforme o algoritmo
        """
        pass