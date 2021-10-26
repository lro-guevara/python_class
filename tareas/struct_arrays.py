'''
##  NAME
       struct_arrays.py
##  VERSION
        [1.0]
##  AUTHOR
	Luz Rosario Guevara Cruz <lguevara@lcg.unam.mx>

##  GITHUB REPOSITORY
	https://github.com/lro-guevara/python_class
##  DATE
    [2020/10/25]
## DESCRIPTION
    Generamos arrays structurados para imprimir información correspondiente de cada dato segun el tamaño
    de este y se realican operaciones.
##  CATEGORY
        [Data Base analysis]
##  USAGE
	[Bioinformatic, usage in Python 3.9]
##  ARGUMENTS
    [No arguments required]

##  INPUT
    -
OUTPUT
Produccion
[('Gen 1',  5, 3) ('Gen 2', 11, 7) ('Gen 3',  4, 9) ('Gen 4',  2, 6)]
Costos
[('Gen 1', 3.5) ('Gen 2', 5. ) ('Gen 3', 7. ) ('Gen 4', 4.3)]
Costo unitario
 [[0.7        1.16666667]
 [0.45454545 0.71428571]
 [1.75       0.77777778]
 [2.15       0.71666667]]
Costo g/L
[('Gen 1', 0, 1.16666667) ('Gen 2', 0, 0.71428571)
 ('Gen 3', 1, 0.77777778) ('Gen 4', 2, 0.71666667)]


'''

#Importamos librerias
import numpy as np

#Arrays con datos input
produccion=np.array([[5, 3], [11, 7], [4, 9], [2, 6]])
costo = np.array([3.5, 5, 7, 4.3])

#Arrays estructurados por categorias
#Array estructurado por la produccion de los genes y temperatura
pstruct = np.array([('Gen 1', 5, 3), ('Gen 2', 11, 7), ('Gen 3', 4, 9), ('Gen 4', 2, 6)],
    dtype=[('gen', (np.str_, 5)), ('K°1', np.int32), ('K°2', np.int32)])

#Array estructurado por los costos
cstruct = np.array([('Gen 1', 3.5), ('Gen 2', 5), ('Gen 3', 7), ('Gen 4', 4.3)],
    dtype=[('gen', np.str_, 5), ('costo', np.float64)])

#Array segun el precio g/L
prestruct = np.array([('Gen 1', 0.7, 1.16666667), ('Gen 2', 0.45454545, 0.71428571), ('Gen 3', 1.75, 0.77777778), ('Gen 4', 2.15, 0.71666667)],
       dtype=[('gen', (np.str_, 5)), ('K°', np.int32), ('costo g/L', np.float64)])

#Se obtiene el precio
precio = (costo / produccion.T).T


#Imprimimos arrays
print("Produccion\n"+str(pstruct))

print("Costos\n"+str(cstruct))

print("Costo unitario \n " + str(precio))

print("Costo g/L \n" + str(prestruct))