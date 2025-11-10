from Client import Client 
from CompteBancaire import CompteBancaire

cli = Client("Yassir")
cli.compte.deposer(300)
cli.compte.retirer(50)
cli.afficher()

