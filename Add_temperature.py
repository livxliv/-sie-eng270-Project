import pandas as pd
import random

# Charger le fichier CSV initial
input_file_path = 'coral_coordinates_realwithdates.csv'
output_file_path = 'Position_date_temp.csv'

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv(input_file_path)

# Fonction pour générer un nombre aléatoire entre 23,000 et 30,000
def generate_random_number():
    return random.uniform(16.000, 30.000)

# Parcourir les colonnes (à partir de la troisième colonne)
for col in df.columns[2:]:
    # Ajouter des nombres aléatoires à chaque cellule de la colonne
    df[col] = df.apply(lambda row: generate_random_number(), axis=1)

# Enregistrer le DataFrame modifié dans un nouveau fichier CSV
df.to_csv(output_file_path, index=False)

print(f"Nouveau fichier CSV créé avec succès. Chemin : {output_file_path}")
