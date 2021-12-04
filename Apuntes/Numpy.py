"""
DATE: 19/10/2021, 26/10/2021
TOPIC: NUMPY

"""

import numpy as np

# Unidades de absorbancia
ecoli_matraz = np.array([0.1, 0.15, 0.19, 0.5,
                         0.9, 1.4, 1.8, 2.1, 2.3])
ecoli_matraz.ndim
ecoli_matraz.shape

## [] -> contenedor, () -> duplas

# Array
array_1D = np.array((1, 2, 3))
array_1D.ndim  # 1 dimension
array_1D.shape  # 3 filas
len(array_1D)  # 3

# 2D
array_2D = np.array([(1, 3, 4), (2, 5, 6)])
array_2D.ndim  # 2 dimensiones
array_2D.shape  # (2,3)

# 3D
array_3D = np.array([([1, 2], [3, 4]),
                     ([5, 6], [6, 7])])

"""
OPERACIONES

array1 + array2 = array de la misma dimension que el 1 y 2

np.sum(array * 2, axis = 0)  # especificar eje

array/2  # Todo el objeto se divide

NOTA: En Numpy también se realiza el reciclaje de arrays como en R

También existen potencias para arrays:
array**2
array**array

Sacar la transpuesta:
array.T  # De fila a columna

Maimos y minimos:
array.min()  # = np,min(array)
array.max()  # = np.max(array)

Trigonometricas

Operadores como: +=, *= 

Redondear:
np.ceil(array)  # Redondeo hacia arriba
np.floor(array)  # Redondeo hacia abajo
np.round(array)  # Redondeo al mas cercano
"""

## EJERCICIO 1
produccion = np.array([[5, 3], [11, 7], [4, 9], [2, 6]])
costos = np.array([3.5, 5, 7, 4.3])

# Transponer
costo_unitario = (costos / produccion.T).T

"""
TIPOS DE DATO

array.dtype 

float -> 0.1, 0.2, 0.3
int32 -> 1, 2, 3
booleano -> True, False, True

Acceso booleano:
array_int[array_booleano]  # Acceder a valores de un array como en R
(array_int <2 ) | (array_int >3)  # Array contra array, da los que sean mayor a 2 y menor a 3

Datos complejos

Datos de fechas:
array = np.daytime64('2005-02-25')
"""

menor_costo = costo_unitario.min()
mayor_costo = costo_unitario.max()

# Booleanos
menor - cost_bool = costo_unitario == menor_costo
mayor_cost_bool = costo_unitario == mayor_costor

costo_unitario[(mayor_cost_bool | menor_cost_bool)]

"""
ACCEDER A ARRAYS

1 dimensión:
array[2]  # Posicion 3 empezando en 0
array[2:5]  # De la posicion 3 a la 6
array[:6:2]  # Del 0 al 6 en dos en dos
array[::2]  # Del inicio al final de dos en dos
array[1::2]  # Del 1 al resto de dos en dos
array[::-1]  # Imprime el array en reversa 

2D:
array[2]  # Tercer elemento empezando en 0
array[2][1]  # Acceder como matriz

Utilizar "..." o ";,;,"  para evitar escribir todas las dimensiones


CREAR ARRAYS

np.arange(10)  # Sí maneja decimales
np.arange(0, 10, 2)  # Comienza en 0 sin llegar a 10 en pasos de dos en dos
np.linspace(0, 8, 5)  # Comienza en 0 llega al 8 en 5 segmentos

Hay problemas con los decimales y su redondeo:
np.arange(0.5, 0.8, 0.1)  # Sí llega a 0.8 por problemas de redondeo

np.random.randint(0, 10, 3)  # Comienza en 0, tres numeros, sin tener 10
np.zeros((2,3))  # Matrices de ceros

También se puede repetir, unir, dividir; borrar, unir u ordenar filas o columnas


ARRAYS VS LISTAS
listas -> heterogeneas
ej_lista = [[0,0,0]]*2  # Repite la lista 2 veces, la copia

arrays -> homogeneos

"""
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Matriz
# genfromtxt o loadtxt lee la matriz de un documento
count_matrix = np.array([[3, 3, 0],
                         [0, 0, 1],
                         [1, 1, 0],
                         [0, 0, 1],
                         [1, 0, 4],
                         [1, 2, 0]])

## Obtener matriz de coexpresion
count_matrix = np.where(count_matrix > 0, 1, 0)
print(count_matrix)

# Observar la expresion nivel gen
print(count_matrix.T[0])

# Interseccion de vectores
print((count_matrix.T[0]) & (count_matrix.T[0])))

# Producto punto
print(np.dot(count_matrix.T[0], count_matrix.T[0]))

expresion = np.matmul(count_matrix.T, count_matrix)

# Plotear
plt.inshow(expresion)
plt.colorbar()
plt.show()

G = nx.DiGraph(expresion)
nx.draw(G, node_size=900, with_labels=True)
plt.show()

"""
SEEDS aleatorias

import numpy as np

np.random.seed(10)  # seed = 10

"""

## Secuencias aleatorias

rom
Bio.Seq
import Seq
import numpy as np


def secuencia_aleatoria(tamano=100, p=[0.5, 0.5, 0.5, 0.5], seed=None):
    np.random.seed(seed)  # posibilidad de reproducibilidad
    DNA = list("ATGC")
    # secuencia random con distribucion p
    secuencia = Seq(''.join(np.random.choice(DNA, tamano, p)))
    return (secuencia)


secuencia = secuencia_aleatoria(25, p=[0.1, 0.2, 0.4, 0.3])
secuencia


def seq_aleatorias(tamano=100, p=[0.5, 0.5, 0.5, 0.5], seed=None,
                   num_seq=10, archivo="files/SeqAleatorias.fasta"):
    with open(archivo, 'w') as file:
        for i in range(num_seq):
            sec = secuencia_aleatoria(tamano, p, seed)
            file.write(">Seq" + str(i) + "\n")
            file.write(str(sec))
            file.write("\n")
    file.close()


#####################################################

from Bio import SeqIO
import csv
import re


# Busqueda de patrones en FASTA
def busqueda_patron(fasta="files/SeqAleatorias.fasta", output="files/ejercicioNP.csv"):
    tf_interes_mod = {"TF_1": 'ATG[GG|TAG]', "TF_2": 'T[TC|AA]GAAT',
                      "TF_3": "GTATGCGGGG", "TF_4": "TAT[GT]CC",
                      "TF_5": "TATATA[GT|TG]"}
    outfile = open(output, "w")
    writer = csv.writer(outfile)
    for rec in SeqIO.parse(fasta, "fasta"):
        # secuencia por analizar
        seq = rec.seq
        # array para guardar numero de coindicencias
        tf_counts = np.empty((0), dtype="int")
        for tf in tf_interes_mod.values():
            counts = len(re.findall(tf, str(seq)))
            tf_counts = np.append(tf_counts, [counts])
        # escribir counts encontrados (iterable)
        writer.writerows([tf_counts])
    outfile.close()
