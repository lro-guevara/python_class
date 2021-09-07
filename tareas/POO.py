'''
##  NAME
       POO.py
##  VERSION
        [0.0.1]
##  AUTHOR
	Luz Rosario Guevara Cruz <lguevara@lcg.unam.mx>

##  GITHUB REPOSITORY
	https://github.com/lro-guevara/python_class
##  DATE
    [2021/09/06]
##  DESCRIPTION
    This program evaluates the characteristics of an input biomolecule by calling different functions.
##  CATEGORY
        [biochemical analysis, genomic sequence for example]
##  USAGE
    Bioinformatic usage
    Python 3.9

##  INPUT
    Biomolecular characters
OUTPUT
    Specific data about input
EXAMPLES
    Input:
    DNA = a_nucleicos('CHONP','nucleotido','7.5')
    DNA.gc_percentage('AATGCGC')
    Output:
    {'elementos': 'CHONP', 'unidad': 'nucleotido', 'pH': '7.5'}
    GC content:
    57.14285714285714
'''

class biomoleculas():
    def __init__(self, elementos, unidad, pH):
        self.elementos = elementos
        self.unidad = unidad
        self.pH = pH


class lipido(biomoleculas):
    saponificables = False
    no_saponificable = False

    def saponificables(self):
        self.Saponificables = True
        self.No_saponificable = False

    def no_saponificable(self):
        self.no_saponificable = True
        self.saponificable = True

    def tipe(self):
        print(self.saponificable)
        print(self.no_saponificable)

class azucares(biomoleculas):
    Soluble = False
    Insoluble = False

    def estructura(self, estructura):
        self.estructura = estructura  # monosacaridos,oligosacaridos, polisacaridos

    def Soluble(self):
        self.Insoluble = True
    def Insoluble (self):
        self.Insoluble = True
    def tipe(self):
        print(self.Soluble)
        print(self.Insoluble)

class proteinas(biomoleculas):
    def aminoacidos(self, secuencia_aa):
        self.secuencia_aa = secuencia_aa
        self.length = len(secuencia_aa)


class a_nucleicos(biomoleculas):
    def gc_percentage(self, sec):
        self.sec = sec
        gc_total = (self.sec.count('G')) + (self.sec.count('C'))
        percentage = gc_total / len(self.sec) * 100
        print ("GC content:")
        print(percentage)

DNA = a_nucleicos('CHONP','nucleotido','7.5')
print(DNA.__dict__)
DNA.gc_percentage('AATGCGC')