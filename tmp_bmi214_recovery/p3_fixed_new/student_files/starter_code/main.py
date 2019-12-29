"""
This is the master file, which you should use to set up and run the simulations.
You may define functions or classes as necessary

For an input sequence, do the following (see project page for details):
	1. load sequence from fasta file and initialize protein into extended configuration
	2. Run a series of simulations (n=5 or 10):
		- Perform MCMC sampling with 9-mer fragments from kT=100 to kT=1 (assembly stage)
		- Perform MCMC sampling with 3-mer fragments from kT=1 to kT=0.1 (refinement stage)
		- Take best (lowest-energy) structure after refinement and perform energy minimization (see utils.relax)
		- Log energy and RMSD to native structure after minimization
	3. Visualize lowest-RMSD structure in PyMol

"""


from pyrosetta import *
from pyrosetta.rosetta import *
init(extra_options='-mute all -constant_seed')

from Protein import Protein
from FragmentSampler import MCMCSampler

import utils
import argparse
import numpy as np
import time
import os



def main():
    pass


if __name__=='__main__':
    pass

