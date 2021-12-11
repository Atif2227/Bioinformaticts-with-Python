# This is the code testing File.

# Importing everything from dna_toolkit file.
from central_dogma_toolkit import *
from utilities import colored

# Taking user input DNA string.
#DNA_str = input("Input Your DNA string - ")
#my_DNA = validateSeq(DNA_str)
#print(f"\nYour DNA String is :{colored(my_DNA)}")

# Store the Randonly generated DNA into a variable, DNA_str.
DNA_str = validateSeq(rand_DNA_str)

# Getting coloured DNA string.
print(f'\nSequence: {colored(DNA_str)}\n')

# Getting The length of the DNA.
print(f'[1] -> Sequence Length: {len(DNA_str)}\n')

# Getting the Nucleotide frequency.
print(colored(f'[2] -> Nucleotide frequency: {CountNucFrequency(DNA_str)}\n'))

# Getting the transcribed sequence.
print(f'[3] -> Transcribed Sequence: {colored(transcription(DNA_str))}\n')

'''Print command for checking the reverse complement
print(reverse_complement(DNA_str))'''

# Getting the coloured DS DNA.
print(f"[4] -> Double Stranded DNA:\n 5'{colored(DNA_str)} 3'")

# Print command for showing line bond between complementary base pairs of the DS DNA strand.
print(f"   {''.join(['|' for i in range(len(DNA_str))])}")

# Reversing the reverse complement to get the complementary strand.
print(colored(f" 3'{(reverse_complement(DNA_str))[::-1]} 5'\n"))

# Getting the GC content.
print(f'[5] -> GC Content: {GC_content(DNA_str)}%\n')

# Getting the GC content of fixed length subsections of DNA.
print(
    f'[6] -> GC content in the Subsection where K = 5: {GC_content_subsec(DNA_str, k = 5)}\n')

# Getting the Codons from DNA string.
print(f'[7] -> Amino Acid Sequence from DNA: {translate_seq(DNA_str)}\n')

# Getting the frequency of a particular Amino Acid.
print(
    f'[8] -> Codon Frequency for Amino Acid (L): {codon_usage(DNA_str, "L")}\n')

print('[9] -> The Reading Frames:')
for frame in gen_reading_frames(DNA_str):
    print(frame)

# The above function could be tested with a test reading frames.
# test_rf = ['V', 'M', 'S', 'E', 'C', 'V',
#           'S', 'V', 'P', 'T', 'L', '_', 'T', 'N']
# print(proteins_from_rf(test_rf))

print('\n[10] + All Proteins in 6 Reading Frames:')
for prot in all_proteins_from_orfs(DNA_str, 0, 0, True):
    print(f'{prot}')

# Test the funtion 'all_proteins_from_orfs' witha real nucleotide sequence from NCBI.
# Copy the nucletide sequence from FASTA file.
# Store it as a string in any variable, e.g, NCBI_Nuc = "----"
# Now call the function with this  -> for prot in all_proteins_from_orfs(NBCI_Nuc, 0, 0, True):
# It will give you all possible protein sequence fron 6 RFs.
# Copy the translated sequence for the nucleotide from NCBI.
# Find the sequence in the console's output.
# If your code is correct you would get the protein sequence in the search for sure.
