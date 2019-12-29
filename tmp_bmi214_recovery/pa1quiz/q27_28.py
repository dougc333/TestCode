import align_quiz_functions

avg_gap,avg_gap_len = align_quiz_functions.count_gaps("../../../q2_output/human_chimp.output")
avg_mis = align_quiz_functions.count_mismatches("../../../q2_output/human_chimp.output")
print("open gap 5:")
avg_gap,avg_gap_len = align_quiz_functions.count_gaps("../../../q27.output")
avg_mis = align_quiz_functions.count_mismatches("../../../q27.output")
print("open gap 0.5:")
avg_gap,avg_gap_len = align_quiz_functions.count_gaps("../../../q28.output")
avg_mis = align_quiz_functions.count_mismatches("../../../q28.output")

