from ecr.comportamento import Comportamento
from ecr.resposta import Resposta
from sae.agente.avancar import Avancar


class ExplorarComMem(Comportamento):
    """
    Classe de comportamento para exploração com memória

    Este comportamento permite ao agente explorar o ambiente de forma eficiente,
    garantindo que ele não visite frequentemente as mesmas posições
    A memória é utilizada para registar posições já exploradas, e uma estratégia 
    de descarte é aplicada quando o limite de memória é atingido
    """
    def __init__(self, memoria_max=100):
        """
        Inicializa o comportamento ExplorarComMem com uma memória limitada

        Parâmetros:
        memoria_max (int): Número máximo de estados (posição e direção) que
                           o agente pode armazenar em memória (100 por padrão)

        Atributos:
        - self._memoria: Lista que armazena as situações já visitadas pelo agente
        - self._memoria_max: Limite máximo de itens que a memória pode conter
        - self._resposta: Define a resposta padrão do comportamento
        """
        self._memoria = []
        self._memoria_max = memoria_max
        self._resposta = Resposta(Avancar())
    
    def activar(self, percepcao):
        """
        Ativa o comportamento de exploração com memória baseada na perceção atual do agente

        Parâmetros:
        percepcao (objeto): Contém informações sobre a posição e direção do agente no ambiente

        Lógica:
        1. A situação atual (posição e direção) é extraída da perceção
        2. Se a situação não estiver na memória, é considerada uma nova situação:
           - Adiciona-se à memória para evitar revisitas frequentes
           - Remove-se a memória mais antiga, caso o limite seja atingido, para manter o espaço
        3. Ativa a resposta padrão do agente (avançar) com base na perceção

        Retorno:
        Resposta: A ação do agente para a perceção atual (neste caso, avançar)
        """
        situacao_atual = (percepcao.posicao, percepcao.direccao) #extrai a posição e direção atuais do agente
        if situacao_atual not in self._memoria: #caso a situação atual do agente não exista na memória, significa que é uma situação nova
            self._memoria.append(situacao_atual) #adicionar à memória a situação
            if len(self._memoria) > self._memoria_max: #se a memória estiver cheia
                self._memoria.pop(0) #elimina-se a primeira memória
                #este if serve para o agente não estar constantemente no mesmo sitio
            return self._resposta.activar(percepcao) #ativa a resposta