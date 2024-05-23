# Importare la classe Dictionary dal file dictionary.py per avere le sue funzionalità all'interno di questo file

from dictionary import Dictionary

# Definire la classe Translator
class Translator:

    # Definire il metodo __init__ inizializzando un dizionario tramite la classe Dictionary()
    def __init__(self):
        self.dizionario = Dictionary()


    # Definire il metodo __str__ (che potrebbero sempre servire nei test che vengono svolti nella fase di realizzazione
    # del programma)
    def __str__(self):
        return f'{self.dizionario}'


    # Definire il metodo __repr__ (che potrebbero sempre servire nei test che vengono svolti nella fase di realizzazione
    # del programma)
    def __repr__(self):
        return f'{self.dizionario}'


    # Definire il metodo printMenu che stampa il menù iniziale secondo la formattazione richiesta dal testo dell'
    # esercizio
    def printMenu(self):
        print("-----------------------------")
        print("Translator Alien-Italian")
        print("-----------------------------")
        print("1. Aggiungi una nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("-----------------------------")


    # Definire il metodo loadDictionary che permette di fare il load del dizionario tramite il metodo load_dictionary()
    # introdotto e inizializzato all'interno della classe Dictionary()
    def loadDictionary(self):
        return self.dizionario.load_dictionary()


    # Definire il metodo handleAdd che permette di aggiungere una parola aliena e la relativa traduzione al dizionario
    # e al file dictionary.txt tramite il metodo addWord() introdotto e inizializzato all'interno della classe
    # Dictionary()
    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        return self.dizionario.addWord(entry)


    # Definire il metodo handleTranslate che permette di stampare la traduzione di una parola aliena in lingua umana
    # tramite il metodo translate() introdotto e inizializzato all'interno della classe Dictionary()
    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.dizionario.translate(query)


    # Definire il metodohandleWildCard che permette data la wildcard di stampare la parola aliena e la sua relativa
    # traduzione in lingua umana tramite il metodo translateWordWildCard introdotto e inizializzato all'interno della
    # classe Dictionary()
    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.dizionario.translateWordWildCard(query)


    # Definire un metodo printDictionary che stampa tutto il contenuto del file dictionary.txt tramite il metodo
    # print_dictionary() introdotto e inizializzato all'interno della classe Dictionary()
    def printDictionary(self):
        return self.dizionario.print_dictionary()