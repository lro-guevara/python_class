# import Bio.Seq
from Bio.Seq import Seq
from Bio.Seq import MutableSeq

seqobj = Seq("ATCGTG")
print(str(seqobj))

mutable = MutableSeq(seqobj)
mutable[0] = "n"

print(seqobj.complement())
print(seqobj.reverse_complement())
print(seqobj.translate(to_stop=True))
rna = seqobj.transcribe()
print(rna.back_transcribe())
print(seqobj[0:3])

import re

for codon in re.findall(r"(.{3})", str(seqobj)):
    print(codon)

from Bio.Seq import SeqUtils
from Bio.SeqUtils import nt_search

patron = Seq("ACG")
sequence = Seq("ATGCGCACGGCGTGATCAGCTTATAGCCGTACG")
resultado = nt_search(str(sequence), patron.reverrse_complement())
print(resultado)

print(GC(sequence))
print(molecular_weight(sequence))

# Exercise 1

secuencia = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
inicio = Seq("ATG")
posicion = nt_search(str(secuencia), inicio)

for i in range(1, len(posicion)): #Empieza en posicion para saltar patron a buscar
    #Guarda secuenci en posicion de codon de inicio
    sec_prot = secuencia[i:]
    # Traducir secuencia hasta codon de paro
    proteina = sec_prot.translate(to_stop=True)
    print(proteina)

###############

from Bio import SeqIO
filename= "files/seq.nt.fa"
#Revisa cada seqrecords del archivo
for seq_record in SeqIO.parse(filename,"fasta"):
    print("ID{}".format(seq_record.id))
    print("len{}".format(len(seq_record))
    print("Traduccion{}",format(seq_record.seq.translate(to_stop=False)))

#Leer archivo en diccionario
id_dict = SeqIO.to_dict(SeqIO.parse(filename, "fasta"))

