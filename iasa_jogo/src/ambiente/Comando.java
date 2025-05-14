package ambiente;

/**
 * Interface que define um comando que pode ser executado no ambiente.
 * <p>
 * Um comando representa uma ação que o agente pode realizar no ambiente. Ele é o resultado
 * da decisão tomada pelo agente após processar uma perceção. Por exemplo, no contexto de um jogo,
 * um comando pode ser "PROCURAR", "APROXIMAR", "FOTOGRAFAR", etc.
 * <p>
 * Nesta está presente o princípio de abstração, onde o comando é representado de forma
 * genérica, permitindo que diferentes implementações concretas sejam criadas para diferentes
 * tipos de ações.
 */
public interface Comando {

    /**
     * Mostra o comando que desencadeou a ação atual.
     * <p>
     * Este método permite que o comando seja exibido ou representado de forma legível.
     * Por exemplo, no contexto de um jogo, o comando pode ser mostrado na interface do utilizador
     * para indicar qual ação o agente está realizando.
     */
    public void mostrar();
}
