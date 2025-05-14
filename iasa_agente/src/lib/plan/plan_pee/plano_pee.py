from plan.plano import Plano

class PlanoPEE(Plano):
    
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao]
    
    @property
    def dimensao(self):
        """
        Retorna a dimensão do plano, ou seja, o número de passos
        """
        return len(self.__passos)
    
    def obter_accao(self, estado):
        if self.__passos:
            passo = self.__passos.pop(0)
            if passo.estado == estado:
                return passo.operador
            
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)
