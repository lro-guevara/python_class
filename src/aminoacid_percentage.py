'''
NAME
        aminoacid_percentage.py

VERSION
        1.0

AUTHOR
    	Luz Rosario Guevara Cruz <lrosarioguevara@gmail.com>

GITHUB REPOSITORY
        https://github.com/lro-guevara/python_class

DESCRIPTION
        This program takes an input from a protein sequence and a list of hydrophilic amino acids, looking for the
        amino acids in the protein sequence to obtain the percentage of these amino acids in the protein sequence.
CATEGORY
        Sequence analysis, protein sequence.

USAGE
	    Bioinformatic usage, run in python console.

ARGUMENTS
        [No additional arguments are required]

INPUT
        The input is given by user.

OUTPUT
        The percentage of hydrophilic amino acids will be printed on the screen.

EXAMPLES
        Input: "MSRSLLLRFLLFLLLLPPLP"
        Output:  "aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65"

'''

#Definimos la función que usará como input proteína y lista de amino ácidos hidrofílicos
def aa_percentage(protein, aa_list):
#Creamos una variable y la inicializamos a 0
    percentage = 0
#En un ciclo for contamos la frecuencia de aninoácidos hidrofílicos en la secuencia para obtener el porcentaje
# en comparación a la longitud total.
    for aa in aa_list:
        percentage += protein.count(aa) * 100 / len(protein)
    return percentage

#Declaramos lista de amino ácidos hidrofílicos
aa_list=['A','I','L','M','F','W','Y','V']

#Corroboramos la función
assert aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert aa_percentage("MSRSLLLRFLLFLLLLPPLP", aa_list ) == 65


#Imprimimos a pantalla
print("Este programa calcula el porcentajede amino ácidos hidrofílicos en su proteina. \nInserte la proteína a analizar: ")
#Guardamos en una variable la secuencia
protein_sequence = input()
#La convertimos a mayúsculas
protein = protein_sequence.upper()
#Imrpimimos el porcentaje
print("El porcentaje de amino ácidos hidrofílicos es: " + str (aa_percentage(protein, aa_list)) + "%")