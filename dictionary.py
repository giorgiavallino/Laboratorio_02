# Definire la classe Dictionary
class Dictionary:

    # Definire il metodo __init__
    def __init__(self):
        self.dizionario = {}

    # Definire il metodo __str__
    def __str__(self):
        return f'{self.dizionario}'

    # Definire il metodo __repr__
    def __repr__(self):
        return f'{self.dizionario}'

    # Definire il metodo load_dictionary che permette di caricare e visualizzare il dizionario
    def load_dictionary(self):
        with open("dictionary.txt", "r") as file:
            for linea in file:
                parole = linea.strip().split()
                print(parole)
                if len(parole) == 2:
                    self.dizionario[parole[0]] = parole[1]
            print(self.dizionario)


    def addWord(self, parole_da_aggiungere):
        print(parole_da_aggiungere)
        # if len(parole_da_aggiungere) == 2:
            # self.dizionario[parole_da_aggiungere[0]] = parole_da_aggiungere[1]

    # Definire un metodo translate il quale data una parola aliena ne trovi la corrispondente traduzione in lingua
    # umana
    def translate(self, parola_aliena_da_tradurre):
            return print(self.dizionario[parola_aliena_da_tradurre])

    def translateWordWildCard(self):
        pass

p = Dictionary()
p2 = input("")
p.addWord(p2)

