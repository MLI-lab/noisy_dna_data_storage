import numpy as np

def file_to_list(filename):
    seqs = []
    with open(filename) as f:
        for line in f:
            seqs += [line[0:-1]]
    return seqs

def fastq_to_list(fastq_filename):
    seqs = []
    with open(fastq_filename) as f:
        for i,line in enumerate(f):
            if (i + 3) % 4 == 0:
                seqs += [line[0:-1]]
    return seqs


def seq_stats(seqs):
    length = np.zeros(200)
    nucleotides = np.zeros(4)
    total = 0
    ctr = 0
    for seq in seqs:
        ctr += 1
        length[len(seq)] += 1
        nucleotides[0] += seq.count('A')
        nucleotides[1] += seq.count('C')
        nucleotides[2] += seq.count('G')
        nucleotides[3] += seq.count('T')
        total += len(seq)
    return length, nucleotides/total,ctr

def fraction_recovered(candidates,orig_seqs):
    d = {}
    for seq in orig_seqs:
        d[seq] = 0
    for cand in candidates:
        if cand in d:
            d[cand] += 1
    av = sum([ d[seq]>0 for seq in d]) / len(d)
    print("Fraction of recovered sequences: ", av )
    if av>0:
        print("Fraction of recovered sequences: ", sum([ d[seq] for seq in d]) / len(d) / av )