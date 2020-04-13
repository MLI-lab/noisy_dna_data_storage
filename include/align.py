from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO
import operator

def multiple_alignment(cluster,out=False):
    # write cluster to file
    file = open("cl.fasta","w") 
    for i,c in enumerate(cluster):
        file.write(">S%d\n" % i)
        file.write(c)
        file.write("\n")
    file.close()

    #muscle_exe = r"./muscle3.8.31_i86darwin64" 
    muscle_exe = r"~/muscle3.8.31_i86linux64"
    output_alignment = "output_alignment.fasta"
    muscle_cline = MuscleCommandline(muscle_exe, input="cl.fasta", out=output_alignment)
    stdout, stderr = muscle_cline()
    msa = AlignIO.read(output_alignment, "fasta")
    if out:
        print(msa)
    alignedcluster = []
    for i in msa:
        alignedcluster += [i.seq]
    return alignedcluster

def majority_merge(reads,weight = 0.4):
    # assume reads have the same lenght
    res = ""
    for i in range(len(reads[0])):
        counts = {'A':0,'C':0,'G':0,'T':0,'-':0,'N':0}
        for j in range(len(reads)):
            counts[reads[j][i]] +=1
        counts['-'] *= weight
        mv = max(counts.items(), key=operator.itemgetter(1))[0]
        if mv != '-':
            res += mv
    return res

def make60s(seq,target_len=60):
    res = []
    for i in range(len(seq)-target_len+1):
        res += [seq[i:i+60]]
    return res

def generatesubseq(seq,target_length):
    seqs = []
    for i in range(len(seq)-target_length+1):
        seqs.append( seq[i:i+target_length] )
    #seqs = [seq[:target_length]]
    return seqs
