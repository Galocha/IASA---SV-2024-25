from agente.controlo_delib.mec_delib import MecDelib
from controlo_delib.modelo.modelo_mundo import ModeloMundo
from controlo_delib.modelo.estado_agente import EstadoAgente

from plan.plan_pee.planeador_pee import PlaneadorPee
from sae.ambiente.ambiente import Ambiente
from sae.agente.transdutor import Transdutor #tem o método percecionar
from sae.defamb import DEF_AMB

# ---------------------------------------
# Testes de integração do mecanismo de deliberação e planeamento
#
# Fundamentação teórica:
# - P4-iasa-proj.pdf, página 3: demonstra a arquitetura deliberativa, incluindo
#   os módulos de perceção, modelo do mundo, deliberação e planeamento
# - Os métodos deste ficheiro simulam o ciclo de funcionamento de um agente
#   deliberativo, testando a atualização do modelo do mundo, a geração de
#   objetivos e a criação de planos
# ---------------------------------------

def obter_percecao():
    """
    Obter perceção do ambiente 

    Fundamentação teórica:
    - O agente obtém perceções do ambiente através do transdutor, 
    que converte o estado do ambiente em informação sensorial
    - Este método simula a perceção inicial do agente num ambiente específico

    Retorno:
    - Percepcao: objeto com a perceção sensorial do ambiente
    """
    num_amb = 4
    ambiente = Ambiente(DEF_AMB[num_amb])
    transdutor = Transdutor()
    transdutor.iniciar(ambiente)
    return transdutor.percepcionar()

def actualizar_modelo_mundo():
    """
    Teste de atualização do modelo do mundo

    Fundamentação teórica:
    - O modelo do mundo é atualizado com base nas perceções do ambiente, 
    permitindo ao agente manter uma representação interna do estado do ambiente

    Retorno:
    - ModeloMundo: modelo atualizado após assimilar a perceção

    >>> modelo_mundo = actualizar_modelo_mundo()
    >>> modelo_mundo.alterado
    True

    >>> estado = modelo_mundo.obter_estado()
    >>> estado.posicao
    (0, 0)

    >>> estados = modelo_mundo.obter_estados()
    >>> len(estados)
    671

    >>> operadores = modelo_mundo.obter_operadores()
    >>> len(operadores)
    4

    >>> estado = EstadoAgente((28, 9))
    >>> modelo_mundo.obter_elemento(estado)
    <Elemento.ALVO: 'A'>
    """
    percecao = obter_percecao() #obter a perceção
    modelo_mundo = ModeloMundo() #instânciar o modelo do mundo
    modelo_mundo.actualizar(percecao) #atualizar o modelo perante a perceção
    return modelo_mundo #retornar o modelo atualizado

def gerar_objectivos():
    """
    Teste de geração de objetivos pelo mecanismo de deliberação

    Fundamentação teórica:
    - A deliberação é responsável por decidir o que fazer, 
    gerando objetivos a partir do modelo do mundo

    Retorno:
    - list: lista de objetivos (estados alvo) ordenados pela distância até ao agente

    >>> objectivos = gerar_objectivos()
    >>> len(objectivos)
    3
    """
    modelo_mundo = actualizar_modelo_mundo()
    mec_delib = MecDelib(modelo_mundo)
    return mec_delib.deliberar()

def gerar_plano():
    """
    Teste de geração de plano

    Fundamentação teórica:
    - O planeador recebe o modelo do mundo e os objetivos, 
    gerando um plano de ações para atingir os fins deliberados

    Retorno:
    - Plano: plano de ações para atingir os objetivos

    >>> plano = gerar_plano()
    >>> plano.dimensao
    37
    """
    planeador = PlaneadorPee()
    modelo_mundo = actualizar_modelo_mundo()
    objectivos = gerar_objectivos()
    plano = planeador.planear(modelo_mundo, objectivos)
    return plano

# Executar teste
if __name__ == "__main__":
    import doctest
    doctest.testmod() #executar os testes a partir das instruções de docstring