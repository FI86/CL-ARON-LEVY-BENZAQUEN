# Exercice propriete, encapsulation et destructeur
# Créez une classe Animal :
#     Attributs privés : __nom, __age
#     Propriétés pour accéder et modifier nom et age avec vérification (âge >= 0).
#     Une méthode parler() qui affiche "L'animal fait un bruit."
#     Un destructeur (__del__) qui affiche :
#     "{nom} a été retiré du zoo."
# Créez deux classes filles :
#     Chien, redéfinit parler() → affiche "{nom} aboie : Woof!"
#     Chat,  redéfinit parler() → affiche "{nom} miaule : Miaou!"
# Créez une fonction faire_parler(animaux) qui prend une liste d’objets Animal et appelle leur méthode parler().


# Classe Animal
class Animal:
    # Constructeur
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    # Proprietes
    @property
    def nom(self):
        return self.__nom

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("L'âge ne peut pas être négatif.")
        self.__age = value

    # Methode parler
    def parler(self):
        print("L'animal fait un bruit.")

    # Destructeur
    def __del__(self):
        print(f"{self.nom} a été retiré du zoo.")


# Classe Chien
class Chien(Animal):
    def parler(self):
        print(f"{self.nom} aboie : Woof!")


# Classe Chat
class Chat(Animal):
    def parler(self):
        print(f"{self.nom} miaule : Miaou!")


# Fonction qui fait parler un animal
def faire_parler(animal: Animal) -> None:
        animal.parler()


# Programme principal
if __name__ == "__main__":
    animal = Animal("toto", 4)
    rex = Chien("Rex", 5)
    minou = Chat("Minou", 3)
    faire_parler(animal)
    faire_parler(rex)
    faire_parler(minou)

    # La fin de programme Déclenche le destrcuteur __del__ pour chaque objet crée.