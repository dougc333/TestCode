"""
Utility functions. 
You may add your own functions as necessary, but DO NOT MODIFY THESE FUNCTIONS.
"""
import numpy as np
import Bio.PDB
from pyrosetta.rosetta.protocols.relax import FastRelax
from Protein import Protein
from pyrosetta import *
from pyrosetta.rosetta import *
init(extra_options = "-mute all -constant_seed")

pdb_parser = Bio.PDB.PDBParser(QUIET=True)
scorefxn_centroid = create_score_function('score3')
scorefxn_fa = get_fa_scorefxn()

convert3to1 = {'HIS':'H','LYS':'K','ARG':'R','ASP':'D','GLU':'E','SER':'S','THR':'T','ASN':'N','GLN':'Q','ALA':'A','VAL':'V','LEU':'L','ILE':'I','MET':'M','PHE':'F','TYR':'Y','TRP':'W','PRO':'P','GLY':'G','CYS':'C'}
convert1to3 = {'H':'HIS','K':'LYS','R':'ARG','D':'ASP','E':'GLU','S':'SER','T':'THR','N':'ASN','Q':'GLN','A':'ALA','V':'VAL','L':'LEU','I':'ILE','M':'MET','F':'PHE','Y':'TYR','W':'TRP','P':'PRO','G':'GLY','C':'CYS'}

def score_pose(pose, scorefxn):
	"""
	Utility function that scores a pose using a given scorefunction
	Params
		- pose (pose object): pose object produced by pose_from_pdb or Protein.pose
		- scorefxn (ScoreFunction object): path to native structure in PDB format
		- scorefxn (Rosetta ScoreFunction): score function, either centroid ('score3') or full-atom ('fa_standard')
	Returns
		- Score after minimization (float)
	"""
	return scorefxn(pose)

def relax(pdb, native, scorefxn=scorefxn_fa):
	"""
	Performs energy minimization using Rosetta FastRelax protocol, superimpose onto native structure, and calculate RMSD
	--------
	Params
		- pdb (str): path to input structure in PDB format
		- native (str): path to native structure in PDB format
		- scorefxn (ScoreFunction): energy function to use in scoring. Either centroid ('score3') or full-atom ('fa_standard'), default full-atom
	Returns
		- Protein object representing relaxed structure
		- RMSD between input and native (float)
		- Score after minimization (float)
	"""
	pose=pose_from_pdb(pdb)
	score = score_pose(pose, scorefxn)
	print('initial score', score)

	to_fullatom = SwitchResidueTypeSetMover('fa_standard')
	to_fullatom.apply(pose)

	relax = FastRelax() #ClassicRelax()
	relax.set_scorefxn(scorefxn)

	relax.apply(pose)
	score = score_pose(pose, scorefxn)
	print('final score', score)
	pose.dump_pdb("%s_fast_relax.pdb"% (pdb[:-4]))

	native_pose=pose_from_pdb(native)
	relax.apply(native_pose)
	native_pose.dump_pdb("%s_fast_relax.pdb"% (native[:-4]))

	rmsd = superimpose_rmsd("%s_fast_relax.pdb"% (pdb[:-4]), "%s.pdb"% (native[:-4]))
	print('RMSD to native', rmsd)

	return Protein(pose=pose), rmsd, score

def superimpose_rmsd(pdb1, pdb2):
	"""
	Superimposes coordinates from pdb1 onto pdb2 and calculates the RMSD
	--------
	Params
		- pdb1 (str): path to pdb to superimpose
		- pdb2 (str): path to pdb to superimpose onto
	Returns
		- rmsd (float): RMSD between superimposed structures
	"""
	pred_structure = pdb_parser.get_structure('predicted', pdb1)
	ref_structure = pdb_parser.get_structure('reference', pdb2)
	pred_model = pred_structure[0]
	ref_model = ref_structure[0]

	ref_atoms = []
	for ref_chain in ref_model:
		for ref_res in ref_chain:
			if not ref_res.get_resname().startswith(' '):
				ref_atoms.append(ref_res['CA'])
	pred_atoms = []
	for pred_chain in pred_model:
		for pred_res in pred_chain:
			pred_atoms.append(pred_res['CA'])

	superimposer = Bio.PDB.Superimposer()
	superimposer.set_atoms(ref_atoms, pred_atoms)
	superimposer.apply(pred_model.get_atoms())
	rmsd = superimposer.rms

	io = Bio.PDB.PDBIO()
	io.set_structure(pred_structure) 
	io.save(pdb1[:-4] + '_aligned.pdb')

	return rmsd

def rmsd(query, target):
	"""
	Calculate RMSD between query and target
	--------
	Params
		- query (ndarray): array of shape (N,D),  where N is number of points and D is dimension
		- target (ndarray): array of shape (N,D),  where N is number of points and D is dimension
	Returns
		- rmsd (float): RMSD between query and target
	"""
	N,D = query.shape
	result = 0.0
	for i in range(N):
		result += np.sum([(query[i] - target[i])**2.0 for i in range(D)])
	return np.sqrt(result/N)
