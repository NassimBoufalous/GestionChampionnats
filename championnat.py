class Championnat:
    def __init__(self, nom, date_debut, date_fin, points_gagnes, points_perdus, points_nuls):
        self.id = None
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.points_gagnes = points_gagnes
        self.points_perdus = points_perdus
        self.points_nuls = points_nuls
        self.equipes = []
        self.matchs = []

    def ajouter_equipe(self, equipe):
        self.equipes.append(equipe)

    def ajouter_match(self, match):
        self.matchs.append(match)
