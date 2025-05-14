package maqest;

import agente.Accao;

/**
 * Classe que representa uma transição entre estados numa Máquina de Estados.
 * <p>
 * Uma transição define como o sistema evolui de um estado para outro em resposta a um evento,
 * podendo também estar associada a uma ação que deve ser executada durante a transição.
 * <p>
 * Segundo os PDFs, as transições são essenciais para modelar a dinâmica de sistemas, onde
 * eventos desencadeiam mudanças de estado e ações correspondentes.
 */
public class Transicao {
    private Estado estadoSucessor; // Estado para o qual a transição leva.
    private Accao accao; // Ação associada à transição.

    /**
     * Construtor da transição.
     * <p>
     * Este método inicializa uma transição com um estado sucessor e uma ação. A ação pode ser null
     * se a transição não estiver associada a nenhuma ação.
     *
     * @param estadoSucessor O estado para o qual a transição leva.
     * @param accao A ação associada à transição.
     */
    public Transicao(Estado estadoSucessor, Accao accao){
        this.accao = accao;
        this.estadoSucessor = estadoSucessor;
    }

    //estes getters foram feitos, porque, segundo os slides, estes são read-only
    public Estado getEstadoSucessor(){
        return estadoSucessor;
    }

    public Accao getAccao(){
        return accao;
    }
}
