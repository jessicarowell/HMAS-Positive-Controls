#!/usr/bin/env python

# Author: Jessica Rowell
# Data modified: 8/6/2019

# Make positive controls for primers using the PhiX genome: 
# Use a sliding window function (window size = length of amplicon) to go along PhiX sequence.
# When GC content of the PhiX fragment = GC content(+-5%) of the target amplicon for that primer pair, 
#   slap the forward primer at the beginning and the reverse rpimer (its reverse complement) to the end

# Inputs: PhiX genome (https://www.ncbi.nlm.nih.gov/nucleotide/NC_001422)
#         all entries from enterics.amr.fixed.genotypes.txt that target the following genes: 
#           aac(s)-Id, aadA7, blaCMY-1, blaCTX-M-15, blaTEM-1, drfA32, qnrB, msr(E)
#         Retrieved via: grep -wf twist_10seqs_loose.txt ../enterics.amr.fixed.genotypes_annotated.txt > enterics.amr.fixed.genotypes_twist10.txt

# Output: positive control sequences and corresponding ids (id_genome):

from Bio.Seq import Seq

## Functions
# Adapted from: https://scipher.wordpress.com/2010/12/02/simple-sliding-window-iterator-in-python/
def slidingWindow(sequence,winSize,step=1):
    """Returns a generator that will iterate through
    the defined chunks of input sequence.  Input sequence
    must be iterable."""
 
    # Verify the inputs
    try: it = iter(sequence)
    except TypeError:
        raise Exception("**ERROR** sequence must be iterable.")
    if not ((type(winSize) == type(0)) and (type(step) == type(0))):
        raise Exception("**ERROR** type(winSize) and type(step) must be int.")
    if step > winSize:
        raise Exception("**ERROR** step must not be larger than winSize.")
    if winSize > len(sequence):
        raise Exception("**ERROR** winSize must not be larger than sequence length.")
 
    # Pre-compute number of chunks to emit
    numOfChunks = int(((len(sequence)-winSize)/step)+1)
 
    # Do the work
    for i in range(0,numOfChunks*step,step):
        yield sequence[i:i+winSize]
    

# Import PhiX
phiX = open("/scicomp/home/ick4/data/amr_panel/twist/NC_001422.1_phiX174.fasta","r")
seq = phiX.read()
bare_seq = seq.split("\n",1)[1] # Sequence without the header (iterable)
   

positive_controls_id = [] # Store identifying info here
positive_controls_seq = [] # Store positive control sequence, with its primers, here
not_found = []
with open('/scicomp/home/ick4/data/amr_panel/twist/enterics.amr.fixed.genotypes_twistAll.txt') as f:
    for line in f:
        line = line.rstrip()
        # For each target, grab: group_id (column 1), genome (4), amplicon length (7), gc content (8), forward and reverse primers(5-6) 
        id = line.split("\t")[0]
        genome = line.split("\t")[3]
        amplicon = line.split("\t")[8]      
        gc = int(line.split("\t")[7])
        (fwd, rev) = line.split("\t")[4:6]
        # Create the reverse complement of the reverse primer
        rev_seq = Seq(rev)
        rev_rcompl = rev_seq.reverse_complement()
        #rev_rcompl = str(rev_rcompl)
        # Window size = amplicon length minus length of fwd and rev primers
        window_size = len(amplicon) - len(fwd) - len(rev)
        frag = amplicon[len(fwd):(len(amplicon)-len(rev))] # Don't really need this - it's the target without the primers
        # Use a sliding window function to go along PhiX. Check GC content for each window.
        windows = slidingWindow(bare_seq, window_size, step=1)
        print(windows)
        print("Next")
        id2 = id + "_" + genome
        found = 0
        for i in windows:
            # When GC content = same as file, save this window as the pos ctrl fragment & add primers to it
            dna_list = list(i)
            gc_count = dna_list.count("G") + dna_list.count("C")
            gc_frac = int((gc_count / len(dna_list))*100)
            if (gc - 5) < gc_frac < (gc + 10):
                found = 1                
                new_frag = fwd + i + rev_rcompl
                positive_controls_seq.append(new_frag)
                positive_controls_id.append(id2)
                break
        if found == 0:
            id2 = id + "_" + genome
            #print("No suitable window found for: ", id, genome, sep=' ', end='\n')

print("Number of suitable windows found = ", end=" ")
print(len(positive_controls_id))
print("Number of suitable windows not found = ", end=" ")
print(len(not_found))


# Output it with identifying data from enterics file: group_id, genome
#with open('/scicomp/home/ick4/data/amr_panel/twist/positive_controls.txt', 'w') as f:
    #for k in range(0,len(positive_controls_id)):
       #f.write('\t'.join(positive_controls_id[k], positive_controls_seq[k]) + "\n")
       #print(positive_controls_seq[k], end="\n")    
     #print(positive_controls_id[k]\t%s\t % positive_controls_seq[k])
with open('/scicomp/home/ick4/data/amr_panel/twist/positive_controls.txt', 'w') as f:
    for k in range(0,len(positive_controls_id)):
        print(positive_controls_id[k], end="\t", file=f)
        print(positive_controls_seq[k], file=f)    
