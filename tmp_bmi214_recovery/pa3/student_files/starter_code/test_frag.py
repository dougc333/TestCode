
from FragmentSet import FragmentSet

fs = FragmentSet("../starter_data/helix_9mers.frag","../starter_data/helix_9mers.rmsd")
res = fs.get_lowRMS_fragments(1,3)
print(res)
