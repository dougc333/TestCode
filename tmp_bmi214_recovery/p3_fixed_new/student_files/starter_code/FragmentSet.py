import utils
import numpy as np
import os

class FragmentSet(object):
	def __init__(self, fragfile, rmsdfile):
		"""
		This class contains the fragment library for the input protein. It must do the following:
		- Read in fragment file and parse fragments at each position. Fragment files are of the form <protein>_<frag_len>mers.frag
		- Read in RMSD file containing pre-calculated RMSD to native structure for each fragment at each position.
		- Based on fragments and their corresponding RMSDs, rank fragments at each position by RMSD
		
		"""
		pass


	def get_lowRMS_fragments(self, pos, N):
		"""
		Returns the top-ranked fragments by RMSD at a defined position in the chain
		--------
		Params
			- pos (int): fragment position in chain (1-indexed)
			- N (int): number of fragments to return
		Returns
			- lowRMS_fragments (list): top N fragments at pos by RMSD. This should be a list of lists of (phi, psi) tuples. 
			  For example, a 3-mer fragment could be represented as the following: [(-60.892, 142.456), (-72.281, 128.933), (-132.337, -175.477)]
		"""
		pass





