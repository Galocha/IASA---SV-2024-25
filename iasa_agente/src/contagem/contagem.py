from modelo.heuristica_contagem import HeuristicaContagem
from modelo.problema_contagem import ProblemaContagem
from pee.larg.procura_larg import ProcuraLargura
from pee.mec_proc.no import No
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.prof.procura_prof import ProcuraProfundidade
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim

valor_inicial = 0
valor_final = 20
incrementos = [5, 1, 6, 9, 6]

problema = ProblemaContagem(valor_inicial, valor_final, incrementos)

#teste procura em profundidade
#mec_proc = ProcuraProfundidade()
#solucao = mec_proc.procurar(problema)

"""
Dimensão: 4
Custo: 144
Estado: 0
Operador: 6
Estado: 6
Operador: 6
Estado: 12
Operador: 6
Estado: 18
Operador: 6
Nós processados: 21
Nós memória: 21

-> Cmemoria = b*d, onde o b - fator de ramificação e o d - profundidade
-> 21 = b*4 <=> b = 21/4

custo elevado: 6² + 6² + 6² + 6² = 144
Explicação:
- Como esta procura usa o método LIFO (Last in, First out), penso que o incremento 6 esteja a ser utilizado por ser o último da lista (cheguei a testar com outros
valores, pois o 6 está duplicado na lista, e realmente está a ser usado o último incremento)
- A profundidade desta solução é 4, ou seja, a dimensão do percurso desde o estado inicial até ao objetivo foi 4, pois a árvore expandiu-se 4 vezes
- Como o número de nós processados é igual ao número de nós em memória, isso significa que não foram eliminados nós após a sua exploração
- Sendo o custo 144, concluí-se que esta procura não é ótima e que não é completa, pois o último estado foi o 18 e não o 20
"""

#teste procura em profundidade limitada
# mec_proc = ProcuraProfLim()
# solucao = mec_proc.procurar(problema)

"""
Dimensão: 4
Custo: 144
Estado: 0
Operador: 6
Estado: 6
Operador: 6
Estado: 12
Operador: 6
Estado: 18
Operador: 6
Nós processados: 21
Nós memória: 21

Explicação:
- Segundo a classe ProcuraProfLim, o valor padrão da profundidade máxima é 10, então os resultados desta procura são idênticos ao anterior, pois a profundidade foi 4 (4 < 10)
"""

#teste procura em largura
# mec_proc = ProcuraLargura()
# solucao = mec_proc.procurar(problema)

"""
Dimensão: 3
Custo: 142
Estado: 0
Operador: 5
Estado: 5
Operador: 6
Estado: 11
Operador: 9
Nós processados: 221
Nós memória: 221

Explicação:
- Este método utiliza FIFO (First in, First Out), e como este mecanismo procura o caminho mais curto (menor profundidade) e com custo menor, desde o estado inicial até ao objetivo, 
os incrementos utilizados foram 5; 6 e 9, onde: custo = 5² + 6² + 9² = 142. Poderia ter utilizado 6; 9 e 6, mas o custo seria 153, que é maior que 142
"""

#teste procura em profundidade iterativa
#mec_proc = ProcuraProfIter()
#solucao = mec_proc.procurar(problema)

"""
Dimensão: 3
Custo: 153
Estado: 0
Operador: 6
Estado: 6
Operador: 6
Estado: 12
Operador: 9
Nós processados: 16
Nós memória: 15

custo: 6² + 6² + 9² = 153
Explicação:
- Esta procura combina as vantagens das procuras em profundidade limitada e em largura.
- A cada iteração, é feita uma procura em profundidade com um certo limite de profundidade (que por defeito é 100). Depois de cada iteração, é incrementado em 1 o valor
do limite de profundidade até chegar ao valor limite definido
- Repete até chegar ao objetivo
- Como esta combina procura em profundidade e em largura, o primeiro incremento foi 6 e foi aumentando até chegar ao 9
- Houve um nó a ser eliminado, já que nós_memória = nós_processados - nós_eliminados <=> 15 = 16 - nós_eliminados <=> nós_eliminados = 1
"""

#teste procura custo uniforme
#mec_proc = ProcuraCustoUnif()
#solucao = mec_proc.procurar(problema)

"""
Dimensão: 20
Custo: 20
Estado: 0
Operador: 1
Estado: 1
Operador: 1
Estado: 2
Operador: 1
Estado: 3
Operador: 1
Estado: 4
Operador: 1
Estado: 5
Operador: 1
Estado: 6
Operador: 1
Estado: 7
Operador: 1
Estado: 8
Operador: 1
Estado: 9
Operador: 1
Estado: 10
Operador: 1
Estado: 11
Operador: 1
Estado: 12
Operador: 1
Estado: 13
Operador: 1
Estado: 14
Operador: 1
Estado: 15
Operador: 1
Estado: 16
Operador: 1
Estado: 17
Operador: 1
Estado: 18
Operador: 1
Estado: 19
Operador: 1
Nós processados: 101
Nós memória: 81

Explicação:
- A procura de custo uniforme, prioriza a exploração dos nós com menor custo, daí o incremento utilizado da lista ser 1, que resulta também num custo acumulado menor
- Os nós foram eliminados dos nós em memória, pois os nós foram todos explorados
- A partir destes resultados, percebe-se que este tipo de procura é ótimo pois chegou ao valor final pretendido, e que tem uma maior complexidade computacional
"""

#teste procura AA
# heuristica = HeuristicaContagem(valor_final)
# mec_proc = ProcuraAA()
# solucao = mec_proc.procurar(problema, heuristica)

"""
Dimensão: 20
Custo: 20
Estado: 0
Operador: 1
Estado: 1
Operador: 1
Estado: 2
Operador: 1
Estado: 3
Operador: 1
Estado: 4
Operador: 1
Estado: 5
Operador: 1
Estado: 6
Operador: 1
Estado: 7
Operador: 1
Estado: 8
Operador: 1
Estado: 9
Operador: 1
Estado: 10
Operador: 1
Estado: 11
Operador: 1
Estado: 12
Operador: 1
Estado: 13
Operador: 1
Estado: 14
Operador: 1
Estado: 15
Operador: 1
Estado: 16
Operador: 1
Estado: 17
Operador: 1
Estado: 18
Operador: 1
Estado: 19
Operador: 1
Nós processados: 101
Nós memória: 81

Explicação:
- Sendo a Procura A* da forma f(n) = g(n) + h(n), e sabendo que a Procura de Custo Uniforme é f(n) = g(n) e que a Procura Sôfrega é f(n) = h(n), e sabendo também que os resultados
desta procura foram iguais à anterior, significa que h(n) não foi admissível
"""

#teste procura sofrega
# heuristica = HeuristicaContagem(valor_final)
# mec_proc = ProcuraSofrega()
# solucao = mec_proc.procurar(problema, heuristica)

"""
Dimensão: 4
Custo: 164
Estado: 0
Operador: 9
Estado: 9
Operador: 9
Estado: 18
Operador: 1
Estado: 19
Operador: 1
Nós processados: 21
Nós memória: 17

custo = 9² + 9² + 1 + 1 = 164
Explicação:
- A Procura Sôfrega é do tipo f(n) = h(n), ou seja, esta utiliza a função heurísitica, que estima o custo ou a distância de um nó até ao objetivo
- Supondo que h(n) = |valor_final - estado_atual|, então, para cada incremento da lista:
    - Nó inicial:
    0 + 5 = 5 -> h(5) = |20 - 5| = 15
    0 + 1 = 1 -> h(1) = 19
    0 + 6 = 6 -> h(6) = 14
    0 + 9 = 9 -> h(9) = 11 <- melhor heurística
    0 + 6 = 6 -> h(6) = 14
    ou seja, o incremento utilizado foi o 9
    - Estado seguinte (9):
    9 + 5 = 14 -> h(14) = |20 - 14| = 6
    9 + 1 = 10 -> h(10) = 10
    9 + 6 = 15 -> h(15) = 5
    9 + 9 = 18 -> h(18) = 2 <- melhor heurística
    9 + 6 = 15 -> h(15) = 5
    ou seja, o incremento utilizado foi o 9
    - Estado seguinte (18):
    18 + 5 = 23 -> ultrapassa 20
    18 + 1 = 19 -> h(19) = 1 <- melhor e única heurísitca, neste caso
    18 + 6 = 24 -> ultrapassa 20
    18 + 9 = 27 -> ultrapassa 20
    18 + 6 = 24 -> ultrapassa 20
    ou seja, o incremento utilizado foi o 1
    - Estado seguinte (19):
    19 + 1 = 20 <- objetivo
    ou seja, o incremento utilizado foi o 1
- Como os nós em memória são 17 e os processados são 21, concluí-se que foram eliminados os 4 nós explorados, ou seja, a procura sôfrega não mantém todos os nós explorados
"""

# ------------------------------------------------------------------------------------------------------------------------------------------ #

valor_inicial_1 = 0
valor_final_1 = 9
incrementos_1 = [1, 2, -1]

problema_1 = ProblemaContagem(valor_inicial_1, valor_final_1, incrementos_1)

#ProcuraLargura
#mec_proc = ProcuraLargura()
#solucao = mec_proc.procurar(problema_1)

#ProcuraProfLim
#mec_proc = ProcuraProfLim(prof_max=5)
#solucao = mec_proc.procurar(problema_1)

#ProcuraCustoUnif
#mec_proc = ProcuraCustoUnif()
#solucao = mec_proc.procurar(problema_1)

#ProcuraSofrega
#heuristica_1 = HeuristicaContagem(valor_final_1)
#mec_proc = ProcuraSofrega()
#solucao = mec_proc.procurar(problema_1, heuristica_1)

#ProcuraAA
heuristica_1 = HeuristicaContagem(valor_final_1)
mec_proc = ProcuraAA()
solucao = mec_proc.procurar(problema_1, heuristica_1)


if solucao:
    print(f"Dimensão: {solucao.dimensao}") #profundidade
    print(f"Custo: {solucao.custo}")
    for passo in solucao:
        print(f"Estado: {passo.estado.valor}")
        print(f"Operador: {passo.operador.incremento}")
    print(f"Nós processados: {mec_proc.nos_processados}")
    print(f"Nós memória: {mec_proc.nos_memoria}")
    print(f"Nós repetidos: {mec_proc.nos_repetidos}")