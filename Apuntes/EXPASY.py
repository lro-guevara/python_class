"""
DATE: 12/10/2021
TOPIC: EXPASY
"""

## EJERCICIO 1
## Acceder a UniProtKB, gen DEFA de organismo A. aegypti

from Bio import Entrez, SeqIO

# Acceder
Entrez.email = "lguevara@lcg.unam.mx"
handle = Entrez.esearch(db="protein", term="Aedes aegypti[Orgn] AND DEFA[Gene]")
record = Entrez.read(handle)

print(record["IdList"])

handle = Entrez.efetch(db="protein", id=record["IdList"][0], rettype="gb", retmode="text")

record = SeqIO.read(handle, "genbank")

print(record.annotations["db_source"])

DEFA_prot = record.annotations['accessions']

db_source = record.annotations["db_source"]


# Uso de SWISS-PROT
# ExPASy accede a la base de datos de ExPASy
# SwissProt lee archivos

# EJERCICIO 2

from Bio import ExPASy   # Para archivo crudo
from Bio import SwissProt   # Para leerlo

handle = ExPASy.get_sprot_raw(DEFA_prot)

record = SwissProt.read(handle)

# Explorar record
print(record.created)  # Fecha de creacion
print(record.annotation_update)  # Actualizacion
print(record.taxonomy_id)  # ID

# EJERCICIO 3

# Crear un objeto SeqRecord

import Bio.SeqRecord, Bio.Seq

objeto_SeqRecord = Bio.SeqRecord.SeqRecord(seq=Bio.Seq.Seq(record.sequence),  # Crear objeto de secuencia
                                           id=record.entry_name,  # Dar ID
                                           name=record.organism)  # Dar nombre


handle = ExPASy.get_sprot_raw('P91793')

record = SeqIO.read(handle, "swiss")
print(record.__dict__.keys())

print(objeto_SeqRecord.format("fasta"))


### PROSITE

print('PDOC00627')
from Bio import ExPASy
from Bio.ExPASy import Prosite
handle = ExPASy.get_prosite_raw("PS00785")
record = Prosite.read(handle)
print (record.name)

print(record._dict_.keys())

print(record.pdoc)

from Bio.ExPASy import ScanProsite
sequence = "MEHKEVVLLLLLFLKSGQGEPLDDYVNTQGASLFSVTKKQLGAGSIEECAAKCEEDEEFTCRAFQYHSKEQQCVIMAENRKSSIIIRMRDVVLFEKKVYLSECKTG" \
           "NGKNYRGTMSKTKN"
handle = ScanProsite.scan(seq=sequence)
result = ScanProsite.read(handle)
print(type(result))

print(result[0])

handle = ExPASy.get_sprot_raw("PS50948")
record = Prosite.read(handle)