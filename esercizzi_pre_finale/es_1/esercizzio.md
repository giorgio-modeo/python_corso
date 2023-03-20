Esercizio - Gestione di un negozio online
Si intende realizzare una gerarchia di classi per la gestione di un negozio online che vende prodotti di vario genere, tra cui alimentari e non alimentari.
Un prodotto è caratterizzato da un codice identificativo, un nome, una descrizione, un prezzo e una quantità disponibile.


1) I prodotti alimentari sono caratterizzati inoltre da una data di scadenza e da un eventuale sconto se si acquista una quantità minima.
2) I prodotti non alimentari sono caratterizzati invece dalla loro categoria (es. abbigliamento, elettronica, libri) e dal loro peso.
Alcune categorie di prodotti non alimentari sono soggette a una tassa aggiuntiva del 10% sul prezzo base.

Scrivere in python l’implementazione della gerarchia di classi descritta fornendo per Prodotti Alimentari e Non Alimentari i relativi attributi e i metodi che permettono di visualizzare le caratteristiche citate.
Definire mediante un diagramma UML le classi che realizzano la gerarchia descritta utilizzando una classe astratta Prodotto.
Implementare il metodo str() e la riscrittura del metodo eq() per il confronto di prodotti uguali.
Scrivere un main che crea diversi tipi di prodotto e si possano comparare per sapere se sono uguali.

prodotto
    code
    nome
    descrizione
    prezzo
    quantita

alimento
    scadenza
    sonto (if quantita minima > 5)10%

non alimenti
    categoria
    peso
    tassa aggiuntiva(10% si no)


1) Crea prodotto
2) Compara prodotti
3) Stampa elenco prodotti e il costo totale
4) Stampa elenco prodotti per categoria
5) Stampa elenco prodotti in ordine di prezzo
6) Stampa elenco prodotti con sconto
7) Stampa elenco prodotti scaduti
8) Stampa elenco prodotti soggetti a tassa aggiuntiva.
Consigli per la soluzione:
usare classe astratta Prodotto e classi ProdottoAlimentare, ProdottoNonAlimentare che ereditano da Prodotto.
Creare metodo astratto calcola_prezzo() per calcolare prezzo di ogni prodotto.
Utilizzare la libreria datetime per gestire le date di scadenza dei prodotti alimentari.
