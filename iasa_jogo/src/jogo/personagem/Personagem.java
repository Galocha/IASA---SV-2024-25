package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;

/**
 * Classe que representa a personagem do jogo
 */
public class Personagem extends Agente {
    public Personagem(AmbienteJogo ambiente){ //construtor da classe
        super(ambiente, new ControloPersonagem()); //foi necessário fazer super, pois Personagem estende de Agente
        //no super, o parâmetro ambiente será o do AmbienteJogo da Personagem, e o controlo é uma nova instância do ControloPersonagem
    }
}
