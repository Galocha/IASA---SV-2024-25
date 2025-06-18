from modelo.modelo_pdm import ModeloPDM
from lib.pdm.pdm import PDM

class ModeloAmbiente7x1(ModeloPDM):
    """
    Implementação concreta de ModeloPDM para o ambiente 7x1 descrito nos materiais
    Modela um problema de decisão sequencial com 7 estados lineares e ações de movimento

    Características principais:
    - Ambiente totalmente determinístico
    - Dois estados terminais: 1 (perda) e 7 (ganho)

    Fundamentação teórica (15-pds-exemplo.pdf):
    - Páginas 1-5: Descrevem o ambiente 7x1 com estados terminais em 1 (perda) e 7 (ganho)
    - Página 2: Mostra as matrizes de transição e recompensa para este ambiente
    - Página 4: Apresenta o cálculo iterativo das utilidades para este caso
    """
    def __init__(self):
        """
        Inicializa o modelo do ambiente 7x1 com:
        - Estados possíveis (1 a 7)
        - Ações possíveis ('<' esquerda e '>' direita)
        - Matriz de transições determinísticas (T)
        - Matriz de recompensas (R)
        
        Estados terminais:
        - Estado 1: Perda (não permite transições)
        - Estado 7: Ganho (não permite transições)

        Exemplo (15-pds-exemplo.pdf, página 2):
        - T(2,'<',1) = 1 (transição determinística)
        - R(6,'>',7) = 1 (recompensa positiva no objetivo)
        """
        self.__S = [1, 2, 3, 4, 5, 6, 7]
        self.__A = ['<', '>'] # esquerda: < | direita: >
        self.__T = {
            #(estado inicial, operador, resultado) : probabilidade
            (1, '<', 1):0,
            (1, '>', 2):0,
            (2, '<', 1):1,
            (2, '>', 3):1,
            (3, '<', 2):1,
            (3, '>', 4):1,
            (4, '<', 3):1,
            (4, '>', 5):1,
            (5, '<', 4):0,
            (5, '>', 6):1,
            (6, '<', 5):1,
            (6, '>', 7):1,
            (7, '<', 6):0,
            (7, '>', 7):0
        }
        self.__R = {
            (1, '<', 1):0,
            (1, '>', 2):0,
            (2, '<', 1):-1,
            (2, '>', 3):0,
            (3, '<', 2):0,
            (3, '>', 4):0,
            (4, '<', 3):0,
            (4, '>', 5):0,
            (5, '<', 4):0,
            (5, '>', 6):0,
            (6, '<', 5):0,
            (6, '>', 7):1,
            (7, '<', 6):0,
            (7, '>', 7):0
        }

        #dicionário definido por significado
        #padrão chave: produto cartesiano entre S e A
        #contra-domínio: conjunto de estados S
        self.__transicoes = {(s, a): sn for s, a, sn in self.__T if s not in [1, 7]}

    def S(self):
        """
        Retorna todos os estados possíveis do ambiente
        
        Retorno:
            list: Lista de estados [1, 2, 3, 4, 5, 6, 7]

        Teoria (15-pds.pdf, página 36):
        - S representa o conjunto de estados do mundo
        """
        return self.__S

    def A(self, s):
        """
        Retorna as ações possíveis para um estado específico
        
        Parâmetros:
            s: Estado atual
            
        Retorno:
            list: Lista de ações possíveis ou lista vazia para estados terminais

        Teoria (15-pds.pdf, página 36):
        - A(s) representa o conjunto de ações possíveis num estado s
        """
        return self.__A if s not in [1, 7] else []

    def T(self, s, a, sn):
        """
        Retorna a probabilidade de transição entre estados
        
        Parâmetros:
            `s`: Estado atual
            `a`: Ação executada
            `sn`: Estado seguinte
            
        Retorno:
            float: probabilidade `T(s,a,sn)`

        Teoria (15-pds.pdf, página 8):
        - `T(s,a,s')` representa a probabilidade de transição de um estado `s` 
        para um estado sucessor `sn` através de uma ação `a`
        """
        return self.__T[(s, a, sn)]

    def R(self, s, a, sn):
        """
        Retorna a recompensa associada a uma transição
        
        Parâmetros:
            `s`: Estado atual
            `a`: Ação executada
            `sn`: Estado seguinte
            
        Retorno:
            float: recompensa `R(s,a,sn)`

        Teoria (15-pds.pdf, página 8):
        - `R(s,a,s')` representa a recompensa esperada ao transitar de 
        `s` para `sn` através de `a`
        """
        return self.__R[(s, a, sn)]
    
    """
    função de geração de um estado 
    
    política dá a ação
    utilidade dá o valor que corresponde à ação que maximiza a utilidade
    """

    def suc(self, s, a):
        """
        Gera o estado sucessor que resulta de realizar a ação `a` no estado `s`
        
        Parâmetros:
            `s`: Estado atual
            `a`: Ação executada
            
        Retorno:
            list: Lista contendo um único estado sucessor (ambiente determinístico)
                  ou lista vazia para transições inválidas

        Implementado com indicação do docente

        Funcionamento:
        - Procura no dicionário de transições `self.__transicoes` o estado sucessor `sn` para o par `(s, a)`
            - Caso exista sucessor, retorna uma lista com esse estado
            - Caso não exista, retorna uma lista vazia (transição inválida)
        """
        #return self.__transicoes.get((s, a)) if (s, a) in self.__transicoes else []
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []
    
if __name__ == "__main__":
    modelo = ModeloAmbiente7x1()
    pdm = PDM(modelo, 0.5, 0.0)
    utilidade, politica = pdm.resolver()
    print(f"\nUtilidade: {utilidade}")
    print(f"\nPolítica: {politica}\n")

    """
    INTERPRETAÇÃO DOS RESULTADOS (15-pds-exemplo.pdf p.4)
    
    1. ANÁLISE DAS UTILIDADES:
       Estado 6: 1.000   - Valor máximo (atinge diretamente o estado 7 com recompensa +1)
       Estado 5: 0.500   - Metade do valor do estado 6 (γ=0.5)
       Estado 4: 0.250   - Metade do estado 5 (0.5×0.5)
       Estado 3: 0.125   - Metade do estado 4 (0.5³)
       Estado 2: 0.063   - Metade do estado 3 (0.5⁴)
       Estados 1 e 7: 0 - Terminais (não acumulam utilidade futura)
       
       Padrão: U(s) = γ^(distância ao objetivo) × Rmax
       Coerente com a equação U(s) = R(s) + γU(s') (15-pds.pdf p.27)

    2. POLÍTICA ÓTIMA:
       Todos os estados (2-6) → ação '>' (direita)
       - Estado 2: Evita '<' que leva à perda (-1)
       - Estado 5: Única ação possível é '>'
       - Estado 6: Direto para o ganho (+1)
       
       Exemplo (p.5): A política sempre maximiza a utilidade esperada:
       π*(s) = argmaxₐ Σ T(s,a,s')[R(s,a,s') + γU(s')]
    """