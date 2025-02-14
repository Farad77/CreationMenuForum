import random
from datetime import datetime, timedelta
import csv

# Listes de données
NOMS = ['Martin', 'Bernard', 'Thomas', 'Petit', 'Robert', 'Richard', 'Durand', 'Dubois', 'Moreau', 'Laurent',
        'Simon', 'Michel', 'Lefebvre', 'Leroy', 'Roux', 'David', 'Bertrand', 'Morel', 'Fournier', 'Girard']

PRENOMS = ['Jean', 'Pierre', 'Michel', 'André', 'Philippe', 'René', 'Louis', 'Alain', 'Jacques', 'Bernard',
           'Marie', 'Jeanne', 'Catherine', 'Françoise', 'Anne', 'Monique', 'Isabelle', 'Sophie', 'Martine', 'Nicole']

NIVEAUX = ['6eme', '5eme', '4eme', '3eme']
CLASSES = ['A', 'B', 'C', 'D', 'E']
PROGRAMMES = [f'Programme {i}' for i in range(1, 8)]  # Programme 1 à 7

def generer_date_aleatoire():
    """Génère une date aléatoire entre le 1er et le 14 février 2025"""
    debut = datetime(2025, 2, 1)
    fin = datetime(2025, 2, 14)
    delta = fin - debut
    intervalle_aleatoire = random.random() * delta.total_seconds()
    date_aleatoire = debut + timedelta(seconds=intervalle_aleatoire)
    return date_aleatoire.strftime('%Y-%m-%d %H:%M:%S')

def generer_voeux():
    """Génère une liste de 3 voeux uniques"""
    return random.sample(PROGRAMMES, 3)  # Prend 3 programmes aléatoires sans répétition

def generer_eleve():
    """Génère les données d'un élève"""
    nom = random.choice(NOMS)
    prenom = random.choice(PRENOMS)
    niveau = random.choice(NIVEAUX)
    classe = random.choice(CLASSES)
    classe_complete = f'{niveau}{classe}'
    date = generer_date_aleatoire()
    voeux = generer_voeux()
    
    return [date, nom, prenom, classe_complete, voeux[0], voeux[1], voeux[2]]

def generer_fichier_voeux(nombre_eleves=540, nom_fichier='voeux.csv'):
    """Génère le fichier CSV avec les voeux des élèves"""
    en_tetes = ['Date', 'Nom', 'Prenom', 'Classe', 'Voeux1', 'Voeux2', 'Voeux3']
    eleves = [generer_eleve() for _ in range(nombre_eleves)]
    
    # Tri par date
    eleves.sort(key=lambda x: x[0])
    
    # Écriture dans le fichier CSV
    with open(nom_fichier, 'w', newline='', encoding='utf-8') as fichier:
        writer = csv.writer(fichier, delimiter=';')
        writer.writerow(en_tetes)
        writer.writerows(eleves)

if __name__ == '__main__':
    # Génération du fichier
    generer_fichier_voeux()
    print("Fichier voeux.csv généré avec succès !")