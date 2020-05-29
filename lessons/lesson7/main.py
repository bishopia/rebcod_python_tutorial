#DNA Toolkit/Code testing file
from DNAToolkit import *
from utilities import colored
import random


randDNAStr = ''.join([random.choice(Nucleotides)
					for nuc in range(50)])
#rndDNAStr = "ATTTGCcc"

DNAStr = validateSeq(randDNAStr)

# print(f'\nSequence: {DNAStr}\n')
# print(f'[1] + Sequence Length: {len(DNAStr)}\n')
# print(f'[2] + Nucleotide Frequency: {nucleotide_frequency(DNAStr)}\n')

# print(f'[3] + DNA/RNA Transcription: {transcription(DNAStr)}\n')

# print(f"[4] + DNA String + Complement + Reverse Complement:\n5' {DNAStr} 3'")
# print(f"    {''.join(['|' for c in range(len(DNAStr))])}")
# print(f"3' {reverse_complement(DNAStr)[::-1]} 5' [Complement]")
# print(f"5' {reverse_complement(DNAStr)} 3' [Rev. Complement]\n")

# print(f'[5] + GC content: {gc_content(DNAStr)}%\n')
# print(f'[6] + GC content in windows of size k=5: {gc_content_subsec(DNAStr, k=5)}\n')

# print(f'[7] + Amino acid sequence from DNA: {translate_seq(DNAStr, 0)}\n')
# # print(f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")}\n')

# print('[9] + Reading frames:')
# for frame in gen_reading_frames(DNAStr):
#     print(frame)

print('\n[10] + All proteins in all ORFs:')
for prot in all_proteins_from_orfs(NM_000207, 0, 0, True):
    print(f'{prot}')
