from abc import ABC, abstractmethod

#classe que representa um estado do problema
#esta classe é abstrata e  (estereótipo <<hashable>>)
#isto segundo o slide 3 do P3-iasa-proj
class Estado(ABC):
    """
    Classe abstrata que representa a unidade fundamental para resolução automática de problemas
    através de procura em espaços de estados. Desenvolvida com base em:

    1. 09-rac-aut.pdf:
       - slide 11: Estados representam configurações possíveis de um problema
       - slide 13: Devem possuir identificação única

    2. 10-pee-1.pdf:
       - slides 5 e 6: Nós como elementos da árvore de procura
       - slides 26 e 27: Necessidade de identificação única para evitar repetições
       - slides 11: Estados como vértices no grafo de espaços de estados

    3. P3-iasa-proj., slide 3:
       - Estereótipo <<hashable>> para eficiência computacional
       - Contém mecanismos de identificação única

    """

    #segundo o diagrama do slide 3 do P3-iasa-proj, este método é abstrato e retorna o valor do estado
    @abstractmethod
    def id_valor(self):
        """
        Método central que materializa o conceito de identificação única de estados
        Deve retornar um valor constante e único para cada configuração distinta do problema

        Fundamentação:
        - 09-rac-aut.pdf, slide 13: Identificação única permite distinguir configurações
        - P3-iasa-proj.pdf, slide 3: <<hashable>> exige este método
        - 10-pee-1.pdf, slide 27: Necessário para memória de explorados
        """
        pass  

    #os próximos métodos foram implementados devido a esta classe conter o estereótipo <<hashable>>, como já foi mencionado
    def __hash__(self):
        """
        Implementação do protocolo Python para objetos hashable, essencial para:
        - Armazenamento eficiente em dicionários e conjuntos
        - Detecção de estados repetidos durante a procura
        - Integração com algoritmos de procura em grafo
        """
        return self.id_valor()

    def __eq__(self, other):
        """
        Implementação de igualdade entre estados, crucial para:
        - Comparação direta de configurações
        - Atualização da fronteira de procura
        """
        if isinstance(other, Estado): #se o outro objeto for uma instância de estado
            return self.__hash__() == other.__hash__() #compara-se os hash de cada instância