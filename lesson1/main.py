#DNA Toolkit/Code testing file
from DNAToolkit import *
import random

randDNAStr = ''.join([random.choice(Nucleotides)
					for nuc in range(200)])
#rndDNAStr = "ATTTGCcc"

DNAStr = validateSeq(randDNAStr)

print(countNucFrequency(DNAStr))
