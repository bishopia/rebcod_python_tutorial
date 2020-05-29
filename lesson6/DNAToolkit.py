#DNA Toolkit file
from collections import Counter
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


def translate_seq(seq, init_pos=0):
	"""Translates a DNA sequence into an amino acid sequence"""
	return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]


# def codon_usage(seq, aminoacid):
# 	"""Provides frequency of each codon encoding a given amino acid in a DNA sequence"""
# 	tmpList = []
# 	for i in range(0, len(seq) - 2, 3):
# 		if DNA_Codons[seq[i:i + 3] == aminoacid:
# 			tmpList.append(seq[i:i + 3])

# 	freqDict = dict(collections.Counter(tmpList)) #CANNOT FIGURE OUT WHY THIS DOESN'T WORK
# 	totalWight = sum(freqDict.values())
# 	for seq in freqDict:
# 		freqDict[seq] = round(freqDict[seq] / totalWight, 2)
# 	return freqDict


def gen_reading_frames(seq):
	"""generates six reading frames of a DNA sequence, 3 each from template and reverse complement string"""
	frames = []
	frames.append(translate_seq(seq, 0))
	frames.append(translate_seq(seq, 1))
	frames.append(translate_seq(seq, 2))
	frames.append(translate_seq(reverse_complement(seq), 0))
	frames.append(translate_seq(reverse_complement(seq), 1))
	frames.append(translate_seq(reverse_complement(seq), 2))
	return frames


def proteins_from_rf(aa_seq):
	"""compute all posible proteins in an aminoacid seq and return a list of possible proteins"""
	current_prot = []
	proteins = []
	for aa in aa_seq:
		if aa == "_":
			#STOP accumulating amino acides if _ - STOP was found
			if current_prot:
				for p in current_prot:
					proteins.append(p)
				current_prot = []
		else:
			#START accumulating amino acides if M - START was found
			if aa == "M":
				current_prot.append("")
			for i in range(len(current_prot)):
				current_prot[i] += aa
	return proteins
