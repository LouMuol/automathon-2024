import csv
import random

# Ouvrir le fichier CSV en mode lecture
with open('./automathon-2024/automathon-2024/submission_random.csv', 'r') as csvfile:
    # Créer un lecteur CSV
    reader = csv.reader(csvfile)
    # Créer une liste pour stocker les lignes modifiées
    modified_rows = []
    # Parcourir chaque ligne du fichier CSV
    for row in reader:
        # Modifier les valeurs de la ligne selon vos besoins
        # Par exemple, si vous voulez modifier la première colonne :
        row[1]=1-int(row[1])
        # Ajouter la ligne modifiée à la liste
        modified_rows.append(row)

# Ouvrir le fichier CSV en mode écriture
with open('./automathon-2024/automathon-2024/submission_random.csv', 'w', newline='') as csvfile:
    # Créer un écrivain CSV
    writer = csv.writer(csvfile)
    # Écrire les lignes modifiées dans le fichier CSV
    writer.writerows(modified_rows)
