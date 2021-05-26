
'''
NAME
        arguments_at.py
VERSION
        [1.0]
AUTHOR
    	Luz Rosario Guevara Cruz <lrosarioguevara@gmail.com>
GITHUB REPOSITORY
        https://github.com/lro-guevara/python_class
DESCRIPTION
        This program calculates the AT content using commands arguments in a number of sequences
        and create a new file as the output.
CATEGORY
        Sequence analysis, DNA sequence, genomic sequence for example.
USAGE
	    Bioinformatic usage, run in python console.
ARGUMENTS
        [-i, --input]   [The path of input file]
        [-o, --output]  [The path of output file]
        [-h, --help]    [Shows help message]

INPUT
        4_dna_sequences.txt
OUTPUT
        .txt file with AT content of each sequence.
EXAMPLES
    Input: 4_dna_sequences.txt
    Output:at_dna_sequences.txt

'''

#Get the library needed to use arguments.
import argparse

#Create the parser
parser = argparse.ArgumentParser(description="This program calculates the AT content using commands arguments")

#Define the arguments
parser.add_argument("-i","--input",
                    metavar="path/to/file",
                    help="File with DNA sequences",
                    required=True)
parser.add_argument("-o","--output",
                    metavar="path/to/file",
                    help="Name of Output file",
                    required=False)

#Execute arguments
arguments = parser.parse_args()

#Create a function to calculate at_content
def get_at_content(dna, dec=2):
    if dna.count("N") > 0:
        raise ValueError(f'The sequence contains {dna.count("N")} N\'s')
    dna = (dna.replace('"', '')).replace("-", "")
    at_content = (dna.upper()).count("A") + (dna.upper()).count("T")/len(dna)
    return round(at_content, dec)
#Test that the path is correct
try:
    file = open(arguments.input)
#If the file is not found, we print the error and ask for the input file again
except IOError:
    print("File not found.")
    new_path = input("Insert the input file: ")
#Open the new file
    file = open(new_path)
#Read the content of the input file
data = file.readlines()
#Close the file
file.close()

#Open a new file as output
new_file = open("output/at_dna_sequences.txt", "w")

for sequence in data:
    #For everylne we split with "="
    split = sequence.split(" = ")
    #Write in the new file the sequence's name and using the function, the at content.
    new_file.write(f'> SEQ_{split[0]} has an {get_at_content(split)} of at content\n')
#Close the new file
new_file.close()