from CompteBancaire import CompteBancaire 

compte = CompteBancaire("Ali", 1000)
compte.deposer(200)
compte.retirer(150)
print(compte)
print("Solde accessible (lecture) :", compte.solde)

# Tentative de modification directe
# compte.solde = 500  # Ne fonctionnera pas