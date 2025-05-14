from dataclasses import dataclass # Importar o decorador @dataclass que permite criar classes de dados 
from mod.estado import Estado # Importar a classe abstrata Estado da camada de modelo
from mod.operador import Operador  # Importar a classe abstrata Operador

# Definir a classe PassoSolucao como uma dataclass, gerando automaticamente métodos úteis como __init__ e __repr__
@dataclass 
class PassoSolucao:
    """
    Representa um passo individual em uma sequência de solução para problemas de
    raciocínio automático, conforme definido em:

    1. P3-iasa-proj.pdf (slide 5):
       - Componente da classe Solucao
       - Armazena um estado e o operador que levou a ele

    2. 10-pee-1.pdf (slide 13 e 15):
       - Elemento da sequência que compõe uma solução completa
       - Captura a relação estado-operador no caminho solução
    """
    estado: Estado # Atributo que representa o estado atingido neste passo da solução
    operador : Operador # Atributo que representa o operador que levou a este estado a partir do anterior