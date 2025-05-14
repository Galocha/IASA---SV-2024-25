from agente.controlo_react.controlo_react import ControloReact
#from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from agente.controlo_react.reaccoes.recolher import Recolher
from sae.agente.agente import Agente

class AgenteReact(Agente):
    def __init__(self):
        """
        Construtor do Agente Reactivo.
        
        Inicializa um agente com comportamento de exploração e controlo reactivo.
        Conforme o slide 11 do pdf 07-arq-react-2, o controlo reactivo é responsável
        por processar percepções e gerar ações através de um módulo comportamental.
        
        (O comportamento de exploração (Explorar) é instanciado com um limiar de 0.7,
        que representa a intensidade mínima para ativação do comportamento.)

        Instânciou-se o Recolher, após ser feito, pois este já instância explorar.
        """
        super().__init__()  # Inicializa a classe base Agente
        self.__comportamento = Recolher()  # Comportamento privado de exploração
        self.controlo = ControloReact(self.__comportamento)  # Módulo de controlo reactivo

    def executar(self):
        """
        Método principal de execução do agente, implementando o ciclo percepção-decisão-ação.
        
        Este ciclo é fundamental para agentes reactivos:
        1. Percepcionarem: Obter informações do ambiente
        2. Processarem: Transformar percepções em ações
        3. Atuarem: Executar a ação no ambiente
        
        Este método executar, funciona da mesma maneira que o executar do agente da primeira
        parte do projeto.
        """
        percepcao = self._percepcionar()  # Obtém percepção do ambiente (método herdado)
        accao = self.controlo.processar(percepcao)  # Processa percepção para gerar ação
        self._actuar(accao)  # Executa a ação no ambiente (método herdado)