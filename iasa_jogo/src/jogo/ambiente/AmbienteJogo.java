package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Classe que representa o Ambiente de Jogo, no qual será possível o agente interagir
 */
public class AmbienteJogo implements Ambiente {
    public EventoJogo evento; //instância da classe EventoJogo, que será usada para definir o evento atual do ambiente
    private Scanner scanner = new Scanner(System.in); //scanner é utilizado para receber um input do utilizador
    private Map<String, EventoJogo> eventos; //tendo em conta o UML, eventos terá de ser Map pois está ligado por composição ao Enum EventoJogo, deste modo criou-se um dicionário, evitando switch-case ou if-else
    public AmbienteJogo(){ //construtor da classe
        eventos = new HashMap<String, EventoJogo>(); //inicialização do dicionário dos eventos
        //atribuição de uma string ao respetivo evento
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
    }
    public void evoluir(){ //evolução do ambiente | este método é implementado a partir da interface Ambiente
        evento = gerarEvento(); //faz-se evento = gerarEvento() para atualizar o evento atual do ambiente
    }
    public Evento observar() { //observar o evento atual | este método é implementado a partir da interface Ambiente
        if (evento != null){
            evento.mostrar(); //mostrar no ecrã o evento atual
        }
        return evento; //retornar o mesmo
    }
    public void executar(Comando comando){ //método que permite mostrar um determinado comando | este método é implementado a partir da interface Ambiente
        //mostrar o comando no ecrã
        comando.mostrar();
    }
    private EventoJogo gerarEvento(){ //a partir do input do utilizador, é gerado um evento, retornando o mesmo
        System.out.print("\nEvento? ");
        String codigoEvento = scanner.next();
        return eventos.get(codigoEvento);
    }
    public EventoJogo getEventoJogo(){ //como é read-only, foi necessário criar o getter para EventoJogo
        return evento;
    }
}
