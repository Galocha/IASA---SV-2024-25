package jogo.ambiente;

import ambiente.Evento;

/**
 * Enumeração que representa todos os tipos de Eventos do jogo possíveis
 * <p>
 * Esta implementa a interface Evento, definindo as ocorrências específicas que
 * podem acontecer no ambiente do jogo. Cada evento representa algo que o agente pode percecionar
 */
public enum EventoJogo implements Evento {
    SILENCIO,
    RUIDO,
    ANIMAL,
    FUGA,
    FOTOGRAFIA,
    TERMINAR;

    /**
     * Método que exibe o evento atual no ecrã.
     *
     */
    @Override
    public void mostrar() {
        System.out.printf("\nEvento: %s\n", this);
    }
}