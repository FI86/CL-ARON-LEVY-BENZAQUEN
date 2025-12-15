# Exercice modèle de conception

# Créer une interface appelée StrategiePaiement avec une méthode payer(montant).
# Implémenter plusieurs stratégies concrètes :
#     PaiementCarte
#     PaiementPayPal
#     PaiementCrypto
# Créer une classe GestionnairePaiement qui utilise une stratégie de paiement et peut en changer avec changer_strategie().
# Ajoute un système de confirmation de commande (affiche un message avant d’appeler la méthode payer).


# Interface de strategie
class StrategiePaiement:
    def payer(self, montant):
        raise NotImplementedError("Cette méthode doit être redéfinie")


# Strategies concretes
class PaiementCarte(StrategiePaiement):
    def payer(self, montant):
        print(f"Paiement de {montant}€ par carte de crédit effectué.")


class PaiementPayPal(StrategiePaiement):
    def payer(self, montant):
        print(f"Paiement de {montant}€ via PayPal effectué.")


class PaiementCrypto(StrategiePaiement):
    def payer(self, montant):
        print(f"Paiement de {montant}€ en cryptomonnaie confirmé.")


# Contexte qui utilise une strategie
class GestionnairePaiement:
    def __init__(self, strategie: StrategiePaiement):
        self.strategie = strategie

    def changer_strategie(self, strategie: StrategiePaiement):
        self.strategie = strategie

    def passer_commande(self, montant):
        self.strategie.payer(montant)


# Utilisation
if __name__ == "__main__":
    paiement = GestionnairePaiement(PaiementCarte())
    paiement.passer_commande(100)

    paiement.changer_strategie(PaiementPayPal())
    paiement.passer_commande(50)

    paiement.changer_strategie(PaiementCrypto())
    paiement.passer_commande(200)
