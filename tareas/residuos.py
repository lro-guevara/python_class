'''
##  NAME
       residuos.py
##  VERSION
        [0.0]
##  AUTHOR
	Luz Rosario Guevara Cruz <lguevara@lcg.unam.mx>

##  GITHUB REPOSITORY
	https://github.com/lro-guevara/python_class
##  DATE
    2020/09/27
##  DESCRIPTION
    Este programa toma un archivo pdb para analizar los datos y bucar un residuo aminoacidico en las cadenas
    de proteinas, estos residuos se guardan en una lista y se imprime su posición.

##  CATEGORY
        [sequence amonioacid analysis]
##  USAGE
	Uso bioinformatico en Python
##  ARGUMENTS
    Sin argumentos adicionales

##  INPUT
    Archivo pdb
OUTPUT
    Lista de residuos

EXAMPLES
    INPUT
    1kcw.pdb
    OUTPUT
    Se encontró LYS 61 veces.

[['LYS', 1], ['LYS', 3], ['LYS', 23], ['LYS', 24], ['LYS', 49], ['LYS', 50], ['LYS', 67], ['LYS', 79],
['LYS', 85], ['LYS', 91], ['LYS', 109], ['LYS', 129], ['LYS', 168], ['LYS', 182], ['LYS', 183], ['LYS', 188],
['LYS', 190], ['LYS', 192], ['LYS', 218], ['LYS', 226], ['LYS', 229], ['LYS', 263], ['LYS', 288], ['LYS', 326],
['LYS', 350], ['LYS', 376], ['LYS', 402], ['LYS', 403], ['LYS', 418], ['LYS', 449], ['LYS', 465], ['LYS', 504],
['LYS', 518], ['LYS', 528], ['LYS', 539], ['LYS', 542], ['LYS', 543], ['LYS', 553], ['LYS', 557], ['LYS', 590],
['LYS', 600], ['LYS', 619], ['LYS', 691], ['LYS', 693], ['LYS', 734], ['LYS', 751], ['LYS', 759], ['LYS', 761],
['LYS', 762], ['LYS', 780], ['LYS', 800], ['LYS', 802], ['LYS', 806], ['LYS', 841], ['LYS', 868], ['LYS', 894],
['LYS', 917], ['LYS', 925], ['LYS', 928], ['LYS', 938], ['LYS', 987]]

'''

# Importar librerias
from Bio import PDB


# Definir funcion para encontrar id de aminoacidos
def residues_id(path, cadena, residue):
    # Lista en la que se guardara el id del residuo
    residuos = []
    # Funcion para crear parser
    parser = PDB.PDBParser(QUIET=True)
    struct = parser.get_structure('prot', path)

    # Analizamos los datos dentro de la estructura prot
    for modelo in struct:
        for chain in modelo:
            # Continuamos ciclos si la cadena corresponde
            if chain.id == cadena:
                for residuo in chain:
                    # Si el nombre del residuo corresponde guardamos en una lista
                    if residuo.get_resname() == residue:
                        residuos.append([residue, residuo.id[1]])
    # Si la busqueda fue correcta se imprimen los resultados
    if len(residuos) != 0:
        print("Se encontró " + str(residue) + " " + str(len(residuos)) + " veces. \n")
        print(residuos)
    # Si la busqueda no arrojo resultados se imprime mensaje
    else:
        print("No se encontró el residuo " + str(residue) + " en cadena A.")


# Pedimos residuo que se quiere buscar
residue = input("Residuo a buscar: ")

print("Se buscará el residuo " + str(
    residue) + " en la cadena A del archivo 1kcw.pdb. \n ¿Desea cambiar los datos de búsqueda? y/n")
if input() == "n":
    residues_id('1kcw.pdb', 'A', residue)
else:
    path = input("Ingrese nombre del archivo: ")
    cadena = input("Ingrese cadena: ")
    residues_id(path, cadena, residue)
