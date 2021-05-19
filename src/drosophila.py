'''
NAME
        drosophila.py
VERSION
        1.0
AUTHOR
    	Luz Rosario Guevara Cruz <lrosarioguevara@gmail.com>
GITHUB REPOSITORY
        https://github.com/lro-guevara/python_class
DESCRIPTION
        This program takes an input from a Drosophila genes document and prints the name of the gene according
         to its characteristics.
CATEGORY
        Sequence analysis, protein sequence, genomic sequence for example
USAGE
	    Bioinformatic usage, run in python console.
ARGUMENTS
        [No additional arguments are required]
INPUT
        The input is given by user.
OUTPUT
        The name of the gene according to length, species of origin, at content.

EXAMPLES
    Input: 6-data
    Output:
    Genes que pertenecen a Drosophila melanogaster o Drosophila simulans
kdy647
jdg766
kdy533
Genes con longitud 90 a 110 nucleótidos:
kdy647
kdy533
teg436
Genes con AT inferior a .5 y con un nivel de expresión mayor a 200:
teg436
Genes que comienzan con k o h y no pertenecen a Drosophila melanogaster:
kdy647
kdy533
hdt739
hdu045
Gen kdy647 tiene un contenido de AT alto.
Gen jdg766 tiene un contenido de AT bajo.
Gen kdy533 tiene un contenido de AT bajo.
Gen hdt739 tiene un contenido de AT bajo.
Gen hdu045 tiene un contenido de AT bajo.
Gen teg436 tiene un contenido de AT bajo.

'''

#Definimos la función que calculará el contenido AT
def at_function(sequence):
    #Contamos contenido A y T
    a_percentage = (sequence.upper()).count("A")
    t_percentage = (sequence.upper()).count("T")
    #Obtenemos la proporción de at
    at_content = (a_percentage + t_percentage) / len(sequence)
    return at_content

#Abrimos archivo de input
file = open("../docs/6-data.csv", "r")
#Leemos todas las líneas
all_lines = file.readlines()
#Cerramos el archivo
file.close()

#Definimos la función para imprimir genes de D. melanogaster o simulans
def specie(asunder):
    print("Genes que pertenecen a Drosophila melanogaster o Drosophila simulans:")
    for line in all_lines:
        #Separamos las líneas por ,
        asunder = line.split(",")
        if asunder[0] == "Drosophila melanogaster" or asunder[0] == "Drosophila simulans":
            print(asunder[2])

#Imprimimos genes con longitud de 90 a 110
def length(asunder):
    print("")
    print("Genes con longitud 90 a 110 nucleótidos: ")
    for line in all_lines:
        asunder = line.split(",")
        if len(asunder[1]) >= 90 and len(asunder[1]) <= 110:
            print(asunder[2])

#Definimos función que imprimirá los genes con una densidad <.5 de AT
def at_density(asunder):
    print("")
    print("Genes con AT inferior a .5 y con un nivel de expresión mayor a 200: " )
    for line in all_lines:
        asunder = line.split(",")
        if at_function(asunder[1]) < 0.5 and int(asunder[3]) > 200:
            print(asunder[2])

#Definimos función que permite imprimir genes que inician con k o h y no pertenecen a D. melanogaster
def letter(asunder):
    print("")
    print("Genes que comienzan con k o h y no pertenecen a Drosophila melanogaster:")
    for line in all_lines:
        asunder = line.split(",")
        if asunder[1] != "Drosophila melanogaster" and asunder[2].startswith("k") or asunder[2].startswith("h"):
            print(asunder[2])

#Imprimimos el nombre de todos los genes y el contenido de AT que portan, como alto, medio o bajo
def data(asunder):
    print("")
    for line in all_lines:
        asunder = line.split(",")
        if at_function(asunder[1]) > .65:
            print("Gen " + asunder[2] + " tiene un contenido de AT alto.")
        elif at_function(asunder[2]) < .45:
            print("Gen " + asunder[2] + " tiene un contenido de AT bajo.")
        else:
            print("Gen " + asunder[2] + " tiene un contenido de AT medio.")

#Ejecutamos las funciones

specie(all_lines)
length(all_lines)
at_density(all_lines)
letter(all_lines)
data(all_lines)






