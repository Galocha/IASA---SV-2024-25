package ambiente;

/**
 * Interface Evento
 * Define os métodos que uma implementação de um evento
 * Num sistema de agentes inteligentes, um evento representa uma ocorrência no ambiente, percetível pelo agente
 * <p>
 * Está aqui presente a abstração, onde foi definida uma interface genérica de evento
 */
public interface Evento {

    /**
     * Permite que o evento seja exibido ou representado de forma legível.
     */
    public void mostrar();
}
