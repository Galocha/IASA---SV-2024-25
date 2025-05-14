from pee.mec_proc.fronteira import Fronteira #import necessário pois esta classe herda de Fronteira

class FronteiraFIFO(Fronteira):
    def inserir(self, no):
        """
        Classe que implementa uma fronteira do tipo FIFO (First In, First Out)

        Representa uma estrutura de dados utilizada em mecanismos de procura, onde os nós são geridos de 
        forma que os primeiros a serem inseridos sejam os primeiros a serem processados
        Esta abordagem é utilizada em estratégias como a procura em largura (Breadth-First Search)

        Fundamentação teórica:
        - 10-pee-1.pdf, página 28: explica-se que a procura em largura utiliza uma fronteira FIFO para explorar primeiro os nós mais antigos
        - P3-iasa-proj.pdf, página 7: é descrito o conceito de fronteira como uma estrutura ordenada que gerencia os nós a explorar
        """
        self._nos.append(no)