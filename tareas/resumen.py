'''
##  NAME
       resumen.py
##  VERSION
        [0.0]
##  AUTHOR
	Luz Rosario Guevara Cruz <lguevara@lcg.unam.mx>

##  GITHUB REPOSITORY
	https://github.com/lro-guevara/python_class
##  DATE
    [2021/09/20]
##  DESCRIPTION
        [Se analiza un archivo .gb para otorgar los datos de las secuencias y donde fueron obtenidas mediante una funcion]
##  CATEGORY
        [sequence analysis, genebank]
##  USAGE
	[Bioinformático, Python]
##  ARGUMENTS
    [Sin argumentos adicionales]

##Required library
    from Bio.Seq import Seq
    from Bio import SeqIO
##  FUNCTIONS
def resumen(path, genes):
       for gb_record in SeqIO.parse(path, "genbank"):

        print("Organismo:", gb_record.annotations["organism"])
        print("Fecha:", gb_record.annotations["date"])
        print("Version de la secuencia:", gb_record.annotations["sequence_version"])
        print("Aislado:", gb_record.features[0].qualifiers["isolation_source"])
        print("Pais:", gb_record.features[0].qualifiers["country"])

        for j, gene in enumerate(genes):
            print("Gen_"+str(j+1)+": "+ str(gene))
            for i in range(1, len(gb_record.features), 2):
                if gb_record.features[i].qualifiers['gene'] == [gene]:
                    inicio = gb_record.features[i].location.nofuzzy_start
                    fin = inicio + 15
                    print("DNA:", gb_record.seq[inicio:fin])
                    print("RNA:", gb_record.seq[inicio:fin].transcribe())
                    print("Proteína:", gb_record.seq[inicio:fin].translate())
    return
##  INPUT
    [virus.gb]
OUTPUT
    [Gen_x: Y
    País:
    Fecha:
    Lugar de extracción:
    Versión:
    DNA:
    RNA:
    Proteina:]
EXAMPLES
    Input:
        virus.gb
    Output:
        Organismo: Isfahan virus
        Fecha: 13-AUG-2018
        Version de la secuencia: 1
        Aislado: ['Phlebotomus papatasi']
        Pais: ['Iran:Isfahan province']
        Gen_1: L
        DNA: ATGGATGAGTACTCT
        RNA: AUGGAUGAGUACUCU
        Proteína: MDEYS
'''
#Importar las librerias necesarias
from Bio.Seq import Seq
from Bio import SeqIO

#Definir la funcion con input path y genes
def resumen(path, genes):

    #Usar archivo gb
    for gb_record in SeqIO.parse(path, "genbank"):

        #Imprimir las caracteristicas del organismo segun se encuentren
        print("Organismo:", gb_record.annotations["organism"])
        print("Fecha:", gb_record.annotations["date"])
        print("Version de la secuencia:", gb_record.annotations["sequence_version"])
        print("Aislado:", gb_record.features[0].qualifiers["isolation_source"])
        print("Pais:", gb_record.features[0].qualifiers["country"])

        #Enumerar los genes encontrados
        for j, gene in enumerate(genes):
            #Imprimir su nombre y numero
            print("Gen_"+str(j+1)+": "+ str(gene))
            for i in range(1, len(gb_record.features), 2):
                #Si se encuentran un gen imprimir su secuencia en DNA,RNA y aminoacidos
                if gb_record.features[i].qualifiers['gene'] == [gene]:
                    inicio = gb_record.features[i].location.nofuzzy_start
                    fin = inicio + 15
                    print("DNA:", gb_record.seq[inicio:fin])
                    print("RNA:", gb_record.seq[inicio:fin].transcribe())
                    print("Proteína:", gb_record.seq[inicio:fin].translate())


#Dar la ruta del archivo
path = "../docs/virus.gb"
#Determinar genes a buscar
genes = ["G", "L", "M", "N", "P"]

#Llamar a la funcion
resumen(path, genes)
