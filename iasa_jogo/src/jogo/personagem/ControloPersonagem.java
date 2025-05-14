package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jdk.jfr.Event;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

/**
 * Classe que representa o controlo da personagem
 * <p>
 * Esta classe implementa a interface Controlo, definindo a lógica de decisão da personagem
 * com base nas perceções do ambiente. O controlo processa as perceções e decide qual ação
 * a personagem deve realizar.
 * <p>
 * O conceito de modularização é aqui utilizado para lidar específicamente com o controlo da personagem,
 * não misturando a lógica de outras funcionalidades do jogo com esta. Esta abordagem permitiu sistematizar
 * interações, pois a tomada de decisão da personagem está isolada e bem estruturada. Isto facilita também
 * a manutenção e extensão do sistema.
 */
public class ControloPersonagem implements Controlo {

    /**
     * Pelo slide 14 do pdf da parte 1 do projeto, é necessário declarar
     * um atributo privado de máquina de estados
     */
    private MaquinaEstados maqEst;

    /**
     * Construtor da classe `ControloPersonagem`.
     * <p>
     * Este método inicializa o controlo da personagem, preparando-o para processar perceções
     * e decidir ações.
     */
    public ControloPersonagem(){
        //Definir os estados
        Estado procura = new Estado("Procura");
        Estado inspeccao = new Estado("Inspecção");
        Estado observacao = new Estado("Observação");
        Estado registo = new Estado("Registo");

        //Definir as ações
        Accao procurar = new Accao(ComandoJogo.PROCURAR);
        Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
        Accao observar = new Accao(ComandoJogo.OBSERVAR);
        Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);

        procura
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.RUIDO, inspeccao, aproximar)
                .transicao(EventoJogo.SILENCIO, procura, procurar);

        inspeccao
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.SILENCIO, procura)
                .transicao(EventoJogo.RUIDO, inspeccao, procurar);

        observacao
                .transicao(EventoJogo.ANIMAL, registo, observar)
                .transicao(EventoJogo.FUGA, inspeccao);

        registo
                .transicao(EventoJogo.FUGA, procura)
                .transicao(EventoJogo.FOTOGRAFIA, procura)
                .transicao(EventoJogo.ANIMAL, registo, fotografar);

        maqEst = new MaquinaEstados(procura);
    }

    /**
     * Método que processa uma perceção e decide qual é a ação que a personagem deve realizar.
     * <p>
     * Este método é o núcleo do controlo da personagem. Este recebe uma perceção do ambiente
     * e, com base nessa informação, decide qual a ação a realizar. A ação é então retornada
     * para ser executada no ambiente.
     *
     */
    @Override
    public Accao processar(Percepcao percepcao) {
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();
        return accao;
    }

    /**
     * Método que exibe o controlo da personagem no ecrã.
     * <p>
     * Este método é útil para fornecer feedback sobre o estado atual do controlo da personagem,
     * facilitando a compreensão e a depuração do sistema.
     *
     */
    private void mostrar(){ //alterar o javadoc
        System.out.printf("Estado atual: %s\n", getEstado().getNome());
    }

    public Estado getEstado(){
        return maqEst.getEstado();
    }
}
