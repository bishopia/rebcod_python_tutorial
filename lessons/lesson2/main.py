#DNA Toolkit/Code testing file
from DNAToolkit import *
from utilities import colored
import random


randDNAStr = ''.join([random.choice(Nucleotides)
					for nuc in range(50)])
#rndDNAStr = "ATTTGCcc"

DNAStr = validateSeq(randDNAStr)

print(f'\nSequence: {DNAStr}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(f'[2] + Nucleotide Frequency: {nucleotide_frequency(DNAStr)}\n')

print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')

print(f"[4] + DNA String + Complement + Reverse Complement:\n5' {DNAStr} 3'")
print(f"    {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n")
