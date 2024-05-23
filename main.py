# Importare il file translator come tr

import translator as tr

# Inizializzare la variabile t appartenente alla classe Translator

t = tr.Translator()

while(True):

    # Implementare il metodo printMenu che permette di stampare il menù tramite il quale è possibile scegliere
    # il numero dell'azione che l'utente deciderà di svolgere

    t.printMenu()

    # Implementare il metodo loadDictionary che permette di caricare il dizionario

    t.loadDictionary()

    # Chiedere all'utente il numero dell'azione che vuole svolgere

    numero = input("Inserisci il numero dell'operazione che vuoi svolgere: ")

    # Introdurre un insieme di condizioni if mediante le quali è possibile svolgere le rispettive funzionalità

    # Se il numero inserito corrisponde a caratteri alfabetici, allora il programma viene bloccato poiché quanto
    # inserito dall'utente non rispecchia quanto richiesto dal codice stesso... il codice continuerà a stampare il menù
    # iniziale tramite il metoodo printMenu e continuerà a chiedere l'inserimento di un input numerico fino a che
    # l'utente non inserirà il valore corretto per il giusto funzionamento del programma
    if numero.isnumeric() == False:
        while numero.isnumeric() == False:
            t.printMenu()
            print(ValueError(f'Non è stato inserito un numero, ma sono state inserite delle lettere... riprovare!'))
            numero = input("Inserisci il numero dell'operazione che vuoi svolgere: ")


    # Se il numero inserito dall'utente è maggiore di 5 o minore di 1, allora il valore immesso non corrisponde a
    # nessuna funzione e, quindi, bisognerà fornire un nuovo numero al quale viene associata un'operazione
    if int(numero) > 5 and int(numero) < 1:
        print(ValueError("Il numero inserito non è adatto allo svolgimento del programma"))


    # Se il numero inserito dall'utente è uno, allora la funzione richiesta è "Aggiungi una parola"
    if int(numero) == 1:
        # Richiedere le parole da aggiungere
        da_aggiungere = input("Inserisci la parola aliena da aggiungere e la relativa traduzione: ")
        # Aggiungere la parola aliena con la sua relativa traduzione
        t.handleAdd(da_aggiungere)


    # Se il numero inserito dall'utente è due, allora la funzione richiesta è "Cerca una traduzione"
    if int(numero) == 2:
        # Richiedere la parola aliena da tradurre
        da_tradurre = input("Inserisci la parola aliena da tradurre: ")
        # Tradurre la parola aliena usando il rispettivo metodo handleTranslate()
        t.handleTranslate(da_tradurre)


    # Se il numero inserito dall'utente è tre, allora la funzione richiesta è "Cerca con wildcard"
    if int(numero) == 3:
        # Richiedere la wildcard in lingua aliena da tradurre
        da_tradurre_con_wildcard = input("Inserisci la parola aliena da tradurre con wildcard: ")
        # Trovare la parola aliena corrispondente alla wildcard e la sua relativa traduzione in lingua umana
        # attraverso il metodo handleWildCard
        t.handleWildCard(da_tradurre_con_wildcard)


    # Se il numero inserito dall'utente è quattro, allora la funzione richiesta è "Stampa tutto il dizionario"
    if int(numero) == 4:
        print("Ecco il dizionario stampato!")
        # Il dizionario viene stampato mediante il rispettivo metodo printDictionary()
        t.printDictionary()


    # Se il numero inserito dall'utente è cinque, allora la funzione richiesta è "Exit" che viene tradotta in codice
    # Python mediante il relativo comando break
    if int(numero) == 5:
        break