from ecr.comportamento import Comportamento
from sae import Avancar, Rodar, Direccao
import random

# Classe que implementa o comportamento de explorar que é um comportamento de reação
class Explorar(Comportamento):
    """
    Classe que representa o comportamento de explorar

    Este comportamento permite ao agente realizar movimentos aleatórios, alternando entre
    avançar ou rodar para uma direção aleatória, dependendo de uma probabilidade configurada

    Fundamentos teóricos:
    - Arquitetura Reativa (Slides 3 e 13, "P2-iasa-proj.pdf"): Utiliza estímulos e ações como base para comportamentos reativos
    - Hierarquia (Slide 7, "07-arq-react-2.pdf"): Destaca como comportamentos simples podem ser integrados em hierarquias maiores
    """
    def __init__(self, prob_rotacao):
        """
        Inicializa o comportamento de exploração com uma probabilidade de rotação

        Parâmetros:
        prob_rotacao (float): Representa a probabilidade de o agente realizar a ação de rodar
                              em vez de avançar, variando de 0 a 1

        Funcionamento:
        - Cria uma lista de direções possíveis (`Direccao`) que o agente pode escolher
        - Configura a probabilidade de rotação, que determina o comportamento aleatório
        """
        self.__prob_rotacao = prob_rotacao # Define a probabilidade de o agente realizar a rotação
        self.__direccoes = list(Direccao) # Cria uma lista com as direções possíveis

    def activar(self, percepcao):
        """
        Ativa o comportamento de explorar baseado em movimento aleatório

        Parâmetros:
        percepcao (objeto): Informação do ambiente percebida pelo agente
                            (Não é utilizada diretamente neste comportamento, mas mantida
                            para garantir o contrato da classe base `Comportamento`)

        Funcionamento:
        - Gera um número aleatório entre 0 e 1 (`movimento`) para decidir a próxima ação do agente
        - Caso o número gerado seja menor que a probabilidade configurada (`prob_rotacao`):
          - Escolhe uma direção aleatória e retorna a ação de rodar para essa direção
        - Caso contrário:
          - Retorna a ação de avançar

        Fundamentos teóricos:
        - Slide 8 (06-arq-react-1.pdf): Movimentos aleatórios são uma parte essencial da exploração
        - Slide 14 (07-arq-react-2.pdf): Mostra como movimentos aleatórios podem ser utilizados em hierarquias compostas de comportamentos
        """
        movimento = random.random() # Gera um valor aleatório entre 0 e 1
        if movimento < self.__prob_rotacao:
            direccao_aleatoria = random.choice(self.__direccoes) # Escolhe aleatóriamente um elemento da lista direccoes
            accao = Rodar(direccao_aleatoria) # Configura a ação de rodar na direção escolhida
            return accao # Retorna a ação de rodar para a direção escolhida
        else:
            accao = Avancar() # Configura a ação de avançar
            return accao # Retorna a ação de avançar caso o movimento seja maior que a probabilidade de rotação