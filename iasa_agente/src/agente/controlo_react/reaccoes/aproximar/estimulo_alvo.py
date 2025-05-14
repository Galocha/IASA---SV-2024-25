from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

class EstimuloAlvo(Estimulo):
    def __init__(self, direccao, gama=0.9):
        """
        Construtor do Estímulo para detecção de alvos numa direção específica
        
        Parâmetros:
        - direccao: Direção a monitorizar (NORTE, SUL, ESTE, OESTE)
        - gama: Fator de decaimento da intensidade com a distância (por padrão, 0.9)
        
        Isto pelo diagrama de classes do slide 12 do P2-iasa-proj (EstimuloAlvo)
        e pelo conceito de estímulos direcionais do slide 16 do 07-arq-react-2.
        """
        self.__direccao = direccao  # Atributo privado para a direção
        self.__gama = gama          # Atributo privado para o fator de decaimento

    def detectar(self, percepcao):
        """
        Método para detectar a presença e intensidade de um alvo na direção configurada.
        
        Parâmetros:
        - percepcao: Informação do ambiente (implementa interface de acesso por direção)
        
        Retorno:
        - float: Intensidade do estímulo (0 se não houver alvo)
        
        Implementa o mecanismo de detecção descrito:
        - Slide 3 do P2-iasa-proj (método detectar da classe Estimulo)
        - Slide 12 do P2-iasa-proj (EstimuloAlvo com direção e gama)
        - Slide 7 do 06-arq-react-1 (associação estímulo-resposta)
        """
        elemento, distancia, _ = percepcao[self.__direccao]  # O "_" ignora dados não usados
        # Calcula intensidade com decaimento exponencial (gama^distancia)
        intensidade = self.__gama ** distancia if elemento == Elemento.ALVO else 0
        return intensidade