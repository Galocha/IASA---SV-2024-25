package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/**
 * Classe que representa o jogo
 */
public class Jogo {
    private static AmbienteJogo ambiente; //por composição, segundo o UML, é necessário uma instância do objeto AmbienteJogo
    private static Personagem personagem; //por composição, segundo o UML, é necessário uma instância do objeto Personagem
    public static void main(String[] args) { //método principal que irá correr o método executar
        ambiente = new AmbienteJogo(); //instância da classe AmbienteJogo, que será o ambiente do jogo
        personagem = new Personagem(ambiente); //instância da classe Personagem, que será a personagem principal do jogo
        executar(); //segundo o diagrama sequencial da página 9, do pdf "P1-iasa-proj", o executar será chamado dentro do main
    }
    private static void executar(){ //método que mantém o jogo em execução | este tem de ser estático pois é chamado dentro do main (sendo este estático)
        //é feito um do-while porque no diagrama sequencial, os comportamentos estão em loop
        do { //é utilizado do-while, pois só se deve testar o evento depois do ambiente evoluir
            ambiente.evoluir(); //dá-se a evolução do ambiente
            personagem.executar(); //dá-se a execução da personagem
        } while (ambiente.getEventoJogo() != EventoJogo.TERMINAR); //o jogo mantém-se ativo enquanto não se der o evento TERMINAR
    }
}
