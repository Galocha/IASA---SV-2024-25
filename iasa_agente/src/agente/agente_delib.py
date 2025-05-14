from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPee
from sae.agente.agente import Agente

class AgenteDelib(Agente):
    """
    Classe que representa um agente deliberativo
    Este agente é responsável por tomar decisões com base em um modelo do mundo
    e um mecanismo de deliberação
    """

    def __init__(self):
        """
        Inicializa o agente deliberativo com um modelo do mundo e um mecanismo de deliberação

        Parâmetros:
        - modelo_mundo (ModeloMundo) - representação interna do ambiente 
        que contém os estados e elementos
        """
        super().__init__()  # Inicializa a classe base Agente
        self.__controlo = ControloDelib(PlaneadorPee())  # Mecanismo de deliberação

    def executar(self):
        percepcao = self._percepcionar()
        accao = self.__controlo.processar(percepcao)
        self.__controlo.mostrar(self.vista)
        self._actuar(accao)