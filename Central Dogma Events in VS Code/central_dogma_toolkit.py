# This file has all the fuctions for different events of Central Dogma.
import random
from typing import Counter
from structures import *


# Generating Random DNA string of fixed length.
rand_DNA_str = ''.join([random.choice(Nucleotides)
                        for x in range(40)])


def validateSeq(seq):
    """Checks if the DNA sequence is a valid DNA sequence or not."""
    tmpseq = seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return "not a DNA String."
    return tmpseq


def CountNucFrequency(seq):
    '''Counts the frequency of Nucleotides in the Nucleotide string.'''
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for i in seq:
        tmpFreqDict[i] += 1
    return tmpFreqDict


def transcription(seq):
    '''Transcribes the DNA into RNA'''
    return seq.replace('T', 'U')


def reverse_complement(seq):
    '''Makes the reverse complement of the DNA string'''
    return''.join([DNA_Reversecomplement[i]
                  for i in seq])[:: -1]


def GC_content(seq):
    '''Gives the total GC content(%) of a sequence.'''
    return round((seq.count('G') + seq.count('')) / len(seq) * 100)


def GC_content_subsec(seq, k=20):
    '''Returns the GC content from fixed lenth sub-section of the given DNA string.'''
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(GC_content(subseq))
    return res


def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    return [DNA_Codons[seq[i:i + 3]] for i in range(init_pos, len(seq) - 2, 3)]


def codon_usage(seq, aminoacid):
    """Provides the frequency of asked aminoacid with its codon in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict


def gen_reading_frames(seq):
    '''Generate the six reading frames of a DNA sequence.'''
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq), 0))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 2))
    return frames


def proteins_from_rf(aa_seq):
    """Compute all possible proteins in an aminoacid seq and return a list of possible proteins"""
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            # STOP accumulating amino acids if _ - STOP was found
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            # START accumulating amino acids if M - START was found
            if aa == "M":
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return proteins


def all_proteins_from_orfs(self, startReadPos=0, endReadPos=0, ordered=False):
    """Compute all possible proteins for all open reading frames"""

    if endReadPos > startReadPos:
        rfs = gen_reading_frames(self[startRead:endRead])
    else:
        rfs = gen_reading_frames(self)

    res = []
    for rf in rfs:
        prots = proteins_from_rf(rf)
        for p in prots:
            res.append(p)

    if ordered:
        return sorted(res, key=len, reverse=True)
    return res
