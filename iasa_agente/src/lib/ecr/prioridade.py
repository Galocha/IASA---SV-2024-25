from .comport_comp import ComportComp

class Prioridade(ComportComp):
    """
    Implementa a seleção de ação por prioridade dinâmica, onde cada ação possui
    um valor de prioridade calculado em tempo real (varia ao longo da execução)

    Fundamentação teórica:
    - 07-arq-react-2.pdf, página 9: na seleção de ações por prioridade, estas são
    selecionadas de acordo com uma prioridade associada que varia ao longo do tempo
    - P2-iasa-proj.pdf, página 6: o diagrama de classes indica que Prioridade
    herda de ComportComp
    - 07-arq-react-2.pdf, página 17: no exemplo do Agente Prospector, este vai usar
    a seleção de ação por prioridade, que produz a ação de aproximação ao alvo mais
    próximo dele em função das prioridades
    """
    def seleccionar_accao(self, accoes):
        """
        Seleciona a ação com maior prioridade

        Parâmetros:
        - accoes - lista de ações com atributo 'prioridade' preenchido

        Retorno:
        - Maior elemento da lista de ações, sendo que a chave de avaliação é a prioridade da ação,
        ou seja, retorna a ação com maior valor no atributo prioridade

        Funcionamento:
        - Seleciona a ação com maior valor de prioridade usando max()
        """
        return max(accoes, key=lambda accao: accao.prioridade)