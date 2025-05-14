from abc import ABC, abstractmethod #import das bibliotecas necessárias para criação de uma classe abstrata

#definir a classe como abstrata, segundo o diagrama do slide 5 do P3-iasa-proj
class Fronteira(ABC):
    """
    Classe abstrata que define a estrutura básica para fronteiras de exploração
    em algoritmos de procura, conforme especificado em:
    - P3-iasa-proj.pdf (slide 5): Diagrama de classes
    - 10-pee-1.pdf (slide 7, 17 a 24): Implementação em algoritmos de procura
    - 09-rac-aut.pdf (slide 6): Papel na exploração de opções

    A fronteira incluí os nós abertos, ou sejaa, os nós em expansão
    """
    #construtor
    def __init__(self):
        """
        Inicialização da estrutura de dados da fronteira.

        Fundamentação teórica:
        - 10-pee-1.pdf (slide 7): Fronteira mantém nós a expandir
        - P3-iasa-proj.pdf (slide 5): Mostra a necessidade do construtor
        """
        self.iniciar()
    
    #método que serve para iniciar a fronteira
    def iniciar(self):
        """
        Método para iniciar a fronteira

        Fundamentação teórica:
        - 10-pee-1.pdf (slide 18): Necessário entre buscas consecutivas
        - P3-iasa-proj.pdf (slide 5): Método presente no diagrama
        """
        self._nos = []
    
    #método abstrato que serve para inserir um nó na fronteira
    @abstractmethod
    def inserir(self, no):
        """
        Método abstrato para inserir nós à fronteira

        Parâmetros:
        no: No - Nó a ser inserido na fronteira

        Fundamentação teórica:
        - 10-pee-1.pdf (slide 7): Fronteira ordena nós conforme estratégia
        - P3-iasa-proj.pdf (slide 5): Método abstrato da classe
        - 09-rac-aut.pdf (slide 6): Parte do processo de exploração de opções
        """
        pass
    
    # método de remoção de um nó da fronteira
    def remover(self):
        """
        Método para retirar o próximo nó a ser explorado

        Retorno:
        No - Próximo nó a ser expandido

        Fundamentação teórica:
        - 10-pee-1.pdf (slides 18 a 23): Diferentes implementações por estratégia
        - P3-iasa-proj.pdf (slide 5): Parte essencial da interface
        - 09-rac-aut.pdf (slide 6): Seleção de opções na exploração
        """
        return self._nos.pop(0)
    
    @property
    def vazia(self):
        return len(self._nos) == 0
    
