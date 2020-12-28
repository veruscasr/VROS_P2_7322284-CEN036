
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

with open("sequencia.fasta", "r") as seq_file:
        for record in SeqIO.parse(seq_file, "fasta"):
            seq_dna = record.seq
            complementar = seq_dna.complement()

print(seq_dna)
print(complementar)

#1 Getting ORFs
def getORFs(dna, frame):
    #frame_count = 0
    for i in range(frame, len(dna), 3):
        codon1 = dna[i:i+3]
        if codon1 == 'atg':
            start = i
            for j in range(start, len(dna), 3):
                codon2 = dna[j:j+3]
                if codon2 in ['taa', 'tag', 'tga']:
                    end = j
                    orflength = end-start+3
                    #frame_count += 1 
                    #100 - 0+3 = 97
                    orf = dna[start:end+3]
                    yield [orflength, orf, start, end+3] #frame_count]

#2 Create a list with all ORFs
sequencias = [seq_dna, complementar]
orfs = []
frames = [0,1,2]

for a in sequencias:
    for i in frames:
        for j in getORFs(a, i):
            orfs.append(j)
print(orfs)

#3 Getting the ORF with max length
maxLengthORF = [] 
from operator import itemgetter
def getMaxLengthORF(orfList, i):
    return max(enumerate(map(itemgetter(i), orfList)), key=itemgetter(1))

maxLengthORF.append(getMaxLengthORF(orfs, -1))
print(maxLengthORF)

#4 Translating the ORF with max length 
maxLengthORFIndex = maxLengthORF[0][0]
novo_maxLengthORFIndex = maxLengthORF[0][1]
orfToTranslate = orfs[1][maxLengthORFIndex]
print(orfToTranslate.translate(stop_symbol=""))

#5 Generate ORF.faa and ORF.fna
#ORF mais comprido no ORF.fna 
#Sequencia fasta
#id original + _frameX_START_END

#peptidio do maior ORF no ORF.faa 
#Sequencia fasta
#id original + _frameX_START_END

#GERAR OUTPUT
import os
print(seq_dna.id)
    
    



