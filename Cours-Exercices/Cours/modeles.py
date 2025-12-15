# Fichier d'exemple de modèles de conception

# Singleton pattern
class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
# Utilisation
a = Singleton()
b = Singleton()

print(a is b)


# Factory pattern
class Chien():
    def parler(self):
        return "Wouf!"
    

class Chat():
    def parler(self):
        return "Miaou!"
    

def animal_factory(animal_type: str):
    match (animal_type.lower()):
        case "chien": return Chien()
        case "chat":  return Chat()

# Utilisation
animal = animal_factory("Chien")
print(animal.parler())


# Observer pattern
class Sujet:
    def __init__(self):
        self.__observateurs: list[Observateur] = []
    
    def attache(self, observateur):
        self.__observateurs.append(observateur)

    def notification(self, message):
        for observateur in self.__observateurs:
            observateur.maj(message)


class Observateur:
    def __init__(self, nom):
        self.__nom = nom

    def maj(self, message):
        print(f"{self.__nom} à recu :", message)

# Utilisation
sujet = Sujet()
observateur1 = Observateur("Obs1")
observateur2 = Observateur("Obs2")
sujet.attache(observateur1)
sujet.attache(observateur2)

sujet.notification("Changement d'état.")


# Strategy pattern
class Context:
    def __init__(self, strategie):
        self.__strategie = strategie

    def execute(self, donnee):
        return self.__strategie(donnee)
    
    @property
    def strategie(self):
        return self.__strategie
    
    @strategie.setter
    def strategie(self, nouvelle_strategie):
        self.__strategie = nouvelle_strategie


def strategy_upper(texte: str):
    return texte.upper()

def strategy_lower(texte: str):
    return texte.lower()

# Utilisation
ctx = Context(strategy_upper)
print(ctx.execute("Hello"))
ctx.strategie = strategy_lower
print(ctx.execute("Hello"))
