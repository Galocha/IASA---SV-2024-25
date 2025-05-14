package agente;

/**
 * Interface que define o controlo de um agente.
 * O controlo processa as perceções do agente e decide qual ação deve ser realizada.
 *<p>
 * Esta interface reflete o princípio de abstração,
 * onde o controlo é representado de forma genérica,
 * permitindo que diferentes implementações concretas
 * sejam criadas para diferentes estratégias de decisão.
 *
 */
public interface Controlo {

    /**
     * Processa uma perceção do ambiente e decide a ação a ser tomada.
     *<p>
     * Este método é o núcleo do controlo do agente. Ele recebe uma perceção do ambiente
     * (informação coletada pelo agente) e, com base nessa informação, decide qual ação
     * o agente deve realizar. A ação é então retornada para ser executada no ambiente.
     *
     * @param percepcao A perceção do ambiente.
     * @return A ação a ser realizada pelo agente.
     *
     */
    Accao processar(Percepcao percepcao);

}