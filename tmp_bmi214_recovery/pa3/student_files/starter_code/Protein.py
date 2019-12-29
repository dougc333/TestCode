
import numpy as np
from pyrosetta import *
from pyrosetta.rosetta import *
#init()
init(extra_options = "-mute all -constant_seed")


class Protein(object):
	def __init__(self, sequence=None, pose=None):
		"""
		Initializes Protein object from either sequence or pose.
		Initializing from sequence produces an extended (unfolded) chain, while initializing from pose is used to create a new protein with a defined structure (pose).
			- Note: this is necessary to copy an existing Protein object
		--------
		Params:
			- sequence (str or None): string containing sequence of 1-letter amino acid codes
			- pose (Pose object or None): Pose (structure), such as the Protein.pose of another Protein object
		"""
		#################################
		######   DO NOT MODIFY!!   ######
		#################################
		if sequence and pose:
			raise Exception('must give only sequence or pose, not both')
		if sequence:
			self.sequence = sequence
			self.length = len(sequence)
			self.pose = pose_from_sequence(sequence)  # PyRosetta pose object
			self.init_extended()

		elif pose:
			self.pose = Pose()
			# this is required to copy a pose. Using pose_copy = pose simply creates new pointer to same object.
			self.pose.assign(pose)
			self.sequence = pose.sequence()
			self.length = pose.total_residue()

		# switch to centroid representation for efficiency
		to_centroid = SwitchResidueTypeSetMover('centroid')
		to_centroid.apply(self.pose)
		#################################

	def init_extended(self):
		"""
		TODO: initialize protein to unfolded state by setting all torsions to very large values.
		A good starting point is to set all phi angles to -150 degrees and all psi angles to 150 degrees.
		--------
		Params:
			- TODO
		Returns:
			- TODO
		"""
		self.pose.set_phi(1,0.)
		self.pose.set_psi(1,0.)
		for idx in range(2,self.length-1):
			#space tab prpoblem here
			self.pose.set_phi(idx,-150.)
			self.pose.set_psi(idx,150.)
			#I hate you vscode
		self.pose.set_phi(self.length,0)
		self.pose.set_psi(self.length,0)
		
    
	def get_length(self):
		return self.length
	
	def get_pose(self):
		return self.pose

	def add_fragment(self,pos,kmer):
		#print("kmer:",kmer)
		for idx in range(0,len(kmer)):
			#print("Protein add_fragment pos:",pos,"kmer[idx][0]:",kmer[idx][0]," kmer[idx][1]:",kmer[idx][1])
			self.set_torsion(int(pos),float(kmer[idx][0]),float(kmer[idx][1]))

	def get_torsion(self, pos):
		"""
		TODO: get torsion angles at a defined position. You don't need to worry about omega angles (why?)
		The following reference may be useful for interacting with the Pose object: https://graylab.jhu.edu/pyrosetta/downloads/documentation/pyrosetta4_online_format/PyRosetta4_Workshop2_PyRosetta.pdf
		--------
		Params:
			- pos (int): position in chain (1-indexed)
		Returns:
			- phi (float): phi angle at position
			- psi (float): psi angle at position
		"""
		return (self.pose.phi(pos), self.pose.psi(pos))

	def set_torsion(self, pos, phi, psi):
		"""
		TODO: set torsion angles at a defined position. You don't need to worry about omega angles (why?)
		The following reference may be useful for interacting with the Pose object: https://graylab.jhu.edu/pyrosetta/downloads/documentation/pyrosetta4_online_format/PyRosetta4_Workshop2_PyRosetta.pdf
		--------
		Params:
			- pos (int): position in chain (1-indexed)
			- phi (float): phi angle at position
			- psi (float): psi angle at position
		"""
		#print(type(self.pose))
		#print(type(pos),pos,type(phi),phi,type(psi),psi)
		self.pose.set_phi(pos,phi)
		self.pose.set_psi(pos,psi)
		

	def save_pdb(self, filename):
		"""
		Saves current structure to PDB file. You do not need to modify this function.
		"""
		self.pose.dump_pdb(filename)


