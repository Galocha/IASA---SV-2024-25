package agente;
import ambiente.Evento;

/**
 * Classe que representa a perceção do agente em relação ao ambiente.
 *<p>
 * A perceção é a interpretação de um evento observado no ambiente.
 * Esta é gerada quando o agente processa as informações coletadas
 * durante a observação do ambiente.
 *<p>
 * Esta classe reflete o princípio de encapsulamento, onde o evento observado é armazenado
 * e acedido de forma controlada, garantindo que a perceção seja consistente e imutável após
 * a sua criação.
 */
public class Percepcao{

	public Evento evento; //evento que desencadeou a perceção

    /**
     * Construtor para criar uma perceção com base num evento.
     * O evento é encapsulado na perceção, que será processada pelo agente
     * para tomar decisões.
     *<p>
     * Este construtor utiliza o princípio de modularização, onde a lógica de criação
     * de uma perceção é centralizada num único ponto, facilitando a reutilização e a
     * consistência do código.
     *<p>
     * @param evento O evento que gerou a perceção.
     */
    public Percepcao(Evento evento) {
        this.evento = evento;
	}

    /**
     * Retorna o evento associado à perceção.
     * <p>
     * Como o Evento é read-only, é necessário criar um getter para ser possível a
     * outra classe perceber qual é o evento que foi desencadeado.
     * <p>
     * Aqui é utilizado o encapsulamento para garantir que o evento não seja
     * acedido diretamente e que não possa ser alterado
     * <p>
     * Este método está alinhado com o princípio de abstração, onde os detalhes internos
     * da perceção são ocultados, expondo apenas a interface necessária para interagir com
     * classe.
     * @return O evento que gerou a perceção.
     */
    public Evento getEvento() {
        return evento;
    }
}