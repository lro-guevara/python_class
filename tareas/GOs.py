'''
##  NAME
       GOs.py
##  VERSION
        [1.0]
##  AUTHOR
	Luz Rosario Guevara Cruz <lguevara@lcg.unam.mx>

##  GITHUB REPOSITORY
	https://github.com/lro-guevara/python_class
##  DATE
    [2020/10/25]
## DESCRIPTION
    Este programa tiene dos listas con distintos GOs  e IDs proteicos para realizar una busqueda y
    escribir los resultados en un archivo output .txt

##  CATEGORY
        [Data Base analysis]
##  USAGE
	[Bioinformatic, usage in Python 3.9]
##  ARGUMENTS
    [No arguments required]

##  INPUT
    -
OUTPUT
    GOs.txt

'''

#Importamos librerias
from Bio import Entrez
from Bio import ExPASy
from Bio import SwissProt

#Correo
from Bio.ExPASy import Prosite

Entrez.email = "lguevara@lcg.unam.mx"


#Funcion para buscar informacion
def search_by_GO(GO_Terms, uniprot_IDs):
    #Abrimos archivo output
    file = open("GOs.txt", "w")
    #Se buscan los archivos input
    for ID in uniprot_IDs:
        handle = ExPASy.get_sprot_raw(ID)
        record = SwissProt.read(handle)

        #Se hace la busqueda de cada elemento de la lista
        for GO in GO_Terms:
            for term in record.cross_references:
                #Comparamos archivos
                if term in GO == GO_Terms:
                    #Escribimos el ID
                    file.write(f'ID: ' + ID + '\n')
                    #Separamos la informacion
                    nombre = record.description.split("=")[1]
                    #Obtenemos el nombre correspondiente
                    #Escribimos la definicion y el organismo
                    file.write(f'Nombre: {nombre.split(";")[0]}\n\n'
                           f'GO: {GO}\n'
                           f'Definicion: {GO[2]}\n'
                           f'Organismo: {record.organism}\n')
                #Obtenemos la longitud de los comentarios
                length = len(record.comments)
                #Para cada comentario se aplica una funcion
                for i in range(0, length):
                    #Se separa la informacion por {
                    location = record.comments.split("{"[0])
                    #Se escribe la licalizacion
                    file.write(f'Localizacion:{location}\n')
                    #Generamos una lista para las referencias
                    references = []
                    #Obtenemos unicamente 2 elementos
                    rcrd = record.references[1:2]
                    #Para cada referencia se apica una funcion
                    for ref in record:
                        #Se guarda en la lista los dos elementos
                        references.append(ref.references[0][1])
                        #Se transforma s string
                        string = str(rcrd())
                        #Se busca la informacion
                        handle = Entrez.efetch(db='pubmed', id=string, rettype="abstract", retmode="text")
                        data = handle.read()
                        handle.close()
                        #Se escribe en el documento
                        file.write(f'Abstract: {data}\n')
                    #Buscamos las referencias
                    all_refs = record.cross_references
                    #Se busca la documentacion con ExPASy
                    for prosite in all_refs:
                        handle = ExPASy.get_prosite_raw(prosite)
                        record = Prosite.read(handle)
                        handle.close()
                        #Se escribe en el documento
                        file.write(f'Documentacion: {record}\n')
                    #Cerrar documento output
                    file.close()

#LISTAS
GO_Terms = ["GO:0046755", "GO:0046761","GO:0046760", "GO:0039702", "GO:0046765", "GO:0046762"]
uniprot_IDs = ["A0A0K2RVI7_9BETC", "A8R4D4_9BETC", "POLG_YEFV1", "POLG_DEN1W", "Q6W352_CVEN9", "D9SV67_CLOC7", "A9KSF7_LACP7", "B8I7R6_RUMCH"]
#Llamar a la funcion
search_by_GO(GO_Terms, uniprot_IDs)
