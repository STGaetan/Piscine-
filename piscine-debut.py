liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''
isAlive = True

def cmd_ajout(liste):
    """Ajoute un évenement à la liste"""
    a = input("Qui nage ? ")
    b = input("quelle nage ? ")
    c = input("combien de longueur ? ")
    liste.append((a,b,c))

def cmd_liste(liste):
    """Affiche tous les performances des nageurs"""
    for elt in liste:
        print(f"Prénom : {elt[0]}, Type de nage : {elt[1]}, Combien de longueur : {elt[2]}")

def cmd_exit():
    """Fini la boucle"""
    temp= input('En êtes-vous sûr ? (o)ui/(n)on ?')
    if temp =='o':
        return False
    else :
        return True
        
while isAlive:
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        cmd_ajout(liste)
        continue
   
    if commande == 'liste':
        cmd_liste(liste)
        continue

    if commande == "exit":
        isAlive = cmd_exit()
        continue

    print(f"Commande {commande} inconnue")