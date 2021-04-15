'''
NAME
       transcript_sequence.py
VERSION
        [1.0]
AUTHOR
	Luz Rosario Guevara Cruz <lrosarioguevara@gmail.com>

DESCRIPTION
        Este programa obtiene la secuencia que será transcrita a partir de una secuencia de DNA. Indica la posición del codón de inicio y del codón de término.
CATEGORY
        Sequence analysis, Genomic sequence.
USAGE


ARGUMENTS
     No se requiere de argumentos en adición.

INPUT
    DNA Sequence: ""AAGGTACGTCGCGCGTTATTAGCCTAAT"


OUTPUT
    El codon de inicio  se encuentra en la pos 4
    El codon de término se encuentra en la pos 17
    Secuencia que se transcribe:


EXAMPLES
    [Example 1:
    Input: dna = 'AAGGATGTCGCGCGTTATTAGCCTAA'

    Output:
    ## El codon TAC empieza en la posicion  4  y termina en  26
    ## Fragmento de RNA que será transcrito (en DNA):
    ## TACGTCGCGCGTTATTAGCC
'''

DNA = "AAGGTACGTCGCGCGTTATTAGCCTAAT"
print ("Secuencia input de DNA:", str (DNA))
start = DNA.find("TAC")
stop = DNA.find("ATT")
print ("El codon de inicio  se encuentra en la pos ", str (start +1))
print ("El codon de término se encuentra en la pos ", str (stop+1))
tsequence = DNA[start:stop]
print ("Fragmento de DNA que será transcrito: " + str (tsequence))


