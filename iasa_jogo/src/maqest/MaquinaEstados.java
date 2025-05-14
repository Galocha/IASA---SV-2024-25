package maqest;

import agente.Accao;
import ambiente.Evento;

/**
 * Classe que implementa uma Máquina de Estados.
 * <p>
 * Uma Máquina de Estados é um modelo computacional que descreve o comportamento de um sistema
 * através de um conjunto de estados, transições entre esses estados e ações associadas a essas transições.
 * <p>
 * Pelo pdf 05-introd-eng-soft-3, a Máquina de Estados é usada para modelar a dinâmica de sistemas, onde o estado
 * atual do sistema evolui em resposta a eventos, originando ações e transições para novos estados.
 * <p>
 * Esta classe é responsável por processar eventos e gerar ações com base no estado atual e nas
 * transições definidas. Ela reflete o conceito de função de transformação, onde o estado atual
 * e o evento são usados para determinar o próximo estado e a ação a ser executada.
 */
public class MaquinaEstados {

    private Estado estado; // Estado atual da máquina de estados

    /**
     * Construtor da Máquina de Estados
     * <p>
     * Este método inicializa a máquina de estados com um estado inicial, que será o ponto de partida
     * para a evolução do sistema.
     * <p>
     * Todas as máquinas de estados precisam de um estado inicial para o
     * sistema poder evoluir.
     * <p>
     * @param estadoInicial O estado inicial da máquina de estados.
     */
    public MaquinaEstados(Estado estadoInicial){
        this.estado = estadoInicial;
    }

    /**
     * Processa um evento e retorna a ação correspondente.
     * <p>
     * Este processa o evento atual, verifica se há uma transição definida para esse evento e,
     * se houver, atualiza o estado atual e retorna a ação associada. Caso contrário, retorna null.
     * <p>
     * Este método está alinhado com o conceito de função de transição de estado (δ) e função de saída (λ),
     * conforme descrito no slide 4 do pdf mencionado nos comentários da classe. A função de transição determina
     * o próximo estado, e a função de saída determina a ação a ser executada.
     * <p>
     * @param evento O evento que ocorreu no ambiente.
     * @return A ação a ser executada, ou null se não houver transição definida para o evento.
     */
    public Accao processar(Evento evento){
        Transicao transicao = estado.processar(evento);
        if(transicao != null){
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        } else {
            return null;
        }
    }

    /**
     * Retorna o estado atual da máquina de estados.
     * <p>
     * Este permite que outras classes acedam ao estado atual da máquina de estados, sem
     * modificar o seu estado interno.
     * <p>
     * Foi feito este getter pois no diagrama de classes do slide 11, do pdf PA-iasa-proj,
     * o atributo estado é read-only.
     * @return O estado atual.
     */
    public Estado getEstado(){
        return estado;
    }
}
