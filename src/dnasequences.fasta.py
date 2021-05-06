'''
NAME
    dnasequences_fasta.py
VERSION
        [1.0]
AUTHOR
	Luz Rosario Guevara Cruz <lrosarioguevara@gmail.com>

GITHUB REPOSITORY
    https://github.com/lro-guevara/python_class

DESCRIPTION
        [Este programa toma las sequencias genómicas de un archivo ".txt" y formula un formato de tipo fasta]
CATEGORY
        [sequence analysis, genomic sequence for example]
USAGE
	    Uso bioinformático, corre en Python.

ARGUMENTS
        Este programa no requiere de argumetos extra.

INPUT
        [Input: 4_dna_sequences.txt]

OUTPUT
    [Output: dnasequences.fasta]


EXAMPLES
    [Example 1: describe the example, input and outputs]
'''

# Abrir el archivo
archivo = open("C:/Users/Home/Desktop/LCG/Segundo semestre/Python/data/4_dna_sequences.txt")
# Leer cada una de las líneas y guardarlas en una variable
file_contents = archivo.readlines()
# Cerrar el archivo que ya no usamos
archivo.close()

# Crear un nuevo archivo .fasta
my_file = open("dnasequences.fasta", "w")

# Iniciamos un loop
n = 1
for line in file_contents:

    line = line.split('=')

    line = (line[-1])
    line = line.replace("-", '')
    line = line.replace('"', '')
    line = line.upper()
    line = (">seq_" + str(n) + "\n" + line)
    n += 1
    print(line)
    my_file.write(line)
my_file.close()