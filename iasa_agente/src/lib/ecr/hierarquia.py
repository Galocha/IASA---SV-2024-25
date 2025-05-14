from .comport_comp import ComportComp

class Hierarquia(ComportComp):
    """
    Implementa a seleção de ação por hierarquia fixa (subsunção), onde a primeira ação gerada
    tem sempre prioridade, seguindo o princípio de supressão/substituição

    Fundamentação teórica:
    - 07-arq-react-2.pdf, página 7: em seleções de ação por hierarquia, os comportamentos
    estão organizados numa hierarquia fixa de subsunção
    - 07-arq-react-2.pdf, página 8: a figura descreve a organização hierárquica de comportamentos
    e como a subsunção (suprimir e substituir) funciona
    - P2-iasa-proj.pdf, página 6: o diagrama mostra Hierarquia como especialização de ComportComp
    """
    def seleccionar_accao(self, accoes):
        """
        Seleciona a ação seguindo uma hierarquia pré-definida

        Parâmetros:
        - accoes - Lista ordenada de ações geradas pelos sub-comportamentos,
        onde a primeira é a mais prioritária na hierarquia

        Funcionamento:
        - Seleciona sempre a primeira ação da lista (accoes[0])

        Retorno:
        - Accao - a primeira ação da lista (mais alta na hierarquia)

        Segundo o P2-iasa-proj.pdf, página 6, esta classe contém apenas
        este método, que servirá para selecionar uma ação por hierarquia de
        subsunção de um comportamento composto
        """
        return accoes[0]