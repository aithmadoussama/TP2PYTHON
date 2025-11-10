
class CompteBancaire :
    
    def __init__(self, titulitaire, solde = 0):
        self._titulaire  = titulitaire
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
    
    @property 
    def solde(self):
        return self.__solde 
    
    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"
