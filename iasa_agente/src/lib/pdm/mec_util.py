class MecUtil:
    """
    Mecanismo de cálculo de utilidades para Processos de Decisão de Markov (PDM)
    Implementa o algoritmo de Iteração de Valor para calcular a utilidade ótima de cada estado

    Fundamentação teórica (15-pds.pdf):
    - Página 35: cálculo iterativo da utilidade de estado com critério de paragem baseado no valor de delta
    - Página 28: mostra o cálculo iterativo da utilidade
    - Página 26: cálculo da utilidade máxima de um estado com base nas utilidades esperadas das ações possíveis
    """
    def __init__(self, modelo, gama, delta_max):
        """
        Inicializa o mecanismo de cálculo de utilidades

        Parâmetros:
        - modelo: ModeloPDM contendo S(), A(s), T(s,a,s'), R(s,a,s') e suc(s,a)
        - gama: fator de desconto para recompensas futuras (γ ∈ [0,1])
        - delta_max: limiar de convergência para parada do algoritmo

        Fundamentação teórica (15-pds.pdf):
        - Página 16: o fator de desconto representa o impacto do decurso do tempo na 
        valorização de recompensas futuras. O instante temporal em que uma recompensa 
        é recebida influencia de forma significativa a sua contribuição para a utilidade 
        (ou valor) acumulada a longo prazo
        - Página 32: Descreve o critério de parada baseado em delta_max
        """
        self.__gama = gama
        self.__delta_max = delta_max
        self.__modelo = modelo

    def utilidade(self):
        """
        Calcula a utilidade ótima para todos os estados usando Iteração de Valor

        O que é a utilidade?
        - A utilidade U(s) é uma medida de desempenho que reflete o valor acumulado de um estado s,
        considerando as recompensas futuras descontadas ao longo de uma sequência de ações
        - Esta tem um âmbito global, ou seja, a longo prazo, capturando o impacto total das decisões
        futuras a partir do estado atual

        Qual é o objetivo?
        - Avaliar a ação que maximiza o ganho acumulado, considerando incertezas (não determinismo)
        nas transições de estado
        - Serve de base para calcular a política ótima

        Retorno:
        - Dicionário {estado: utilidade} com os valores ótimos

        Processo (15-pds.pdf p.35):
        1. Inicializa U(s) = 0 para todos os estados
        2. Repete até convergência (delta < delta_max):
           a. Atualiza U(s) usando a equação de Bellman:
              U(s) ← maxₐ Σ T(s,a,s')[R(s,a,s') + γU(s')]
           b. Calcula a diferença máxima de atualização (delta)

        Funcionamento (descrição):
        - Inicializa a utilidade de todos os estados a 0 (15-pds.pdf, páginas 28 e 35)
        - Repete as atualizações de utilidade usando a equação de Bellman até que a 
        variação máxima entre iterações (delta) seja inferior ao limiar `delta_max` (15-pds.pdf, página 35)
        - Para cada estado, escolhe a ação com maior utilidade esperada e atualiza `U(s)` com esse valor máximo
        """
        S, A = self.__modelo.S, self.__modelo.A
        U = {s: 0 for s in S()}
        while True: #do while (emulado com ciclo infinito + break)
            U_ant = U.copy() #guardar utilidades anteriores
            delta = 0
            for s in S():
                U[s] = max([self.util_accao(s, a, U_ant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - U_ant[s]))
            if delta <= self.__delta_max:
                break
        return U

    def util_accao(self, s, a, U):
        """
        Calcula a utilidade esperada de executar uma ação num estado

        Parâmetros:
        - s: Estado atual
        - a: Ação a ser avaliada
        - U: Dicionário de utilidades atuais

        Retorno:
        - Valor esperado da utilidade ao executar 'a' em 's'

        Equação (15-pds.pdf p.35):
        Σ T(s,a,s')[R(s,a,s') + γU(s')]

        Funcionamento:
        - Para cada estado sucessor `sn` de `s` ao executar `a`, calcula a soma ponderada
        das recompensas esperadas e das utilidades dos estados sucessores, multiplicadas pela
        probabilidade de transição `T(s,a,sn)`. O resultado é a utilidade esperada da ação `a` em `s`

        Fundamentação teórica (15-pds.pdf):
        - Página 35: algoritmo de utilidade ao executar uma ação num estado,
        com base nas utilidades atuais
        """
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        resultado = sum(T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn]) for sn in suc(s, a))
        return resultado

    #propriedades getter para os fator de desconto e limiar de convergência
    @property
    def gama(self):
        return self.__gama
    
    @property
    def delta_max(self):
        return self.__delta_max