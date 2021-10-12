'''
##  NAME
       Get_abstract.py
##  VERSION
        [1.0]
##  AUTHOR
	Luz Rosario Guevara Cruz <lguevara@lcg.unam.mx>

##  GITHUB REPOSITORY
	https://github.com/lro-guevara/python_class
##  DATE
    [2002/10/11]
##  DESCRIPTION
    This program shows us the different matches between a database and the words used as input.
    With this information gets the Article ID and save their abstract and the ID of the articles
    that cited the first in new documents .txt

##  CATEGORY
        [Data Base analysis]
##  USAGE
	[Bioinformatic, usage in Python 3.9]
##  ARGUMENTS
    [No arguments required]

##  INPUT
    Author´s name, key words.
OUTPUT
    "IDS.txt"
    "Abstracts.txt"
    "Citas.txt"

'''

#Importamos Entrez
from Bio import Entrez

#Correo
Entrez.email = "lguevara@lcg.unam.mx"

#Funcion para buscar autores y palabras claves
def Identificacion(autoria,key_terms,cant):
    #Guardamos datos del autor y palabras clave de la lista
    for i in cant:
        datos = f'({autoria}[AUTH] AND ({key_terms[i]}[Title]))'

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
    return("ID.txt")

#Pedir datos de busqueda al usuario
key_terms = []
autoria = input("Ingrese nombre del autor(a): ")
cant = int(input("Cantidad de palabras que desea buscar: "))

for i in cant:
    key_terms.append = input("Ingrese palabra clave: ")

Identificacion(autoria, key_terms, cant)

#Función que busca abstracts
def abstract(ID):
    #Transformamos el formato de nuestro documento con los IDS
    IDS = str(ID[1])
    #Abrimos archivo donde se escribirán los abstracts
    out_handle = open("Abstracts.txt")
    #Accedemos a la base de dato y filtramos la información
    handle = Entrez.efetch(db="pubmed", id=IDS, rettype="abstract", retmode="text")
    data = handle.read
    #Cerramos busqueda
    handle.close()
    #Escribimos en el nuevo documento
    out_handle.write(data)

    # Para cada coincidencia de la busqueda obtenemos IDS que citan a ese artículo
    citas = Entrez.read(Entrez.elink(dbfrom="data_base", db='pubmed', LinkName='pubmed_pubmed_citedin'))
    for i in len(IDS):
        #Escribimos unicamente 3 citas
        for j in range(1, 3):
            #Abrimos nuevo documento
            citado = open("Citas.txt")
            #Escribimos sus resultados
            citado.write(f'El artículo {IDS[i]} es citado en:  {[link["Id"]for link in citas[i]["LinkSetDb"][0]["Link"]]}')
            #Cerramos documento
            citado.close()

#Llamamos a la función
abstract("ID.txt")