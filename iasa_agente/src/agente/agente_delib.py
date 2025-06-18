from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPee
from sae.agente.agente import Agente
from sae.simulador import Simulador

class AgenteDelib(Agente):
    """
    Implementação de um agente autónomo com arquitetura deliberativa, que:
    - Mantém um modelo interno do mundo
    - Utiliza um mecanismo de deliberação para gerar e selecionar objetivos 
    com base no modelo do mundo
    - Executa ações de forma orientada a objetivos (planeamento)

    Atributos:
    - __controlo: módulo de controlo deliberativo que coordena:
        1) Observação do ambiente
        2) Atualização do modelo do mundo
        3) Reconsideração de opções, devido a prováveis mudanças no ambiente:
            3a) Deliberação de objetivos
            3b) Planeamento de ações
        4) Execução de ações

    Fundamentação teórica:
    - 13-arq-delib.pdf, páginas 12 e 16: numa arquitectura deliberativa de agentes autónomos, 
    o agente possui uma representação interna do ambiente (modelo do mundo), que é continuamente 
    atualizada com base nas perceções obtidas do meio envolvente. Esta representação suporta os 
    mecanismos de raciocínio prático, como a deliberação e o planeamento, que também podem ser 
    influenciados diretamente por eventos percetivos. O controlo deliberativo, organizado de forma modular, 
    é responsável por processar estas percepções e gerar as ações a executar, seguindo um ciclo interno de 
    tomada de decisão e ação
    - O código comportamental foi implementado a partir do já existente AgenteReact,
    adaptando-o para um agente deliberativo
    """
    def __init__(self):
        """
        Inicializa o agente com arquitetura deliberativa básica:
        - Controlo deliberativo com planeador baseado em PEE
        - Capacidades de perceção e atuação herdadas de Agente

        Funcionamento:
        1. Inicializa componente base (Agente)
        2. Configura o ciclo deliberativo com:
           - PlaneadorPEE para geração de planos
           - ControloDelib para gestão do processo
        """
        super().__init__()  # Inicializa a classe base Agente
        self.__controlo = ControloDelib(PlaneadorPee())  # Mecanismo de deliberação

    def executar(self):
        """
        Executa um ciclo completo de perceção-decisão-ação:
        1. Percecionar o ambiente
        2. Processar a perceção para gerar ação
        3. Atualizar a vista (componente gráfica)
        4. Executar a ação no ambiente
        """
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        self._actuar(accao)

if __name__ == "__main__":
    agente = AgenteDelib()
    simulador = Simulador(3, agente, vista_modelo=True)
    simulador.executar()