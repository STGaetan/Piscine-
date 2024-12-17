liste = [(1,3,10),(2,1,13),(3,2,6), (3,1,8) ]
listeNageur = [(1, "Pierre"), (2, "Paul"), (3, "Léa")]
listeNages = [(1, 'Brasse'), (2, 'Crawl'), (3, "dos")]
commande = ''

def get_str_from_num_in_list(num, liste):
    """Retourne une str d'un nbr dans une liste"""
    for elt in liste:
        if elt[0]==num:
            return elt[1]
    return "unknown"

def cmd_individu(listeNageur):
    """Ajoute un nouveau nageur"""
    prénom = input("Prénom du nouveau nageur ? ")
    id= len(listeNageur)+1
    listeNageur.append( (id,prénom))
    print(listeNageur)

def cmd_nouvellenage(listeNages):
    """Ajoute une nouvelle nage"""
    nage = input("Quelle nage enregistrer ? ")
    id= len(listeNages)+1
    listeNages.append( (id,nage))
    print(listeNages)

def cmd_ajout(liste):
    """Ajoute un évenement à la liste"""
    for elt in listeNageur:
        print(f"{elt[0]:5} : {elt[1]}")
    a = int(input("Nageur n° ? "))
    for elt in listeNages:
        print(f"{elt[0]:5} : {elt[1]}")
    b = int(input("Nage n° ? "))
    c = int(input("combien de longueur ? "))
    liste.append((a,b,c))

def cmd_liste(liste):
    """Affiche tous les performances des nageurs"""
    print("Prénom       |   nage    |   longueur")
    print("-------------------------------------")
    for elt in liste:
        print(f" {elt[0]:13}| {elt[1]:13}|  {elt[2]}")

def cmd_nageur(liste):
    """Affiche tableau d'un nageur"""
    for elt in listeNageur:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = int(input("Quel numéro de nageur ? "))
    print("Performances de ", tmp)
    print("   nage    |   longueur")
    print("-----------------------")
    for elt in liste:
        if elt[0] == tmp:
            print(f" {elt[1]:10}|   {elt[2]}")

def cmd_nage(liste):
    """Affiche tableau des nages"""
    for elt in listeNages:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = int(input("Quel numéro de nage ? "))
    print("Nage ", tmp)
    print("   Nageur   |   Longueur")
    print("------------------------")
    for elt in liste:
        if elt[1] == tmp:
            print(f" {elt[0]:11}|   {elt[2]}")

def cmd_save(liste, filename):
    """Sauvegarde le tableau"""
    fichier = open(filename, 'w')
    for elt in liste:
       fichier.write(str(elt[0])+','+str(elt[1])+','+str(elt[2])+"\n")
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

    if commande == 'individu':
        cmd_individu(listeNageur)
        continue
    
    if commande == 'nouvelle nage':
        cmd_nouvellenage(listeNages)
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