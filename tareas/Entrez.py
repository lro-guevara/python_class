'''
##  NAME
       Entrez.py
##  VERSION
        [1.0]
##  AUTHOR
	Luz Rosario Guevara Cruz <lguevara@lcg.unam.mx>

##  GITHUB REPOSITORY
	https://github.com/lro-guevara/python_class
##  DATE
    [2021/10/04]
##  DESCRIPTION
        This program uses two different functions, the first one analysis and research
        information about a protein and the second look for the author´s data.
##  CATEGORY
        [data base research]
##  USAGE
	[Informatic usage in Python 3.9]
##  ARGUMENTS
    [No arguments required]

##  INPUT
    [data base, author´s name and key terms]
OUTPUT
    [Protein data
    ID.txt]
EXAMPLES
    [Example 1:
    input:
    Amaranta Manrique (como autora) Y alacranes O ética
    outputs:
    ID.txt]
'''
#Importamos Entrez
from Bio import Entrez

#Correo
Entrez.email = "lguevara@lcg.unam.mx"

#Definimos la primera función
def characters():
    #Buscamos informacion en la base de datos
    handle = Entrez.einfo(db='protein')
    #La guardamos en una variable
    record = Entrez.read(handle)
    #Cerramos la busqueda
    handle.close()

    #Ciclo for para conocer la descripcion de ECNO
    for field in record['DbInfo']['FieldList']:
        #Si el nombre coincide se guarda la informacion en una variable
        if field['Name'] == 'ECNO':
            ECNO = (field['Name'], field['Description'])
            #Se imprime la informacion
            print(ECNO)
    #Ciclo for para conocer la descripcion de la proteina
    for field in record['DbInfo']['LinkList']:
        #Si se encuentra la proteina se guarda la descripcion en una variable
        if field['Name'] == 'protein_protein_small_genome':
            small_protein = (field['Name'], field['Description'])
            #Se imprime la descripcion
            print(small_protein)

#Llamamos a la funcion
characters()

#Funcion para buscar autores y palabras claves
def Identificacion(autoria,key_terms):
    #Guardamos datos del autor y palabras clave de la lista
    datos = f'({autoria}[AUTH] AND ({key_terms[0]}[Title] OR {key_terms[1]}[Title]))'
    #Buscamos los datos en la base de datos
    handle = Entrez.esearch(db="pubmed", term=datos)
    #Leemos y guardamos
    result = Entrez.read(handle)
    #Cerramos la busqueda
    handle.close()
    #Creamos nuevo archivo
    output = open("ID.txt")
    #Escribimos los resultados obtenidos
    output.write("\n" + (result["IdList"]))
    #Cerramos archivo
    output.close()
    #Mensae para el usuario
    print("Datos almacenados en el documento ID.txt")

#Pedir datos de busqueda al usuario
key_terms = []
autoria = input("Ingrese nombre del autor(a): ")
key_terms.append = input("Ingrese dos palabras claves a buscar separadas por un enter: ")
key_terms.append = input()
Identificacion(autoria, key_terms)