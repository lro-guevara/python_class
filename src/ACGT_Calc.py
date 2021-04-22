'''
NAME
    ACGT_Calc.py
VERSION
    [1.0]
AUTHOR
	Luz Rosario Guevara Cruz <lrosarioguevara@gmail.com>

GITHUB REPOSITORY
    https://github.com/lro-guevara/python_class

DESCRIPTION
    [Programa que permite conocer la cantidad de cada uno de los nucleótidos A,T,C,G en una secuencia de DNA dada por el usuario]
CATEGORY
    [Nucleotide percentage]
USAGE
	[No se requieren opciones extras en nuestro programa]

ARGUMENTS
    [No se requiere de argumentos adicionales en nuestro programa]


INPUT
    [La secuencia input es dada por el usuario]


OUTPUT
    [Cantidad de repeticiones de un nucleótido en nuestra secuencia]


EXAMPLES
    [Input:
    DNA_sequence: 'AAGGAUGTCGCGCGTTATTAGCCTAA'
    Output:
    A: 7 , C: 5 , G: 7 , T: 6]
'''
#Imprimimos a pantalla una breve descripción del programa para que el usuario conozca las funciones de este. Solicitamos secuencia input.
print("Programa que a partir de una secuencia de DNA permite conocer la proporción de cada nucleótido en ella. \nIngrese la secuencia de interés")
#Almacenamos el input en una variable
DNA_Sequence = input ()
#En caso de que el usuario coloque el input en letras minúsculas, se convierten en letras mayúsculas para poder reconocerlas.
DNA = DNA_Sequence.upper()
#En variables almacenamos la cantidad de veces que se presenta cada nucleótido en nuestra secuencia.
A = DNA.count("A")
C = DNA.count("C")
G = DNA.count("G")
T = DNA.count("T")
#Imprimimos los resultados que indican la presencia total de los nucleótidos
print("A:", A,", C:", C, ", G:", G,", T:", T)