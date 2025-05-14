#não se faz import de accao pois não estamos a definir tipos

# Pelo slide 9 do pdf 06-arq-react-1, esta classe irá ser utilizada para definir uma resposta
# a um certo estímulo, isto em termos da ação a realizar e da respetiva prioridade.
class Resposta:
    def __init__(self, accao=None):
        """
        Construtor da classe Resposta
        
        Parâmetros:
        - accao: A ação associada a esta resposta. Pode ser qualquer objeto que represente uma ação
        
        Este método inicializa a resposta com uma ação específica.
        O atributo _accao é protegido (indicado por um underscore _), o que significa que ele é acessível
        a subclasses, mas não deve ser modificado diretamente fora da classe.
        """
        self._accao = accao

    def activar(self, percepcao, intensidade=0):
        """
        Método para ativar a resposta e gerar uma ação com base na percepção e na intensidade do estímulo
        
        Parâmetros:
        - percepcao: A percepção atual do ambiente, que será usada para gerar a ação
        - intensidade: A intensidade do estímulo detectado. O valor padrão é 0, caso nenhum estímulo seja detectado
        
        Retorno:
        - Uma ação a ser executada pelo agente, caso haja uma percepção
        
        Conforme o slide 4 do pdf P2-iasa-proj, o método activar é responsável por processar a percepção
        e a intensidade do estímulo para gerar uma ação correspondente.
        """
        if percepcao is not None: #Só se gera uma ação caso haja percepção
            self._accao.prioridade = intensidade
            return self._accao