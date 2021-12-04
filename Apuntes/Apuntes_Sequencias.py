"""
DATE:  14/09/2021
TOPIC:  "SECUENCIAS"

"""

from Bio.Seq import Seq
from Bio import SeqIO


# Utilizar FastQ

path="files/sample.fastq"

mala_calidad = []
umbral = 40
for record in SeqIO.parse(path, "fastq"):
    promedio = sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quality"])
    if (promedio < umbral):
        mala_calidad.append((promedio, record.id))

print(len(mala_calidad))

# Acceder a GenBank

for gb_record in SeqIO.parse("./files/clase_2/aichi.gb", "genbank"):
    print('ID', gb_record.id)
    print('Secuencia', str(gb_record.seq)[0:30],'...')
    print('Longitud', len(gb_record))

for annotation, value in gb_record.annotations.items():
    print(annotation, value)

print(gb_record.annotations['date'])


## EJERCICIO 4
## Obtener organismo y versión de Virus.gb

path = "files/virus.gb"

for gb_record in SeqIO.parse(path, "genbank"):
    print("ID", gb_record.id)

## Obtener lo que se pide en forma de diccionario
version = gb_record.annotations['sequence_version']
organism = gb_record.annotations['organism']


# Acceder a GenBank features
f_source = gb_record.features[0]

f_cds = gb_record.features[1]

print(f_source.location)
print(f_source.type)
print(f_source.qualifiers)
print(f_source.qualifiers['organism'])
print(f_source.qualifiers['collection_date'])
print(f_cds.qualifiers['codon_start'])


## EJERCICIO 5
## Obtener datos del país y aislamiento

## Acceder a la primera posicion de la lista
aislado = gb_record.features[0].qualifiers["isolation_source"]

pais_origen = gb_record.features[0].qualifiers["country"]


# Acceder a Origin

start = gb_record.features[1].location.nofuzzy_start

end = gb_record.features[1].location.nofuzzy_end

new_seq = gb_record.seq[start:end]

translation = new_seq.translate()
