from pee.mec_proc.passo_solucao import PassoSolucao

class Solucao:
    """
    Representa uma solução completa para um problema de busca, encapsulando:
    1. O caminho desde o estado inicial até o objetivo
    2. O custo total da solução
    3. A dimensão (número de passos) da solução

    Referências cruzadas:
    - P3-iasa-proj.pdf (slide 5): Diagrama da classe Solucao
    - 10-pee-1.pdf (slide 13): Solução como sequência de nós
    """
    def __init__(self, no_final):
        self.__no_final = no_final
        self.__passos = []
        no = no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador) # Criar um novo passo
            self.__passos.insert(0, passo) # Inserir o passo no início da lista
            no = no.antecessor # Andar com o nó para trás sucessivamente até não haver mais nenhum antecessor

    def __iter__(self):
        return iter(self.__passos) #iterador para a lista de passos

    def __getitem__(self, index):
        return self.__passos[index]
    
    @property
    def dimensao(self):
        """
        Propriedade que retorna a dimensão da solução

        Funcionamento:
        - Determina a profundidade do nó final

        Fundamentação teórica:
        - 10-pee-1.pdf, slide 31: a dimensão de uma solução refere-se ao número de transições entre os estados no percurso
        - P3-iasa-proj.pdf, slide 5: menciona-se a dimensão como uma propriedade essencial de qualquer solução
        """
        dimensao = self.__no_final.profundidade
        return dimensao
    
    @property
    def custo(self):
        """
        Propriedade que retorna o custo total do percurso da solução

        Funcionamento:
        - Calcula a soma dos custos acumulados ao longo das transições entre estados, desde o estado inicial até o objetivo

        Fundamentação teórica:
        - 10-pee-1.pdf, páginas 15 e 30: o custo é tratado como o valor acumulado que mede a eficiência da solução
        """
        custo = self.__no_final.custo #o custo do nó final é a soma dos custos de todos os nós
        return custo