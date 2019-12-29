from FragmentSet import *

fs_3 = FragmentSet("../starter_data/helix_3mers.frag","../starter_data/helix_3mers.rmsd")

print("fs3 max_pos:",fs_3.get_max_pos())
print(fs_3.topN)

print(fs_3.get_lowRMS_fragments(1,3))