package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

/**
 * Classe que representa um estado numa Máquina de Estados.
 *
 * Um estado define uma configuração específica do sistema, com transições possíveis para outros
 * estados em resposta a eventos. Cada estado pode ter múltiplas transições, dependendo dos eventos
 * que podem ocorrer.
 *
 * Segundo os PDFs, os estados são a base para a modelagem da dinâmica de sistemas,
 * onde o sistema evolui de um estado para outro em resposta a eventos.
 */
public class Estado {

    public String nome; // Nome do estado (read-only)
    private Map<Evento, Transicao> transicoes; // Mapa de transições associadas a eventos

    /**
     * Construtor do estado.
     * <p>
     * Este método inicializa um estado com um nome e um mapa vazio de transições.
     * O nome do estado é usado para identificá-lo no sistema.
     * <p>
     * No slide 11 do pdf P1-iasa-proj, o diagrama de classes mostra 0..*, ou seja,
     * foi necessário criar um dicionário para guardar transições e os respetivos eventos.
     * @param nome O nome do estado.
     */
    public Estado(String nome){
        this.transicoes = new HashMap<Evento, Transicao>();
        this.nome = nome;
    }

    /**
     * Processa um evento e retorna a transição correspondente.
     * <p>
     * Este método verifica se há uma transição definida para o evento e
     * retorna a transição correspondente. Caso contrário, retorna null.
     * @param evento O evento que ocorreu.
     * @return A transição associada ao evento, ou null se não houver transição definida.
     */
    public Transicao processar(Evento evento){
        return transicoes.get(evento);
    }

    /**
     * Define uma transição para um evento sem ação associada.
     * <p>
     * Este método é útil para definir transições que não estão associadas a nenhuma ação.
     * @param evento O evento que desencadeia a transição.
     * @param estadoSucessor O estado para o qual a transição leva.
     * @return O próprio estado, para permitir chamadas encadeadas.
     */
    public Estado transicao(Evento evento, Estado estadoSucessor){
        transicoes.put(evento, new Transicao(estadoSucessor, null));
        return this;
    }

    /**
     * Define uma transição para um evento com uma ação associada.
     * <p>
     * Este método é útil para definir transições que estão associadas a uma ação específica.
     * @param evento O evento que desencadeia a transição.
     * @param estadoSucessor O estado para o qual a transição leva.
     * @param accao A ação associada à transição.
     * @return O próprio estado, para permitir chamadas encadeadas.
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao){
        transicoes.put(evento, new Transicao(estadoSucessor, accao));
        return this;
    }

    /**
     * Retorna o nome do estado.
     * <p>
     * Foi feito este getter pois no diagrama de classes do slide 11,
     * do pdf PA-iasa-proj, o atributo nome é read-only.
     * @return Nome do estado.
     */
    public String getNome(){
        return nome;
    }
}
