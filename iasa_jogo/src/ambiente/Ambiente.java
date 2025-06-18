package ambiente;

/**
 * Interface que define o ambiente onde o agente interage.
 * O ambiente evolui, pode ser observado e permite a execução de comandos.
 *
 * Esta interface também reflete o princípio de abstração,
 * onde o ambiente é representado de forma genérica,
 * permitindo que diferentes implementações
 * concretas sejam criadas para diferentes cenários
 */
public interface Ambiente {

    /**
     * Faz o ambiente evoluir, alterando o seu estado.
     *
     * Este método é responsável por atualizar o estado do ambiente,
     * refletindo mudanças que ocorrem ao longo do tempo.
     */
    public void evoluir();

    /**
     * Observa o ambiente e retorna um evento ocorrido.
     *
     * A observação é o ato de coletar informações do ambiente.
     * É uma ação realizada pelo agente para obter dados sobre o estado atual do ambiente.
     *
     * Este método é responsável por retornar um evento que ocorreu no ambiente.
     *
     * @return O evento observado no ambiente.
     */
    public Evento observar();

    /**
     * Executa um comando no ambiente.
     *
     * Este método permite que o agente realize ações no ambiente, como mover-se, fotografar um animal
     * ou realizar outras interações. O comando é uma representação da decisão tomada pelo agente após
     * processar uma perceção.
     *
     * Este método está alinhado com o ciclo de ação do agente, onde ele executa uma decisão
     * no ambiente. Conforme os slides, a ação é o resultado final do processamento de uma perceção
     * reflete a racionalidade do agente.
     *
     * @param comando O comando a ser executado.
     */
    public void executar(Comando comando);
}