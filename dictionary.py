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
                    self.dizionario[parole[0]] = parole[1]


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
            # Se la lunghezza delle parole è due, allora è possibile aggiungere la parola aliena e la sua traduzione:
            # aggiornare, quindi, il dizionario dell'oggetto indicando con la prima parola, ossia la parola la chiave del
            # dizionario e con la seconda parola, ossia la parola umana, il valore della chiave prima usata
            if len(parole) == 2:
                self.dizionario[parole[0]] = parole[1]
                # Aggiunta la parola, si può successivamente anche aggiornare il file dictionary.txt aggiungendo la parola
                # aliena e la sua relativa traduzione semplicemente vedendoli non come elementi di un dizionario Python, ma
                # come elementi di una lista
                with open("dictionary.txt", "a") as file:
                    file.write(f'\n{parole[0]} {parole[1]}')
        else:
            print(ValueError(f'La parola inserita non è valida!'))


    # Definire un metodo translate il quale data una parola aliena ne trovi la corrispondente traduzione in lingua
    # umana
    def translate(self, parola_aliena_da_tradurre):
        # Se la parola aliena che bisogna tradurre è presente all'interno del dizionario, allora ne verrà stampata la
        # traduzione, altrimenti verrà stampato il seguente messaggio "La parola aliena cercata non esiste oppure non
        # è stata trovata la sua traduzione in lingua umana"
        if parola_aliena_da_tradurre in self.dizionario:
            print(self.dizionario[parola_aliena_da_tradurre])
        else:
            print("La parola aliena cercata non esiste oppure non è stata trovata la sua traduzione in lingua umana")

    #
    def translateWordWildCard(self):
        pass

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