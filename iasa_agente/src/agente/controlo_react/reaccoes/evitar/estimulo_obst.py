from ecr.estimulo import Estimulo

class EstimuloObst(Estimulo):
    """
    Classe para representar um estímulo causado pela detecção de obstáculos
    
    Este estímulo é responsável por verificar a presença de obstáculos numa
    direção específica, retornando a intensidade do estímulo detectado
    A classe serve como base para reações dependentes de obstáculos
    """
    def __init__(self, direccao, intensidade = 1):
        """
        Estímulo para deteção direcional de obstáculos
        
        Parâmetros:
        - direccao: Direção a monitorizar (NORTE/SUL/ESTE/OESTE)
        - intensidade: Valor de intensidade quando obstáculo é detectado (1 por padrão)
        
        Fundamentos teóricos baseados nos slides:
        - Deteção direcional de obstáculos (slide 13 do P2-iasa-proj) -> pelo diagrama, esta classe terá que ter como parâmetro
        uma direção para onde o agente se movimentará após contactar com um obstáculo
        - Estímulos com intensidade fixa (slide 7 do 06-arq-react-1) -> "Respostas fixas e predefinidas aos estímulos"
        - Arquitetura de percepção direcional (slide 16 do 07-arq-react-2) -> para evitar obstáculos, o agente poderá evitar
        em qualquer das 4 direções principais
        """
        self.__direccao = direccao #direção privada para verificação
        self.__intensidade = intensidade #intensidade do estímulo quando um obstáculo é detetado

    def detectar(self, percepcao):
        """
        Deteta a presença de obstáculos na direção especificada
        
        Parâmetros:
        - percepcao: Objeto de percepção do ambiente
        
        Retorno:
        - float: Intensidade do estímulo (valor configurado ou 0)
        
        Implementa:
        - Modelo binário de deteção -> caso a intensidade seja 1, há estímulo, caso seja 0, não há estímulo, daí ser binário (1 - true, 0 - falso)
        - Resposta imediata a contacto (slide 2 do 06-arq-react-1) -> o agente aciona logo após haver uma perceção do ambiente, com base em associações entre estímulos e respostas
        - Integração com sistema direcional (slide 16 do 07-arq-react-2) -> para evitar obstáculos, o agente poderá evitar em qualquer das 4 direções principais
        """
        return self.__intensidade if percepcao.contacto_obst(self.__direccao) else 0 # Caso haja contato com um obstáculo na direção dada, é retornada a intensidade definida, caso contrário, retorna 0 (ou seja, nenhum estímulo foi detetado)