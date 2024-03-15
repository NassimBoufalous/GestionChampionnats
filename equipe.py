
class Equipe:
    def __init__(self, nom, date_creation,matchs_joues,matchs_gagnes,matchs_nuls, stade,points, entraineur, president):
        self.id = None
        self.nom = nom
        self.matchs_joues = matchs_joues
        self.matchs_gagnes = matchs_gagnes
        self.matchs_nuls = matchs_nuls
        self.date_creation = date_creation
        self.stade = stade
        self.points=points
        self.entraineur = entraineur
        self.president = president

    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Date de création : {self.date_creation}")
        print(f"Stade : {self.stade}")
        print(f"Entraîneur : {self.entraineur}")
        print(f"Président : {self.president}")
        print(f"Matchs Joués : {self.matchs_joues}")
        print(f"Matchs Gagnés : {self.matchs_gagnes}")
        print(f"Matchs Nuls : {self.matchs_nuls}")
       