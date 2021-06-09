'''
##  NAME
    rich_at_regions.py
##  VERSION
        [1.0]
##  AUTHOR
	Luz Rosario Guevara Cruz <lguevara@lcg.unam.mx>

##  GITHUB REPOSITORY
	https://github.com/lro-guevara/python_class
##  DATE
    [2021/06/08]
##  DESCRIPTION
        [A partir de una secuencia de DNA introducida por el usuario, se imprimen
        las regiones ricas en AT o emite error si los caracteres no corresponden a nucleótidos.]
##  CATEGORY
        [sequence analysis, genomic sequence]
##  USAGE
	[programName][-options/arguments]
##  ARGUMENTS
    [No se requiere de argumentos extra]
##  FUNCTIONS
def test_dna(dna):
    nondefined = re.findall(r"[^ATGC]", dna)
    try:
        if re.search(r"[^ATGC]", dna):
            raise ValueError
    except ValueError:
        print(f"La secuencia contiene caracteres no especificados.{nondefined}")
    return()

def at_rich(dna):
        prove = re.findall("[AT]{5,}", dna)
        if prove:
            print(f'Las regiones ricas en AT son: {prove}')
        else:
            print("No existen regiones ricas en AT en su secuencia")
        return()

##  INPUT
    [Secuencia de DNA introducida por el usuario]

EXAMPLES
    [input:
    CTGCATTATATCGTACGAAATTATACGCGCG
    output:
    Las regiones ricas en AT son: ['ATTATAT', 'AAATTATA']
    ]
'''
import re

def test_dna(dna):
    nondefined = re.findall(r"[^ATGC]", dna)
    try:
        if re.search(r"[^ATGC]", dna):
            raise ValueError
    except ValueError:
        print(f"La secuencia contiene caracteres no especificados.{nondefined}")
    return()

def at_rich(dna):
        prove = re.findall("[AT]{5,}", dna)
        if prove:
            print(f'Las regiones ricas en AT son: {prove}')
        else:
            print("No existen regiones ricas en AT en su secuencia")
        return()


seq = input("Inserte su secuencia de DNA: ")
seq = seq.upper()

# Llamar a la funcion
test_dna(seq)
at_rich(seq)