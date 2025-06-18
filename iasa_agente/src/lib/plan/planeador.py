from abc import ABC, abstractmethod

class Planeador(ABC):
    """
    Classe abstrata que define a interface para um planeador em sistemas de agentes deliberativos
    Um planeador é responsável por gerar sequências de ações (planos) para alcançar objetivos,
    utilizando representações internas do ambiente e métodos de raciocínio automático

    Fundamentação teórica:
    - 13-arq-delib.pdf, páginas 7-8: arquitetura deliberativa onde o planeador gera planos 
    baseados em modelos internos (planeamento)
    - 14-plan-pee.pdf, página 2: processo de planeamento automático requer modelo e objetivos
    - P4-iasa-proj.pdf, página 3: diagrama de classes mostra Planeador como parte do controlo 
    deliberativo
    """
    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """
        Método abstrato que define a interface para geração de planos de ação

        Parâmetros:
        - modelo_plan: modelo que representa o ambiente e possíveis transições de estado
        - objetivos: lista de estados que representam os objetivos a serem alcançados

        Retorno:
        - Retorna um objeto Plano que contém a sequência de ações definida 
        para atingir os objetivos

        Funcionamento:
        1. Explora o espaço de estados usando o modelo fornecido
        2. Aplica algoritmos de procura (PEE ou PDM) para encontrar a sequência ótima
        3. Retorna o plano encontrado ou None se não houver solução

        Fundamentação teórica:
        - P4-iasa-proj.pdf, página 9: o diagrama indica que este método é parte da interface
        - 14-plan-pee.pdf, página 2: o planeador deve gerar planos com base no modelo de
        planeamento e nos objetivos
        """
        pass