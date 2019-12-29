"""
This file contains the main fragment sampling class, which performs a Monte Carlo simulated annealing procedure to fold a protein.
"""

from pyrosetta import *
from pyrosetta.rosetta import *
from pyrosetta.rosetta.core.scoring import *
init(extra_options='-mute all  -constant_seed')

import numpy as np
import utils
from Protein import Protein
from FragmentSet import FragmentSet

import os
import random




class MCMCSampler(object):
    def __init__(self):
        """
        TO DO: initialize necessary variables
        The score function is given to you (Rosetta centroid score function)
        """
        self.scorefxn = create_score_function('score3')



    def compute_energy(self, protein):
        """
        TO DO
        Compute energy of protein.
        Hint: look at utils.py
        --------
        Params:
            - protein (Protein object): protein to score
        Return:
            - energy of conformation (float)
        """        
        pass

    def perturb_fragment(self): # you may want to add more arguments
        """
        TO DO
        Sample from possible fragments for a position, and replace torsion angles of that fragment in the protein.
        ---------
        Params:
            - TO DO
        Returns:
            - TO DO
        """
        pass


    def metropolis_accept(self): # you may want to add more arguments
        """
        TO DO
        Calculate probability of accepting or rejecting move based on Metropolis criterion.
        --------
        Params:
            - TO DO
        Returns:
            - TO DO
        """
        pass

    def anneal_temp(self):
        """
        TO DO
        Anneal temperature using exponential annealing schedule. Consider kT to be a single variable (i.e. ignore Boltzmann constant)
        --------
        Params:
            - TO DO
        Returns:
            - TO DO
        """
        pass

    def step(self):
        """
        TO DO
        Take a single MCMC step. Each step should do the following:
        1. sample position in chain
            - Note: think about positions you can sample a k-mer fragment from. 
              For example, you cannot sample from position 1 because there is no phi angle
        2. sample fragment at that position and replace torsions in a *copied version* of the protein
        3. measure energy after replacing fragment
        4. accept or reject based on Metropolis criterion
            - if accept: incorporate proposed insertion and anneal temperature
            - if reject: sample new fragment (go to step 3)
        """
        pass


    def simulate(self):
        """
        TO DO
        Run full MCMC simulation from start_temp to end_temp. 
        Be sure to save the best (lowest-energy) structure, so you can access it after.
        It is also a good idea to track certain variables during the simulation (temp, energy, and more).
        -------- 
        Params:
            - TO DO
        Returns:
            - TO DO
        """
        pass





    



