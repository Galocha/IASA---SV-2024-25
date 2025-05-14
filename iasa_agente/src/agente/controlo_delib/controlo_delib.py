from agente.controlo_delib.mec_delib import MecDelib
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo


class ControloDelib():
    """
    Classe ControloDelib, que implementa um controlo deliberativo para agentes autónomos, 
    seguindo os princípios da arquitetura deliberativa.
    Esta componente é responsável por gerar ações baseadas em percepções do ambiente, 
    utilizando processos de raciocínio prático que envolvem deliberação e planeamento

    As componentes do raciocínio prático, como já foi mencionado, são a deliberação
    e o planeamento, onde:
    - Deliberação: decidir o que fazer, resultando em objetivos
    - Planeamento: decidir como fazer, resultando em planos
    """
    def __init__(self, planeador):
        """
        Construtor da classe ControloDelib, onde são iniciados:
        - um modelo de mundo -> representação interna do problema
        - um mecanismo de deliberação -> responsável por deliberar o agente
        - um planeador -> responsável por planear
        - uma lista de objetivos -> lista com os objetivos gerados após deliberação
        - um plano -> plano retornado após planeamento

        Parâmetros:
        - planeador - instância de um planeador que gera um plano

        Para além do planeador, os outros atributos foram iniciados por indicação
        do docente
        """
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__planeador = planeador
        self.__objectivos = None
        self.__plano = None

    def processar(self, percepcao):
        """
        Método que realiza ações perante a perceção obtida, considerando
        também o estado do modelo do mundo

        O processo de tomada de decisão e acção ocorre de forma cíclica, com os
        seguintes passos de processamento:
        1) Observar
        2) Atualizar
        3) Deliberar
        4) Planear
        5) Executar

        Parâmetros:
        - percepcao - informação sensorial do ambiente

        Retorno:
        - accao - ação gerada a partir do processo de tomada de decisão e ação

        Fundamentação teórica:
        - 13-arq-delib.pdf, páginas 13 a 15: o raciocínio prático sustenta o processo
        geral de tomada de decisão que orienta o comportamento do agente, enfrenta problemas
        como a limitação de recursos computacionais e o dinamismo do ambiente, que pode sofrer 
        alterações durante o próprio raciocínio. Assim, é fundamental que este processo 
        permita a reconsideração das opções (objetivos e planos), de forma a integrar possíveis
        mudanças no ambiente que ainda não tenham sido consideradas
        - P4-iasa-proj.pdf, página 3: no diagrama de classes, é percetível a presença deste
        método na classe ControloDelib
        - P4-iasa-proj.pdf, página 6: o fluxograma desta página mostra o correto funcionamento
        deste método, onde o mesmo assimila uma perceção e, caso reconsidere, delibera, planeia
        e executa uma ação. Caso não reconsidere, apenas executa a ação
        """
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()

    
    def __assimilar(self, percepcao):
        """
        Método que atualiza o modelo do mundo (ambiente), com base
        nas perceções do agente

        Parâmetros:
        - percepcao - informação sensorial do ambiente

        Funcionamento:
        - Invoca ModeloMundo.actualizar() para sincronizar o estado interno
        - Marca modelo como alterado caso haja mudanças relevantes

        Fundamentação teórica:
        - 13-arq-delib.pdf, página 13: assimilar neste caso é a atualização do
        modelo do mundo, com base em (novas) perceções
        - P4-iasa-proj.pdf, página 3: no diagrama de classes, este método está
        presente em ControloDelib
        """
        self.__modelo_mundo.actualizar(percepcao)

    
    def __reconsiderar(self):
        """
        Método que determina se é necessário fazer o replaneamento com
        base no estado atual do ambiente

        Retorno:
        - True caso o modelo de mundo tenha sido alterado ou se não existir
        plano de ação

        Fundamentação teórica:
        - 13-arq-delib.pdf, páginas 14 e 15: dá-se a reconsideração de opções, caso
        haja recursos computacionais limitados e mudanças do ambiente durante o 
        raciocínio
        - P4-iasa-proj.pdf, página 3: no diagrama de classes, este método está
        presente em ControloDelib
        """
        return self.__modelo_mundo.alterado or self.__plano == None

    
    def __deliberar(self):
        """
        Método que gera novos objetivos com base no ambiente atual

        Funcionamento:
        - Utiliza MecDelib para determinar objetivos
        - Atualiza lista __objectivos com os objetivos gerados

        Fundamentação teórica:
        - 13-arq-delib.pdf, páginas 11 e 13: a deliberação (raciocínio sobre fins) decide
        o que fazer, gerando objetivos, com base no estado atual do ambiente após
        reconsideração
        - P4-iasa-proj.pdf, página 3: esta classe utiliza o mecanismo de deliberação para 
        deliberar
        """
        self.__objectivos = self.__mec_delib.deliberar()

    
    def __planear(self):
        """
        Método que gera novo plano de ação para alcançar os objetivos atuais
        
        Funcionamento:
        - Se existirem objetivos, invoca planeador para gerar um plano
        - Caso contrário, define plano como None
            
        Fundamentação teórica:
        - 13-arq-delib.pdf, páginas 11 e 13: o planeamento (raciocínio sobre meios)
        decide como fazer, gerando um plano de ação
        - P4-iasa-proj.pdf, página 3: o método está presente na arquitetura
        do ControloDelib
        """
        if self.__objectivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)
        else:
            self.__plano = None


    def __executar(self):
        """
        Método que executa o plano de ação
        
        Retorno:
        - Accao - próxima ação a executar ou None se plano inválido
            
        Funcionamento:
        1. Verifica se existe um plano válido
        2. Obtém o estado atual do mundo
        3. Recupera o operador correspondente do plano
        4. Verifica a existência desse operador
        5. Retorna a ação associada ao operador
        6. Invalida o plano se não houver operação válida (plano = None)
            
        Fundamentação teórica:
        - 13-arq-delib.pdf, páginas 13 e 15: o passo "Executar" serve para
        executar o plano de ação gerado após planeamento
        - P4-iasa-proj.pdf, página 3: o método está presente na classe
        ControloDelib
        """
        if self.__plano:
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)
            if operador:
                return operador.accao
            else:
                self.__plano = None


    def mostrar(self, vista):
        """
        Exibe o estado interno do controlo numa vista (interface gráfica)
        
        Parâmetros:
        - vista - componente de visualização
            
        Funcionamento:
        1. Limpa a vista existente
        2. Mostra o estado atual do modelo do mundo
        3. Se existir, mostra o plano atual
        4. Caso existam objetivos, são marcadas as posições dos mesmos
            
        Fundamentação:
        - P4-iasa-proj.pdf, página 3: método mostrar() presente na arquitetura
        """
        vista.limpar()
        self.__modelo_mundo.mostrar(vista)
        if self.__plano:
            self.__plano.mostrar(vista)
        if self.__objectivos:
            for objectivo in self.__objectivos:
                vista.marcar_posicao(objectivo.posicao)