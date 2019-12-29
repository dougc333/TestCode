import align_quiz_functions 



avg_mis = align_quiz_functions.count_mismatches("../../../q4_output/quiz4_human_bacteria.output")
avg_gap,avg_gap_len = align_quiz_functions.count_gaps("../../../q4_output/quiz4_human_bacteria.output")


#align_quiz_functions.find_align_location("../quiz_input/quiz4_human_bacteria.input", "../../../q4_output/quiz4_human_bacteria.output")

#confusing there is no question 2
#align_quiz_functions.compare_alignments("","../../../q4_output/quiz4_human_bacteria.output")