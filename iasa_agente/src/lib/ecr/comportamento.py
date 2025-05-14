from abc import ABC, abstractmethod 
#abc - Abstract Base Classes: import necessário na criação de classes abstratas ou interfaces
#abstractmethod: decorator usado para definir métodos abstratos que devem ser implementados por subclasses

# Um comportamento é um conjunto de reacções relacionadas entre si no sentido de
# produzirem um resultado específico, por exemplo, evitar um obstáculo.
# Pelo slide 5 do pdf P2-iasa-proj, comportamento é uma interface que define a funcionalidade
# geral de um comportamento, mas não implementa a lógica específica.
# Esta classe herda, então, de ABC.
class Comportamento(ABC):
    @abstractmethod
    def activar(self, percepcao):
        """
        Método abstrato que define a interface para ativar um comportamento com base numa percepção
        
        Parâmetros:
        - percepcao: A percepção atual do ambiente, que será usada para gerar uma ação
        
        Retorno:
        - Uma ação a ser executada pelo agente
        
        Este método deve ser implementado por subclasses concretas de Comportamento.
        Conforme o slide 5 do pdf P2-iasa-proj, o método activar é responsável por
        processar a percepção e gerar uma ação correspondente.
        """
        raise NotImplementedError