class CompteBancaire :
    
    def __init__(self, solde = 0):
        self.__solde = solde
    
    def deposer(self, montant):
        if(montant > 0):
            self.__solde += montant 
        else :
            print("Montant invalide.")
    
    def retirer(self, montant):
        if(0 < montant <= self.__solde):
            self.__solde -= montant
        else :
            print("Fonds insuffisants ou montant invalide.")
    
    def get_solde(self):
        return self.__solde 
    
    