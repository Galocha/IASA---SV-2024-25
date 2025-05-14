from agente.controlo_delib.mec_delib import MecDelib
from controlo_delib.modelo.modelo_mundo import ModeloMundo
from controlo_delib.modelo.estado_agente import EstadoAgente

from plan.plan_pee.planeador_pee import PlaneadorPee
from sae.ambiente.ambiente import Ambiente
from sae.agente.transdutor import Transdutor #tem o método percecionar
from sae.defamb import DEF_AMB

def obter_percecao():
    num_amb = 4
    ambiente = Ambiente(DEF_AMB[num_amb])
    transdutor = Transdutor()
    transdutor.iniciar(ambiente)
    return transdutor.percepcionar()

def actualizar_modelo_mundo():
    """
    Teste de atualização do modelo do mundo

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
    doctest.testmod()