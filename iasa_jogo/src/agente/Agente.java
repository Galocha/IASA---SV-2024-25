package agente;
import ambiente.Ambiente;
import ambiente.Evento;

/**
 * Classe abstrata que representa um agente autónomo.
 * <p>
 * Um agente autónomo é uma entidade que interage com um ambiente, percecionando-o, processando
 * as informações e realizando ações para alcançar os seus objetivos. Esta classe define a estrutura
 * básica de um agente, incluindo a interação com o ambiente e o controlo das suas ações.
 * <p>
 * Segundo os slides, um agente autónomo opera num ciclo de perceção-processamento-ação:
 * Perceção: O agente observa o ambiente e recolhe informações;
 * Processamento: O agente processa as informações e decide qual ação realizar;
 * Ação: O agente executa a ação no ambiente.
 * <p>
 * Esta classe incorpora o princípio da abstração, definindo a funcionalidade do agente de maneira genérica,
 * o que possibilita a implementação de diversos tipos de agentes para distintos cenários.
 */
public abstract class Agente {

	private Ambiente ambiente; // Ambiente onde o agente interage.
	private Controlo controlo; // Mecanismo de controlo do agente.

	/**
	 * Construtor para criar um agente com um ambiente e controlo específicos.
	 * <p>
	 * O ambiente define o espaço onde o agente opera, e o controlo define a lógica de decisão do agente.
	 * <p>
	 * @param ambiente O ambiente onde o agente irá interagir.
	 * @param controlo O mecanismo de controlo do agente.
	 */
    public Agente(Ambiente ambiente, Controlo controlo) {
		this.ambiente = ambiente;
		this.controlo = controlo;
	}

	/**
	 * Executa o agente, permitindo que ele interaja com o ambiente.
	 * <p>
	 * Este método inicia o ciclo de interação do agente com o ambiente.
	 * O agente perceciona o ambiente, processa as informações e realiza
	 * ações de acordo com o seu controlo.
	 * <p>
	 * Segundo o diagrama de atividades do slide 10 do PDF P1-iasa-proj, o método
	 * executar() tem que precepcionar; processar essa preceção (que é uma ação);
	 * e por fim é fazer atuar essa ação.
	 */
    public void executar() {
		Percepcao percepcao = percepcionar();
		Accao accao = controlo.processar(percepcao);
		actuar(accao);
	}

	/**
	 * Permite ao agente percecionar o ambiente.
	 * <p>
	 * Este método é responsável por recolher informações do ambiente,
	 * que serão processadas pelo agente para tomar decisões.
	 * A perceção é o primeiro passo no ciclo de interação do agente com o ambiente.
	 *
	 * @return Uma perceção do ambiente.
	 */
    protected Percepcao percepcionar() {
		Evento evento = ambiente.observar();
		return new Percepcao(evento);
	}

	/**
	 * Permite ao agente realizar uma ação no ambiente.
	 *
	 * @param accao A ação a ser realizada.
	 */
    protected void actuar(Accao accao) {
		if(accao!= null) {
			ambiente.executar(accao.getComando());
		}
	}

	/**
	 * Retorna o controlo do agente.
	 * <p>
	 * Como o Controlo é read-only, é necessário criar um getter para ser possível a
	 * outra classe perceber qual é o controlo que está atualmente a ser feito.
	 * <p>
	 * Aqui é utilizado o encapsulamento para garantir que o controlo não seja
	 * acedido diretamente e que não possa ser alterado
	 *
	 * @return O controlo do agente.
	 */
	public Controlo getControlo() {
		return controlo;
	}
}