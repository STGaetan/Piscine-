liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''

def cmd_ajout(liste):
    """Ajoute un évenement à la liste"""
    a = input("Qui nage ? ")
    b = input("quelle nage ? ")
    c = input("combien de longueur ? ")
    liste.append((a,b,c))

def cmd_liste(liste):
    """Affiche tous les performances des nageurs"""
    print("Prénom       |   nage    |   longueur")
    print("-------------------------------------")
    for elt in liste:
        print(f" {elt[0]:13}| {elt[1]:13}|  {elt[2]}")

def cmd_nageur(liste):
    """Affiche tableau d'un nageur"""
    qui = input("Quel nageur ? ")
    print("Performances de ", qui)
    print("   nage    |   longueur")
    print("-----------------------")
    for elt in liste:
        if elt[0] == qui:
            print(f" {elt[1]:10}|   {elt[2]}")

def cmd_nage(liste):
    """Affiche tableau des nages"""
    quel= input("Quel type de nage ? ")
    print("Nage ", quel)
    print("   Nageur   |   Longueur")
    print("------------------------")
    for elt in liste:
        if elt[1] == quel:
            print(f" {elt[0]:11}|   {elt[2]}")

def cmd_exit():
    """Fini la boucle"""
    temp= input('En êtes-vous sûr ? (o)ui/(n)on ?')
    if temp =='o':
        return False
    else :
        return True
        
isAlive = True
while isAlive:
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        cmd_ajout(liste)
        continue
   
    if commande == 'liste':
        cmd_liste(liste)
        continue

    if commande == 'nageur':
        cmd_nageur(liste)
        continue

    if commande == "nage":
        cmd_nage(liste)
        continue

    if commande == "exit":
        isAlive = cmd_exit()
        continue

    print(f"Commande {commande} inconnue")