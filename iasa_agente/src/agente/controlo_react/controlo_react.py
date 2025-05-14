from ecr.comportamento import Comportamento
# Importa a base para comportamentos reativos

class ControloReact():
    """
    Classe que implementa o núcleo de controlo reativo de um agente autónomo.
    Conforme o slide 7 do pdf P2-iasa-proj, esta classe representa o módulo central
    que processa percepções e coordena os comportamentos do agente.
    """
    def __init__(self, comportamento):
        """
        Construtor da classe ControloReact
        
        Parâmetros:
        - comportamento: O comportamento principal do agente. Deve ser uma instância de
                        uma subclasse de Comportamento (Reaccao ou ComportComp)
        
        Conforme o slide 7 do pdf P2-iasa-proj, este construtor inicializa o
        controlo reactivo com um comportamento específico, que pode ser:
        - Um comportamento simples (Reaccao direta)
        - Um comportamento composto (ComportComp com hierarquia ou prioridades)
        
        O atributo __comportamento é privado (indicado por dois underscores __), o que
        significa que só deve ser acedido dentro desta classe.
        """
        self.__comportamento = comportamento

    def processar(self, percepcao):
        """
        Método principal que transforma percepções em ações.
        
        Parâmetros:
        - percepcao: A informação sensorial recebida do ambiente. Pode conter dados sobre
                    alvos, obstáculos, etc., conforme o domínio do problema.
        
        Retorno:
        - A ação a ser executada pelo agente (objeto do tipo Accao)
        
        Funcionamento:
        1. Delega o processamento ao comportamento atribuído
        2. O comportamento usa:
           - Prioridades: onde a ação com maior prioridade é selecionada para execução
           - Hierarquia: a organização dos comportamentos é feita numa hierarquia fixa de
           subsunção (supressão e substituição)
           - Combinação de ações: as respostas são combinadas numa única resposta, resultando
           numa única ação
        
        Conforme o slide 6 do pdf 06-arq-react-1, este método implementa o núcleo do
        ciclo percepção-reação-ação característico dos agentes reativos.
        """
        return self.__comportamento.activar(percepcao)