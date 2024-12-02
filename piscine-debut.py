liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
listeNageur = []
listeNage = []
listeLongueur = []
commande = ''

def cmd_nouvelleindividu(listeNageur):
    """Ajoute un nouveau nageur"""
    prénom = input("Prénom du nouveau nageur ? ")
    id= len(listeNageur)+1
    listeNageur.append( (id,prénom))
    print(listeNageur)

def cmd_nouvellenage(listeNage):
    """Ajoute une nouvelle nage"""
    nage = input("Nom de la nouvelle nage ? ")
    id= len(listeNage)+1
    listeNage.append( (id,nage))
    print(listeNage)

def cmd_nouvellelongueur(listeLongueur):
    """Ajoute combien de longueur"""
    longueur = input("Combien de longueur ? ")
    id= len(listeLongueur)+1
    listeLongueur.append( (id,longueur))
    print(listeLongueur)

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

def cmd_save(liste, filename):
    """Sauvegarde le tableau"""
    fichier = open(filename, 'w')
    for elt in liste:
        fichier.write(elt[0]+','+elt[1]+','+str(elt[2])+"\n")
    fichier.close()

def cmd_load(liste, filename):
    """Charge la sauvegarde"""
    fichier = open(filename, 'r')
    for line in fichier:
        line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0]=='#':
            continue
        tmp = line.split(',')
        liste.append(tuple(tmp))
    fichier.close()

def cmd_exit():
    """Fini la boucle"""
    temp= input('En êtes-vous sûr ? (o)ui/(n)on ?')
    if temp =='o':
        cmd_save(liste, 'save.backup')
        return False
    else :
        return True

isAlive = True
while isAlive:
    commande = input("Que faut-il faire ? ")

    if commande == 'ajout':
        cmd_ajout(liste)
        continue

    if commande == 'newindividu':
        cmd_nouvelleindividu(listeNageur)
        continue
    
    if commande == 'newnage':
        cmd_nouvellenage(listeNage)
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

    if commande == "save":
        cmd_save(liste, "save.csv")
        continue

    if commande == "load":
        cmd_load(liste, "save.csv")
        continue

    if commande == "exit":
        isAlive = cmd_exit(liste)
        continue

    print(f"Commande {commande} inconnue")