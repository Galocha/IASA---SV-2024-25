from abc import ABC, abstractmethod
#abc - Abstract Base Classes: import necessário na criação de classes abstratas ou interfaces
#abstractmethod: decorator usado para definir métodos abstratos que devem ser implementados por subclasses

# A classe Estimulo é uma interface que define a funcionalidade de deteção de estímulos
# a partir de uma percepção. Conforme o slide 9 do pdf 06-arq-react-1, um estímulo é
# uma informação activadora de uma reacção, ou seja, algo que o agente percebe no ambiente
# e que pode desencadear uma resposta.
class Estimulo(ABC):
    @abstractmethod
    def detectar(self, percepcao):
        """
        Método abstrato para detectar um estímulo a partir de uma percepção
        
        Parâmetros:
        - percepcao: A percepção atual do ambiente, que será analisada para detectar estímulos.
        
        Retorno:
        - Um valor que representa a intensidade ou presença do estímulo detectado.
        
        Este método deve ser implementado por subclasses concretas de Estimulo.
        O método detectar é responsável por processar a percepção e identificar 
        estímulos relevantes, como a presença de um obstáculo, um alvo ou uma fonte de luz.
        """
        raise NotImplementedError