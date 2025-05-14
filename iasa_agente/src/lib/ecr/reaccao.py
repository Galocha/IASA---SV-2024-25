from .comportamento import Comportamento
# Importa a classe Comportamento de um módulo relativo (indicado pelo ponto antes do nome)
# Em Python, imports com ponto (.) são relativos ao package atual, enquanto imports sem ponto são absolutos

class Reaccao(Comportamento):
    def __init__(self, estimulo, resposta):
        """
        Construtor da classe Reaccao
        
        Parâmetros:
        - estimulo: Um objeto do tipo Estimulo, responsável por detectar estímulos no ambiente
        - resposta: Um objeto do tipo Resposta, responsável por gerar uma ação com base no estímulo detectado
        
        Segundo o slide 3 do pdf P2-iasa-proj, uma reacção é uma associação entre um estímulo e uma resposta.
        O construtor inicializa os atributos privados __estimulo e __resposta, que representam essa associação.
        Conforme o diagrama de classes, esses atributos são privados (indicados por dois underscores __), pois 
        encapsulam a lógica interna da reacção.
        """
        self.__estimulo = estimulo
        self.__resposta = resposta

    def activar(self, percepcao):
        """
        Método para ativar a reacção com base na percepção recebida
        
        Parâmetros:
        - percepcao: A percepção atual do ambiente, que será usada para detectar estímulos e gerar ações
        
        Retorno:
        - Uma ação a ser executada pelo agente, ou None se nenhum estímulo for detectado
        
        Conforme o slide 4 do pdf P2-iasa-proj, este método implementa o ciclo percepção-ação:
        - Analisa a intensidade do estímulo usando o método detectar do objeto __estimulo.
        - Se a intensidade for maior que 0, ativa a resposta usando o método activar do objeto __resposta.
        """
        intensidade = self.__estimulo.detectar(percepcao)  # Detecta a intensidade do estímulo
        if intensidade > 0:  # Se houver um estímulo detectado
            return self.__resposta.activar(percepcao, intensidade)  # Ativa a resposta e retorna a ação
        
# Nota: atributo sem underscores: público, atributo com dois underscores: privado , atributo com um underscore: protegido