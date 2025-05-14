from sae import Rodar
from ecr.resposta import Resposta

class RespostaEvitar(Resposta):
    """
    Classe que representa a resposta do agente ao evitar obstáculos

    Este comportamento verifica a presença de obstáculos na direção atual do agente
    Caso um obstáculo seja detectado, o agente irá rodar (mudar sua direção) como forma de evitar a colisão
    
    Fundamentos teóricos:
    - Reacções a Estímulos (Slide 13, "P2-iasa-proj.pdf"): Detalha o processo de ativação de respostas reativas em reação a estímulos
    - Evitar Obstáculos (Slides 12 e 13, "P2-iasa-proj.pdf"): Explica como estímulos relacionados a obstáculos são utilizados para orientar respostas
    - Arquitetura Reactiva (Slides 10 e 14, "07-arq-react-2.pdf"): Mostra como as respostas são organizadas em comportamentos reativos e hierarquias
    - Rodar como Resposta (Slide 8, "06-arq-react-1.pdf"): A mudança de direção é uma das ações primárias do agente na exploração
    """
    def activar(self, percepcao, intensidade = 0):
        """
        Ativa a resposta de evitar obstáculos com base na perceção do agente

        Parâmetros:
        percepcao (objeto): Contém informações do ambiente percebido pelo agente
        intensidade (float): Representa a intensidade do estímulo associado ao comportamento

        Funcionamento:
        - A direção atual do agente é obtida através de `percepcao.direccao`
        - Se for detectado um obstáculo na direção atual (`contacto_obst`), o agente irá calcular uma nova direção,
          usando `rodar` como mecanismo para desviar do obstáculo
        - A ação de rodar é configurada e ativada utilizando a classe `Rodar`
        """
        dir_agente = percepcao.direccao #obtém a direção atual do agente

        if percepcao.contacto_obst(dir_agente): #verifica se há obstáculo na direção atual
            dir_resposta = dir_agente.rodar() #calcula uma nova direção para desviar do obstáculo
            self._accao = Rodar(dir_resposta) #configura a ação de rodar para a nova direção
            return super().activar(percepcao, intensidade) #ativa a resposta configurada
