#DNA Toolkit file
import collections
from structures import *


def validateSeq(dna_seq):
	"""Confirms tha string sequence is proper DNA sequence, contains only CATG (any case)"""
	tmpseq = dna_seq.upper()
	for nuc in tmpseq:
		if nuc not in Nucleotides:
			return False
	return tmpseq


def nucleotide_frequency(seq):
	"""Counts frequency of each nucleotide in sequence"""
	tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
	for nuc in seq:
		tmpFreqDict[nuc] += 1
	return tmpFreqDict
	#return dict(collections.Counter(seq))


def transcription(seq):
	"""DNA ---> RNA Transcription. Replaces thymine with uracil"""
	#DNA --> RNA transcription
	return seq.replace("T", "U")


def reverse_complement(seq):
	"""Swapping in complementary nucleotide, then reversing generated string"""

	#last part is python way of reversing string
	# return(''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1])

	#more optimized, pythonic solution
	mapping = str.maketrans('ATCG', 'TAGC')
	return seq.translate(mapping)[::-1]


def gc_content(seq):
	""" GC content of DNA/RNA sequence"""
	return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subsec(seq, k=20):
	""" GC content of DNA/RNA sub-sequence of length k. k=20 by default"""
	res = []
	for i in range(0, len(seq) - k + 1, k):
		subseq = seq[i:i + k]
		res.append(gc_content(subseq))
	return(res)
