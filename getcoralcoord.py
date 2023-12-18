import csv
import json


with open("Marine_Park.json") as file:

    australia_data=json.load(file)

coral_coord=[]
new_x=[]
new_y=[]

def extract_coor():

    features = australia_data["features"]
    for feature in features:

        properties=feature["properties"]

        x_coord = properties["X_COORD"]
        y_coord=properties["Y_COORD"]
        location= properties["LOC_NAME_L"]

        if "Reef" in location:
            coral_coord.append([x_coord,y_coord])

            for row in coral_coord:

                new_x=row[0]
                new_y=row[1]

    return new_x, new_y

Position_coral=extract_coor()


def creation_csv():
    position_coral_csv="coral_coordinates.csv"

    # Écrire les données dans le fichier CSV
    with open("coral_coordinates.csv", mode='w', newline='') as csv_file:
        
        fieldnames = ['X_COORD', 'Y_COORD']  # Noms des colonnes dans le CSV
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Écrire l'en-tête (noms de colonnes) dans le fichier CSV
        writer.writeheader()

        # Écrire les données dans le fichier CSV
        for x, y in coral_coord:
            writer.writerow({'X_COORD': x, 'Y_COORD': y})

    
    print(f"Fichier CSV créé avec succès : {position_coral_csv}")
new_csv=creation_csv()
