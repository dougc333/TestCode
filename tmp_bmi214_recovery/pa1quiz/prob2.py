import align_quiz_functions 


avg_mis = align_quiz_functions.count_mismatches("../../../q2_output/human_mouse.output")
avg_gap,avg_gap_len = align_quiz_functions.count_gaps("../../../q2_output/human_mouse.output")


print("avg_mis:",avg_mis,"avg_num_gaps:",avg_gap," avg_gap_len:",avg_gap_len)