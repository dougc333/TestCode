import align_quiz_functions 

print("quiz4 p20")
avg_mis = align_quiz_functions.count_mismatches("trypsin_global.output")
avg_gap,avg_gap_len = align_quiz_functions.count_gaps("trypsin_global.output")
align_quiz_functions.find_align_location("pa1/student_files/quiz_input/quiz3_trypsin_domain.input", "trypsin_global.output")
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
