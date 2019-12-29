import align_quiz_functions 

#print("quiz4 human bacteria")
#avg_mis = align_quiz_functions.count_mismatches("q4_output/quiz4_human_bacteria.output")
#avg_gap,avg_gap_len = align_quiz_functions.count_gaps("q4_output/quiz4_human_bacteria.output")
#print("quiz4 human bacteria")

def num_gap(a):
  num=0
  for x in a:
    if x=='_':
      num+=1
  return num

pairs = align_quiz_functions.read_seq_pairs("q4_output/quiz4_human_bacteria.output")
print(type(pairs),len(pairs))
print(len(pairs[0][0]))
print(len(pairs[0][1]))
#for x in pairs:
#  prin
results = []
for idx in range(0,len(pairs)):
  a,b = pairs[idx][0], pairs[idx][1]
  if idx==55293:
    print (a)
    print("-----")
    print (b)
  results.append((idx,num_gap(a),num_gap(b)))

print(max(results,key=lambda x:x[1]))
print(max(results,key=lambda x:x[2]))
(55293, 66, 72)
print(results[55293])

a="LLAVYTGPGPVKDVFSTTNRMTVLLITND_VLARGGFKANFTTGYHL____GIPEPCKA_DHFQCKNGECVPLVN_LCDGHL_HCEDGSDEADCVRFFNG__TTNNNGLVRFRI_QSIWHTACAENWTTQISND_VC_QLLGLGSGN_SSKPI_FPTDG_GPF__V_KLNTAPDGH_LILTPSQQCLQDSLIRLQCNHKSCGKKLAAQDITPKIVGGSNAKEGAWPWVVGLYYGGRL_LCGASLVSSDWLVSAAHCVYGRNLEPSKWTAILGLH__MKSNLTSPQTVPRLIDEIVINPHYNRRR__KDNDIAMMHLEFKVNYTDYIQPICLPE_ENQVF_PPGRNCSIAGWGTVVYQGTT_____ANILQEADVPL_LSNERCQQQ_MPEYNITENMICAGYEEGGIDSCQGDS______________________________GGPLMCQENNRWFLAGVTSFGYKCALPNRPGVYARVSRFTEWIQS__F"
b="LLAVYTGQGPLPDVFSTTNQMTVILFT_DKIVTKQGFLANFTTGYHLGGSKG___AC_TLEEYQCRSGECIPL_HNLCD_NLPQCEDGSDEAKCMRLLNGSLST__KGLVQVRIGKT_WHLACADDWNEQIS_DSVCQQ_LGLGDANMSS_TVLF_T_GDGPFAAITK__TA_N_QSLIFT___________R___________________________RE_AWPWVVSLHFNS_MHLCGASLVSEEWLVTAAHCVYGRHLQPSKWKAVLGLHDQL__NMTHPSTVVRYINQIIINPHYN__KLTKDSDIALMHLQYKVQYTDYIQPVCLPEKNQQ_FLP_GTSCFIAGWG_____DTTSGGSSSNILQEAEVPLIL_NDKC_QQWMPEYSITENMICAGYDTGGIDSCQGDSKRNGHDFEQSYIKMATLVSVDIRLELATGPGGPLMFEDGNKWVLVGVTSFGYKCALPERPGVYTRVTMFVDWIQNTIY"
print(num_gap(a))
print(num_gap(b))