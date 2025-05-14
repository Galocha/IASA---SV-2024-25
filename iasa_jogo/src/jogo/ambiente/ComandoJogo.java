package jogo.ambiente;

import ambiente.Comando;

/**
 * Enumeração que representa todos os comandos possíveis que o agente poderá fazer.
 * <p>
 * Esta implementa a interface Comando, definindo as ações específicas que o agente
 * pode executar no ambiente do jogo. Cada comando representa uma decisão tomada pelo agente após processar uma perceção.
 */
public enum ComandoJogo implements Comando {
    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    /**
     * Método que mostra o comando atual, implementado a partir da interface Comando.
     */
    @Override
    public void mostrar(){
        System.out.printf("Comando: %s\n", this);
    }
}

