from plan.plano import Plano

class PlanoPEE(Plano):
    """
    Implementação concreta de Plano para resultados de Procura em Espaço de Estados (PEE)
    Armazena e gerencia a execução de uma sequência de passos (percurso) que conectam
    o estado inicial ao um objetivo

    Atributos:
    - __passos: lista privada de tuplos (estado, operador) que compõem o plano

    Fundamentação teórica:
    - 14-plan-pee.pdf, página 3: um percurso num espaço de estados é uma sequência de passos
    estado-operador, onde o operador é uma ação que transforma um estado em outro. Os operadores,
    neste caso, são deslocamentos do agente no ambiente entre um estado e o seu sucessor
    - P4-iasa-proj.pdf, página 9: PlanoPEE depende da interface Solucao para o seu correto
    funcionamento
    """
    def __init__(self, solucao):
        """
        Inicializa o plano a partir de uma solução encontrada por um algoritmo de PEE
        (procura informada)

        Parâmetros:
        - solucao: sequência de passos que constitui a solução

        Funcionamento:
        - Armazena internamente a sequência de passos da solução
        - Cada passo contém um estado e o operador que leva ao sucessor

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 9: construtor PlanoPEE recebe Solucao (esta classe
        depende da interface Solucao)
        - 14-plan-pee.pdf, página 4: a solução é o percurso que leva do estado inicial
        ao objetivo, e é representada como uma sequência de passos (plano de ação)
        """
        self.__passos = [passo for passo in solucao]
    
    @property
    def dimensao(self):
        """
        Retorna a dimensão do plano, ou seja, o número de passos que
        o agente tem que executar desde o estado inicial até ao objetivo
        """
        return len(self.__passos)
    
    def obter_accao(self, estado):
        """
        Obtém a próxima ação a executar para o estado atual, consumindo o passo correspondente

        Parâmetros:
        - estado: estado atual do agente para verificação de consistência

        Retorno:
        - Operador: próxima ação a executar

        Funcionamento:
        1. Verifica se ainda existem passos a fazer
        2. Compara o estado do próximo passo com o estado atual
        3. Se coincidirem, remove o passo da lista e retorna o seu operador
        4. Caso contrário, retorna None (possível inconsistência)

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 9: este método, presente no UML, é a realização do
        contrato da interface Plano
        - O código aqui presente foi indicado pelo docente
        """
        if self.__passos:
            passo = self.__passos.pop(0)
            if passo.estado == estado:
                return passo.operador
            
    def mostrar(self, vista):
        """
        Visualiza o plano através de uma interface gráfica

        Parâmetros:
        - vista: componente de visualização com métodos de renderização

        Funcionamento:
        - Para cada passo no plano, mostra um vetor que representa:
            - Posição (do estado)
            - Orientação (do operador)
        - Usa os métodos de visualização fornecidos pela vista

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 9: método mostrar() presente em PlanoPEE.
        Também é a realização do contrato da interface Plano
        - Tal como o método obter_accao(), o código comportamental foi indicado pelo 
        professor
        """
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)
