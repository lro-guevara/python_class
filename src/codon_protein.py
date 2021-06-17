"""
##  NAME
       [codon_protein.py]
##  VERSION
        [1.0]
##  AUTHOR
    Luz Rosario Guevara Cruz <lguevara@lcg.unam.mx>

##  GITHUB REPOSITORY
    https://github.com/lro-guevara/python_class
##  DATE
    [2021/06/16]
##  DESCRIPTION
        [This program ask to user for a RNA sequence and as output prints the amino acid sequence of the protein]
##  CATEGORY
        [RNA sequence analysis, protein sequence for example]
##  USAGE
    [Bioinformatic usage, codified in python]
##  ARGUMENTS
    [No arguments required for usage]

##  FUNCTIONS
def function(arguments):
    [code1]
    [code2]
    return
##  INPUT
    [RNA sequence]
OUTPUT
    [Aminoacid sequence]
EXAMPLES
    [Input:
     AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
    Output:
    MAMAPRTEINSTRING]
"""
#Importamos la libreria necesario para nuestra funcion
import re
#Declaramos nuestro diccionario con el aminoacido correspondiente a cada codon
gencode = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
    'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
    'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
    'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
    'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
    'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
    'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
    'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
    'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
    'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

#Creamos una funcion para saber si hay caracteres no correspondientes en la secuencia
def test_rna(rna):
    no_rna = re.findall(r"[^ATGCU]", rna)
    try:
        if re.search(r"[^ATGCU]", rna):
            raise ValueError
    except ValueError:
        print(f"La secuencia genética contiene caracteres no identificados como nucleótidos: {no_rna}")
        print("Desea intentar de nuevo?(y/n)")
        result=input()
        if result == "y":
            newrna=input("Introduzca su nueva secuencia de RNA:")
            newrna = newrna.upper()
            test_rna(newrna)
        else:
            exit()
    else:
        return(rna)
#Creamos una funcion para saber si el RNA contiene un codon de inicio de la transcripcion
def orf(rna):
    inicio = re.search(r"ATG[ATGC]", rna)
    if inicio:
        return(rna)
    else:
        print(f"La secuencia no contiene codon de inicio")
#Presentamos el programa
print("Este programa te permitirá conocer la secuencia de amino ácidos que genera la secuencia de RNA")
#Declaramos nuestras variables
rna=input("Introduzca su secuencia de RNA:\n")
rna = rna.upper()
rna = rna.replace("U", "T")
#Enviamos nuestra variable como parámetro
test_rna(rna)
newrna = rna.replace("U", "T")
atg = orf(rna)
#Creamos una lista
proteina = []
if atg:
    #Generamos un ciclo que divida las secuencias por codones
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        #Si encontramos al codon de paro se sale del ciclo
        if gencode[codon] == "_":
            break
        #Agregamos a la lista cada nucleotido
        else:
            proteina.append(gencode[codon])
    #Convertimos la lista de nucleotidos en una cadena
    proteina = "".join(proteina)
    #Se imprime el resultado
    print("Su proteína es:\n"+str(proteina))