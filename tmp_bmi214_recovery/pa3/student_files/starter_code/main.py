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


def main(fasta,logdir,nsims, nfrags, anneal_rate):
	#can you create this in FragmentSampler init() or is that too late? first test if it already exists, if not then we can create it
	print("main logdir:",logdir)
	if not os.path.exists(logdir):
		os.makedirs(logdir)
	fh = open(os.path.join(logdir,"simulation_summary.txt"),"w")
	fh.close()
	print("********AUTOSHAMER main.py",fasta, logdir, nsims, nfrags, anneal_rate)
	mcmc = MCMCSampler(fasta,logdir,nsims,nfrags,anneal_rate)	
	mcmc.simulate()

if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--fasta', type=str,  help='fasta file')
	parser.add_argument('--logdir', type=str, default='logdir', help='logfile')
	parser.add_argument('--nsims', type=int, default=1, help='number of sims, dir for each one')
	parser.add_argument('--nfrags', type=int,  default=3, help='num of frags or topN, N')
	parser.add_argument('--anneal_rate', type=float, default=.999, help='the multiplier, not TStart or Tend')
	
	args = parser.parse_args()
	main(args.fasta, args.logdir, args.nsims, args.nfrags, args.anneal_rate)
