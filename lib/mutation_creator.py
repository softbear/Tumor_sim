from Bio import SeqIO
from random import randint

class Mutation_Creator:
    def create_deletion(self, mutable_seq, start, end):
        return mutable_seq[:start] + mutable_seq[end:]

    def create_snv(self, mutable_seq, start, new_base):
        mutable_seq[start] = new_base
        return mutable_seq

    def create_insertion(self, mutable_seq, start, new_seq):
        return mutable_seq[:start] + new_seq +  mutable_seq[start:]

    def create_inversion(self, mutable_seq, start, end):
        inv_seq = mutable_seq[start:end]
        inv_seq.reverse()
        mutable_seq[start:end] = inv_seq
        return mutable_seq

    def create_translocation(self, seq1, seq2, start1, start2, length1, length2):
        new_seq1 = self.create_deletion(seq1, start1,start1+length1)
        new_seq1 = self.create_insertion(new_seq1, start1, seq2[start2:start2+length2])
        new_seq2 = self.create_deletion(seq2, start2,start2+length2)
        new_seq2 = self.create_insertion(new_seq2, start2, seq1[start1:start1+length1])
        return (new_seq1, new_seq2)
