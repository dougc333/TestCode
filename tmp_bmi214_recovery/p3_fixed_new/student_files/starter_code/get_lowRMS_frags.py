"""
This script is used to calculate RMSD to native structure for all fragments in a library. 
This is useful for biased forward folding, which significantly speeds up computation.
*adapted from https://github.com/sarisabban/RosettaDesign/blob/master/Fragments.py
"""

import argparse
import utils

from pyrosetta import *
from pyrosetta.rosetta import *
init(extra_options='-mute all')



def main(fraglen, pdb):
	pose = pose_from_pdb(pdb)
	pdb_id = pdb.split('/')[-1][:-4]
	fragfile = '../data/{}_{}mers.frag'.format(pdb_id, fraglen)
	frag = open(fragfile, 'r')
	data = open('../data/{}_{}mers.rmsd'.format(pdb_id, fraglen), 'w')
	AVG = []

	for line in frag:
		if line.lstrip().startswith('position:'):
			line = line.split()
			size = line[1]
	frag.close()
	for i in range(1, int(size)+1):
		rmsd = []
		pose_copy = pyrosetta.Pose()
		pose_copy.assign(pose)
		frames = pyrosetta.rosetta.core.fragment.FrameList()
		fragset = pyrosetta.rosetta.core.fragment.ConstantLengthFragSet(fraglen)
		fragset.read_fragment_file(fragfile)
		fragset.frames(i, frames)
		movemap = MoveMap()
		movemap.set_bb(True)
		for frame in frames:
			for frag_num in range(1, frame.nr_frags()+1):
				frame.apply(movemap, frag_num, pose_copy)
				RMSD = rosetta.core.scoring.CA_rmsd(pose, pose_copy)
				data.write(str(i)+'\t'+str(frag_num)+'\t'+str(RMSD)+'\n')
				rmsd.append(RMSD)
				lowest = min(rmsd)
				pose_copy.assign(pose)
		AVG.append(lowest)
		print('\u001b[31mPosition:\u001b[0m {}\t\u001b[31mLowest RMSD:\u001b[0m {}\t|{}'.format(i, round(lowest, 3), '-'*int(lowest)))
	data.close()


if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--fraglen', type=int, default=9, help='fragment length')
	parser.add_argument('--pdb', type=str,  help='target PDB structure')
	args = parser.parse_args()
	main(args.fraglen, args.pdb)