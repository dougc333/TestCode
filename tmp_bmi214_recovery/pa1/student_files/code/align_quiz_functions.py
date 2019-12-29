"""
Helper functions for the quiz.
These are applied to output alignments (and in one case also the input alignment).

To run, write code that calls each function with the appropriate input/output files.
"""

def is_number(s):
    """
    Check if a string is a number.

    Inputs:
      s = string
    Returns:
      True if it is a number, False if it is not
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def read_seq_pairs(fname):
    """
    Reads in pairs of alignments in an output.

    Inputs:
       fname = the name of an alignment output file

    Returns:
       pairs = a list of tuples, each tuple is an alignment
    """
    # read the alignments
    pairs = []
    new_pair = ''
    with open(fname, 'r') as f:
        for line in f.readlines():
            # skip score line
            if is_number(line.strip()):
                continue
            # start a new pair at a blank line
            elif len(line.strip()) == 0:
                # store previous pairs
                if len(new_pair) == 2:
                    pairs.append(new_pair)
                new_pair = []
            else:
                new_pair.append(line.strip())
        # store the last pair
        if len(new_pair) == 2:
            pairs.append(new_pair)
    return pairs


def find_align_location(input_file, output_file):
    """
    Reads in an input_file and output alignment, and finds the 
    locations of the alignments within the original sequences.

    Inputs:
       input_file = a file with the input to an alignment
       output_file = the corresponding alignment output file, after running alignment

    Returns:
       the location of the last alignment. This is formatted as (a, b) 
        where a is the location of align_a within seq_a and b is the location of
        align_b within seq_b
    """
    with(open(input_file, 'r')) as infile:
        seq_a = infile.readline().strip()
        seq_b = infile.readline().strip()

    pairs = read_seq_pairs(output_file)
    for pair in pairs:
        align_a = pair[0].replace("_", "")
        align_b = pair[1].replace("_", "")
        loc1 = seq_a.find(align_a)
        loc2 = seq_b.find(align_b)
        print(loc1, loc2)

    return (loc1, loc2)


def compare_alignments(outfile1, outfile2):
    """
    Compares two sets of alignments from two different output files.

    Inputs:
        outfile1 = output file from alignment
        outfile2 = output file to compare it to

    Returns:
        True if the alignments match, False if they do not
      During the program, also prints whether they match, and what does not match.
    """
    pairs1 = set(["%s %s" %(pair[0], pair[1]) for pair in read_seq_pairs(outfile1)])
    pairs2 = set(["%s %s" %(pair[0], pair[1]) for pair in read_seq_pairs(outfile2)])
    diff1 = pairs1.difference(pairs2)
    diff2 = pairs2.difference(pairs1)
    if len(diff1) == 0 and len(diff2) == 0:
        print("Alignments match!")
        return True
    else:
        print("%d alignments in file 1 that are not in file 2.\n\t%s" %(len(diff1), diff1))
        print("%d alignments in file 2 that are not in file 1.\n\t%s" %(len(diff2), diff2))
        return False
    


def count_mismatches(fname):
    """
    Counts the number of mismatches in an alignment.
        Gaps are not included in mismatches!
    Takes as input an alignment output file, prints average across alignments.
    
    Inputs:
       fname = the name of an alignment output file

    Returns:
       the average number of mismatches 
    """
    pairs = read_seq_pairs(fname)

    # go through the pairs and count
    mismatch_count = []
    for pair in pairs:
        num_mismatches = 0
        [seqA, seqB] = pair
        for i in range(0, len(seqA)):
            if ((seqA[i] != seqB[i]) and (seqA[i] != '_') and (seqB[i] != '_')):
                num_mismatches = num_mismatches + 1
        mismatch_count.append(num_mismatches)

    # calculate the average
    avg_mismatches = float(sum(mismatch_count))/len(pairs) 
    print("Average number of mismatches per alignment: %.2f" %avg_mismatches)
    return avg_mismatches

def count_gaps(fname):
    """
    Counts the gaps in an alignment. 
    Takes as input an alignment output file.
    Prints out the average number per alignment and average of avg gap lengths per alignment.
    
    Inputs:
       fname = the name of an alignment output file

    Outputs:
       a tuple containing the average number of gaps and average gap length
    """
    pairs = read_seq_pairs(fname)
    # go thru the pairs and count gaps
    num_gaps = []
    gap_length = []
    for pair in pairs:
        [seqA, seqB] = pair
        curr_gap = False # keep track of whether 
        gap_len = 0
        gap_list = []
        for i in range(0, len(seqA)):
            # gap
            if ((seqA[i]=='_') or (seqB[i] =='_')): 
                if not curr_gap: # start a new gap
                    curr_gap = True
                    gap_len = 1
                else: # add to gap length
                    gap_len = gap_len+1
			# no gap
            else: 
                # if the previous was a gap, add it to the list
                if curr_gap:
                    gap_list.append(gap_len)
                    curr_gap = False
        num_gaps.append(len(gap_list))
        avg_gap_length = float(sum(gap_list))/len(gap_list)
        gap_length.append(avg_gap_length) # avg gap length for each

    # calculate the averages
    avg_num_gaps = float(sum(num_gaps))/len(pairs)
    avg_length_all = float(sum(gap_length))/len(pairs)
    print("Average number of gaps per alignment: %.2f" %avg_num_gaps)
    print("Average length of gaps (this is the average of all averages): %.2f" %avg_length_all)
    return (avg_num_gaps, avg_length_all)



