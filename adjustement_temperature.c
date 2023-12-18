#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
 
#define MAX_LINE_LENGTH 100000  // Taille maximale pour une ligne, peut être augmentée si nécessaire 
 
void modify_csv(const char *input_file_name, const char *output_file_name) { 
    FILE *input_file = fopen(input_file_name, "r"); 
    FILE *output_file = fopen(output_file_name, "w"); 
 
    if (!input_file || !output_file) { 
        perror("Erreur lors de l'ouverture des fichiers"); 
        exit(EXIT_FAILURE); 
    } 
 
    char line[MAX_LINE_LENGTH]; 
    int is_first_line = 1; 
 
    while (fgets(line, MAX_LINE_LENGTH, input_file)) { 
        char *token = strtok(line, ","); 
        int column_count = 0; 
 
        while (token) { 
            column_count++; 
            if (!is_first_line && column_count > 2) { 
                double num = atof(token); 
                fprintf(output_file, "%f", num + 2.0000); // Augmenter la valeur de 2 
            } else { 
                fprintf(output_file, "%s", token); 
            } 
 
            token = strtok(NULL, ","); 
            if (token) { 
                fprintf(output_file, ","); // Ajouter une virgule entre les valeurs 
            } 
        } 
 
        fprintf(output_file, "\n"); // Nouvelle ligne à la fin de chaque ligne 
        is_first_line = 0; // Après la première ligne, mettre à false 
    } 
 
    fclose(input_file); 
    fclose(output_file); 
} 
 
int main() { 
    const char *input_file_name = "REAL_fichier.csv";  // Remplacer par le nom de votre fichier d'entrée 
    const char *output_file_name = "REAL_valeurs2.csv"; // Remplacer par le nom de votre fichier de sortie 
 
    modify_csv(input_file_name, output_file_name); 
 
    return 0; 
}
