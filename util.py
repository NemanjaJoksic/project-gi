from Bio import SeqIO


def read_fasta_file_to_string(input_file):
    string_squence = ''
    fasta_sequences = SeqIO.parse(open(input_file), 'fasta')
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        string_squence += sequence
    return string_squence