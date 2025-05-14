import sys

print("-----------")
print(sys.path)
print("-----------")

from agente.agente_delib import AgenteDelib
from sae import Simulador
from agente.agente_react import AgenteReact

"""
agente = AgenteReact()

sim = Simulador(1, agente)
sim.executar()
"""

agente_delib = AgenteDelib()

sim = Simulador(4, agente_delib, vista_modelo=True)
sim.executar()