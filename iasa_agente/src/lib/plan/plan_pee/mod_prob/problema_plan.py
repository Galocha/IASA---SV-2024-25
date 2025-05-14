from mod.problema import Problema

class ProblemaPlan(Problema):
    def __init__(self, modelo_plan, estado_final):
        """
        Inicializa o problema de planeamento com um modelo de mundo e um estado final

        Parâmetros:
        - modelo_mundo - referência ao modelo do ambiente
        - estado_final - estado alvo que se pretende alcançar
        """
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final
    
    def objectivo(self, estado):
        """
        Verifica se o estado atual é o estado final

        Parâmetros:
        - estado - estado atual do agente

        Retorno:
        - bool - True se o estado atual é o estado final, False caso contrário
        """
        return estado == self.__estado_final