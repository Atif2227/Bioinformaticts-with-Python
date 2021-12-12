# This is the code testing File

from CDE_class import bio_seq

test_dna = bio_seq()

test_dna.generate_rnd_seq(50, "DNA")
print("Sequence Information:", test_dna.get_seq_info(), "\n")
print("Nucleotide Frequency:", test_dna.nucleotide_frequency(), "\n")
print("The RNA(transcript):", test_dna.transcription(), "\n")
print("The Reverse Compliment DNA:", test_dna.reverse_complement(), "\n")
print("GC Content of the Sequence:", test_dna.gc_content(), "\n")
print("GC Content of the subsection:", test_dna.gc_content_subsec(), "\n")
print("Translation:", test_dna.translate_seq(), "\n")
print("Codon Frequency/Percentage:", test_dna.codon_usage("L"), "\n")

# Generating 6 Reading frames
print("All 6 Reading Frames:")
for rf in test_dna.gen_reading_frames():
    print(rf)

# print(test_dna.proteins_from_rf(['Q', 'M', 'T', 'C', 'D','S', 'P', 'Q', 'P', 'R', 'A', 'F', 'D', 'Y', '_', 'S']))

print("\nPossible Proteins from the RFs:", test_dna.all_proteins_from_orfs())
