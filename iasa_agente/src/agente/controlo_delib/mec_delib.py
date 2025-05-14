from sae.ambiente.elemento import Elemento

class MecDelib():
    """
    Implementação do mecanismo de deliberação para agentes deliberativos
    Responsável por gerar e selecionar objetivos com base no modelo do mundo atual
    
    Funcionamento:
    - Analisa o modelo do mundo para identificar possíveis objetivos (estados alvo)
    - Seleciona os objetivos mais relevantes com base em critérios de proximidade
    
    Fundamentação teóricas:
    - 13-arq-delib.pdf, página 11 e 13: um dos passos do processo de tomada
    de decisão e ação é o raciocínio sobre fins, ou seja, a deliberação. Esta
    decide o que fazer consoante o estado do ambiente, gerando os objetivos 
    a alcançar pelo agente
    - P4-iasa-proj.pdf, página 3: esta classe está presente na arquitetura da
    do diagrama de classes da package controlo_delib
    """
    def __init__(self, modelo_mundo):
        """
        Inicializa o mecanismo de deliberação com um modelo de mundo
        
        Parâmetros:
        - modelo_mundo (ModeloMundo) - representação interna do ambiente 
        que contém os estados e elementos

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 3: segundo a arquitetura, o construtor
        desta classe apenas tem como parâmetro o modelo de mundo atual
        """
        self.__modelo_mundo = modelo_mundo
    
    def deliberar(self):
        """
        Método principal que coordena o processo de geração e seleção de objetivos

        Retorno:
        - lista - lista ordenada de objetivos (estados alvo) ou None se nenhum for
        encontrado

        Funcionamento:
        1. Gera objetivos
        2. Seleciona e ordena os objetivos mais relevantes

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 3: o mecanismo de deliberação é responsável
        por deliberar, ou seja, decide o que fazer e gera objetivos
        - Este método foi implementado segundo as informações dadas pelo
        docente em aula
        """
        objetivos = self.__gerar_objetivos()
        if objetivos:
            return self.__selecionar_objetivos(objetivos)
    
    def __gerar_objetivos(self):
        """
        Gera uma lista de possíveis objetivos analisando o modelo do mundo
        
        Retorno:
        - lista - estados que contêm elementos do tipo Elemento.ALVO
            
        Funcionamento:
        - Itera sobre todos os estados do modelo do mundo
        - Filtra apenas os estados que contêm elementos ALVO (objetivos)
            
        Fundamentação teórica:
        - Implementado em aula consoante as informações dadas pelo
        professor
        """
        return[estado for estado in self.__modelo_mundo.obter_estados()
               if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
    
    def __selecionar_objetivos(self, objetivos):
        """
        Ordena os objetivos por proximidade ao agente
        
        Parâmetros:
        - lista de objetivos: lLista de estados alvo a serem ordenados
            
        Retorno:
        - lista de objetivos: objetivos ordenados por distância crescente
            
        Funcionamento:
        - Utiliza a função distancia() do modelo do mundo como chave de ordenação
        - Estados mais próximos têm prioridade
            
        Fundamentação teórica:
        - 13-arq-delib.pdf, página 9: durante o processo de raciocínio automático,
        existem dois tipos de atividades principais, a exploração das melhores opções
        possíveis e a avaliação das mesmas, percebendo quais são as melhores. Na avaliação
        de opções, é avaliado o custo. Sendo o custo melhor quanto menor for, isso significa que
        a distância até a um alvo também tem que ser a menor
        - O código aqui presente foi indicado pelo docente
        """
        objetivos.sort(key= self.__modelo_mundo.distancia)
        return objetivos