
from championnat import Championnat
from equipe import Equipe
from match import Match

def afficher_menu():
    print("Menu :")
    print("1. Ajouter un championnat")
    print("2. Ajouter une équipe")
    print("3. Saisir le résultat d'un match")
    print("4. Afficher les championnats")
    print("5. Afficher la liste des équipes d'un championnat")
    print("6. Afficher le classement d'un championnat")
    print("7. Quitter l'application")



def ajouter_championnat(championnats):
    nom = input("Nom du championnat : ")
    date_debut = input("Date de début : ")
    date_fin = input("Date de fin : ")
    points_gagnes = input("Points pour une victoire : ")
    points_perdus = input("Points pour une défaite : ")
    points_nuls = input("Points pour un match nul : ")
    championnat = Championnat(nom, date_debut, date_fin, points_gagnes, points_perdus, points_nuls)
    championnats.append(championnat)
    championnat.id = len(championnats)

def ajouter_equipe(championnats):
    afficher_championnats(championnats)
    championnat_id = int(input("ID du championnat : "))
    nom = input("Nom de l'équipe : ")
    date_creation = input("Date de création : ")
    stade = input("Stade : ")
    entraineur = input("Entraîneur : ")
    president = input("Président : ")
    equipe = Equipe(nom, date_creation,0,0,0, stade, 0,entraineur, president)
    championnats[championnat_id-1].ajouter_equipe(equipe)
    equipe.id = len(championnats[championnat_id-1].equipes)

def saisir_resultat_match(championnats):
    afficher_championnats(championnats)
    championnat_id = int(input("ID du championnat : "))
    numero_journee = input("Numéro de journée : ")
    equipe1_id = int(input("ID de l'équipe 1 : "))
    equipe2_id = int(input("ID de l'équipe 2 : "))
    score_equipe1 = int(input("Score de l'équipe 1 : "))
    score_equipe2 = int(input("Score de l'équipe 2 : "))
    equipe2 = championnats[championnat_id - 1].equipes[equipe2_id - 1]
    equipe1 = championnats[championnat_id - 1].equipes[equipe1_id - 1]
    match = Match(numero_journee, equipe1_id, equipe2_id, score_equipe1, score_equipe2)

    if score_equipe1 > score_equipe2:
        equipe1.matchs_gagnes += 1
        equipe1.points+=int(championnats[championnat_id-1].points_gagnes)
        equipe1.matchs_joues+=1
        equipe2.matchs_joues+=1
        equipe2.points+=int(championnats[championnat_id-1].points_perdus)
    elif score_equipe1 < score_equipe2:
        equipe2.matchs_gagnes += 1
        equipe2.points+=int(championnats[championnat_id-1].points_gagnes)
        equipe2.matchs_joues+=1
        equipe1.matchs_joues+=1
        equipe1.points+=int(championnats[championnat_id-1].points_perdus)
    else:
        equipe1.matchs_nuls += 1
        equipe1.points+=int(championnats[championnat_id-1].points_nuls)
        equipe2.matchs_nuls += 1
        equipe1.points+=int(championnats[championnat_id-1].points_nuls)
        equipe1.matchs_joues += 1
        equipe2.matchs_joues += 1

    championnats[championnat_id - 1].ajouter_match(match)
    match.id = len(championnats[championnat_id - 1].matchs)

def afficher_championnats(championnats):
    print("Liste des championnats :")
    for index, championnat in enumerate(championnats, start=1):
        print(f"{index}. ID : {championnat.id}, Nom : {championnat.nom}")

def afficher_equipes(championnats):
    afficher_championnats(championnats)
    championnat_id = int(input("Entrez le numéro du championnat : "))
    championnat = championnats[championnat_id - 1]
    print(f"Équipes du championnat {championnat.nom} :")
    for equipe in championnat.equipes:
        print(f"{equipe.id}. {equipe.nom}")

def afficher_matchs(championnats):
    championnat_id = int(input("ID du championnat : "))
    print("Liste des matchs :")
    for match in championnats[championnat_id - 1].matchs:
        print(f"Équipe 1 : {match.equipe1}, Équipe 2 : {match.equipe2}, Score : {match.score_equipe1}-{match.score_equipe2}")

def calculer_classement(championnat):
    classement = sorted(championnat.equipes, key=lambda equipe: (equipe.points, equipe.matchs_gagnes, equipe.matchs_nuls), reverse=True)
    return classement

def afficher_classement(championnats):
    afficher_championnats(championnats)
    championnat_id = int(input("ID du championnat : "))
    championnat = championnats[championnat_id - 1]
    classement = calculer_classement(championnat)
    print(f"Classement du championnat {championnat.nom}:")
    print("Classement | Nom            | Matchs Joués | Matchs Gagnés | Matchs Nuls | Points")
    for index, equipe in enumerate(classement, start=1):
        print("{:<10} | {:<15} | {:<12} | {:<14} | {:<11} | {}".format(
            index, equipe.nom, equipe.matchs_joues, equipe.matchs_gagnes, equipe.matchs_nuls, equipe.points))
def main():
    championnats =[]
    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_championnat(championnats)
        elif choix == "2":
            ajouter_equipe(championnats)
        elif choix == "3":
            saisir_resultat_match(championnats)
        elif choix == "4":
            afficher_championnats(championnats)
        elif choix == "5":
            afficher_equipes(championnats)
        elif choix == "6":
            afficher_classement(championnats)
        elif choix == "7":
            print("Merci d'avoir utilisé l'application. À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")

if __name__ == "__main__":
    main()