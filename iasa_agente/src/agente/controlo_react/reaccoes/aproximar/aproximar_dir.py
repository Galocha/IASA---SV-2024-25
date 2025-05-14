from ecr.reaccao import Reaccao
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from .estimulo_alvo import EstimuloAlvo

class AproximarDir(Reaccao):
    """
        Construtor da classe AproximarDir
        
        Parâmetros:
        - direccao: Direção para aproximação do alvo (NORTE, SUL, ESTE, OESTE)
        
        Conforme o slide 12 do P2-iasa-proj, esta classe implementa uma reação direcional
        para aproximação de alvos, seguindo o padrão estímulo-resposta:
        - Estímulo: EstimuloAlvo (detecta alvos na direção especificada)
        - Resposta: RespostaMover (gera ação de movimento na direção especificada)
        
        Esta classe relaciona-se com o diagrama do slide mencionado acima
        e com o conceito de comportamentos direcionais do slide 16, do pdf 07-arq-react-2 (Agente Prospector).
        """
    def __init__(self, direccao):
        super().__init__(
            EstimuloAlvo(direccao), # Estímulo específico para detetar alvos na direção
            RespostaMover(direccao) # Resposta específica para mover na direção
        )