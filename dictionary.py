# Importare la libreria re di cui si utilizzerà la funzione search

import re

# Definire la classe Dictionary

class Dictionary:

    # Definire il metodo __init__ che presenta inizialmente come parametri un dizionario che viene creato utilizzando
    # un dizionario Python vuoto
    def __init__(self):
        self.dizionario = {}


    # Definire il metodo __str__ (che potrebbero sempre servire nei test che vengono svolti nella fase di realizzazione
    # del programma)
    def __str__(self):
        return f'{self.dizionario}'


    # Definire il metodo __repr__ (che potrebbero sempre servire nei test che vengono svolti nella fase di realizzazione
    # del programma)
    def __repr__(self):
        return f'{self.dizionario}'


    # Definire il metodo load_dictionary che permette di caricare e visualizzare il dizionario
    def load_dictionary(self):
        # Aprire il file in modalità lettura
        with open("dictionary.txt", "r") as file:
            # Per ogni linea del file dividere le parole contenute al suo interno usando split() e eliminando gli spazi
            # iniziali e finali usando strip()
            for linea in file:
                parole = linea.strip().split()
                # se le parole per ogni riga sono due, allora aggiornare il dizionario dell'oggetto indicando con la
                # prima parola di ogni riga, ossia la parola aliena, la chiave del dizionario e con la seconda parola
                # di ogni riga, ossia la parola umana, il valore della chiave prima usata
                if len(parole) == 2:
                    chiave = parole[0].lower()
                    valore = parole[1].lower()
                    self.dizionario[chiave] = valore


    # Definire un metodo addWord che aggiunge la parola aliena e la sua relativa traduzione in lingua umana aggiornando,
    # inoltre, il file dictionary.txt aggiungendo tali componenti nuovi
    def addWord(self, parole_da_aggiungere):
        # Verificare che le parole da aggiungere siano parole costituite da lettere (maiuscole o minuscole)
        # dell'alfabeto: quindi, eliminare gli spazi tra le parole tramite replace e verificare la condizione richiesta
        # tramite isalpha()... se la condizione è vera, allora si può proseguire all'aggiunta delle parole nel
        # dizionario, altrimenti verrà restituita la print con scritto "La parola inserita non è valida"
        parole_da_aggiungere_divise = parole_da_aggiungere.replace(" ", "")
        if parole_da_aggiungere_divise.isalpha() == True:
            # Dividere la stringa parole_da_aggiungere usando split() ed eliminando eventuali spazi iniziali e finali della
            # medesima stringa
            parole = parole_da_aggiungere.strip().split()
            # Affinché la ricerca sia case insensitive, conviene richiedere che la prima parola della lista parole
            # (ossia la parola aliena da aggiungere) sia minuscola come tutte le parole che si trovano nel
            # self.dizionario
            parola_aliena_minuscola = parole[0].lower()
            # Se la lunghezza delle parole è due, allora è possibile aggiungere la parola aliena e la sua traduzione:
            # aggiornare, quindi, il dizionario dell'oggetto indicando con la prima parola, ossia la parola la chiave del
            # dizionario e con la seconda parola, ossia la parola umana, il valore della chiave prima usata
            if len(parole) == 2:
                # Se la parola aliena minuscola non si trova già all'interno del dizionario, allora non siamo nel caso
                # delle traduzioni multiple
                if parola_aliena_minuscola not in self.dizionario:
                    self.dizionario[parole[0]] = parole[1]
                    # Aggiunta la parola, si può successivamente anche aggiornare il file dictionary.txt aggiungendo la
                    # parola aliena e la sua relativa traduzione attraverso la funzione write()
                    with open("dictionary.txt", "a") as file:
                        file.write(f'\n{parole[0]} {parole[1]}')
                # Se la parola aliena si trova già all'interno del dizionario, allora siamo nel caso delle
                # traduzioni multiple

                # DA FARE !!!

        # Se la parola inserita non è costituita solo da caratteri alfabetici, allora stampa l'errore
        else:
            print(ValueError(f'La parola inserita non è valida!'))


    # Definire un metodo translate il quale data una parola aliena ne trovi la corrispondente traduzione in lingua
    # umana
    def translate(self, parola_aliena_da_tradurre):
        # Se la parola aliena che bisogna tradurre è presente all'interno del dizionario, allora ne verrà stampata la
        # traduzione, altrimenti verrà stampato il seguente messaggio "La parola aliena cercata non esiste oppure non
        # è stata trovata la sua traduzione in lingua umana"
        # Si ricorda, inoltre, che bisogna rendere case insensitive la ricerca della traduzione... la parola aliena da
        # tradurre dovrà quindi essere minuscola come tutte le parole del self.dizionario
        parola_aliena_da_tradurre_minuscola = parola_aliena_da_tradurre.lower()
        if parola_aliena_da_tradurre_minuscola in self.dizionario:
            print(f'Parola aliena: {parola_aliena_da_tradurre}, traduzione: {self.dizionario[parola_aliena_da_tradurre_minuscola]}')
        else:
            print("La parola aliena cercata non esiste oppure non è stata trovata la sua traduzione in lingua umana")


    # Definire un metodo translateWordWildCard il quale data una parola aliena contenente un punto di domanda al suo
    # interno al posto di un carattere, ne restituisca la traduzione in lingua umana andando a sostituire alla
    # parola aliena ogni carattere per trovarne il corrispettivo esistente
    def translateWordWildCard(self, wildcard):
        # Se c'è più di un punto interrogativo, allora la parola inserita dall'utente non è valida
        if wildcard.count("?") > 1:
            print(ValueError("L'input inserito non è valido... la wildcard deve contenere soltanto un carattere speciale '?'"))
        # Se il punto interrogativo è solo uno, allora si può procedere con l'esecuzione del codice
        elif wildcard.count("?") == 1:
            # Per utilizzare la funzione search della libreria re bisogna sostituire il punto di domanda presente nella
            # parola aliena inserita dall'utente con un semplice punto
            wildcard_puntata = wildcard.replace("?", ".")
            # Essendo le parole contenute nel self.dizionario tutte minuscole, bisogna richiedere che anche la wildcard
            # lo sia
            wildcard_puntata_minuscola = wildcard_puntata.lower()
            # Per ogni chiave del dizionario, richiedere la condizione di ricerca della traduzione della parola aliena
            for chiave in self.dizionario.keys():
                # Definire una lista vuota chiamata traduzioni
                traduzioni = []
                # La funzione search della libreria re cambia il punto in ogni carattere alfabetico possibile e ricerca
                # il suo corrispotivo per ogni chiave del dizionario
                if re.search(wildcard_puntata_minuscola, chiave):
                    # Inizializzare la variabile traduzione che rappresenta il valore della chiave del dizionario
                    traduzione = self.dizionario.get(chiave)
                    # Aggiungere tale traduzione all'interno della lista traduzioni
                    traduzioni.append(traduzione)
                # Se la lista traduzioni è diversa dalla lista vuota, allora il programma riscrive la lista come
                # una stringa (ossia senza parentesi quadre e virgolette) e ne stampa la relativa traduzione
                # tramite l'apposita print in cui vengono stampate anche la wildcard e la parola aliena rispettiva
                if traduzioni != []:
                    traduzioni_stringa = " ".join(traduzioni)
                    print(f'Data la parola aliena tramite wildcard {wildcard}, la parola aliena trovata è {chiave} e la corrispettiva traduzione in lingua italiana è {traduzioni_stringa}')


    # Definire un metodo print_dictionary che stampa tutto il dizionario contenuto nel file dictionary.txt
    def print_dictionary(self):
        # Aprire il file dictionary.txt
        with open("dictionary.txt", "r") as file:
            # Per ogni linea del file dividere le parole contenute al suo interno usando split() e eliminando gli spazi
            # iniziali e finali usando strip()
            for linea in file:
                parole = linea.strip().split()
                # Associare la prima parola di ogni riga alla variabile parola_aliena e la seconda parola di ogni
                # riga alla variabile parola_umana
                parola_aliena = parole[0]
                parola_umana = parole[1]
                # Stampare la seguente print in maniera tale da visualizzare tutto il dizionario con ogni parola aliena
                # e la sua relativa traduzione in lingua umana
                print(f'Parola aliena: {parola_aliena}, parola umana: {parola_umana}')