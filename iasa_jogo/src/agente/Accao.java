package agente;
import ambiente.Comando;

/**
 * Classe que representa uma ação que o agente pode realizar no ambiente.
 * Reflete o ciclo de perceção-processamento-ação de um agente autónomo,
 * onde a ação é o resultado final do processamento de uma perceção.
 *
 * A relação entre a ação e o comando é fundamental para a racionalidade do agente, pois o agente deve
 * escolher a ação que maximiza o seu desempenho, dado o conhecimento disponível sobre o ambiente.
 *
 * Esta classe também reflete o princípio de modularização da Engenharia de Software, onde a funcionalidade
 * do agente é dividida em partes coesas e bem definidas, facilitando a manutenção e evolução do sistema.
 */
public class Accao {

    /**
     * Comando associado à ação que o agente irá executar.
     * Representa a decisão tomada pelo agente após processar uma perceção.
     *
     * Este atributo é essencial para a interação do agente com o ambiente,
     * conforme descrito nos diagramas.
     */
	public Comando comando;

    /**
     * Construtor da classe Accao.
     *<p>
     * Permite a criação de uma ação específica com base no comando fornecido.
     * O comando define o tipo de ação que o agente irá realizar no ambiente.
     *<p>
     * Este construtor utiliza o conceito de modularização,
     * onde a lógica de criação de uma ação é centralizada
     * em um único ponto, facilitando a reutilização e a consistência do código.
     *
     * @param comando O comando que define a ação a ser realizada pelo agente.
     */
    public Accao(Comando comando) {
        this.comando = comando;
    }

    /**
     * Método para obter o comando associado à ação.
     *<p>
     * Como o Comando é read-only, é necessário criar um getter para ser possível
     * outra classe perceber qual é o comando que está atualmente a ser feito.
     *<p>
     * Aqui é utilizado o encapsulamento para garantir que o comando não seja
     * acedido diretamente e que não possa ser alterado
     * @return O comando associado à ação.
     */
    public Comando getComando() {
        return comando;
    }

}