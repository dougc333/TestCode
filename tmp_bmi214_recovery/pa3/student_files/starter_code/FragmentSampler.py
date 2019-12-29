"""
This file contains the main fragment sampling class, which performs a Monte Carlo simulated annealing procedure to fold a protein.
"""
import numpy as np
from pyrosetta import *
from pyrosetta.rosetta import *
from pyrosetta.rosetta.core.scoring import *
init(extra_options='-mute all  -constant_seed')

import numpy as np
from utils import *
from Protein import Protein
from FragmentSet import FragmentSet

import os
import random


class MCMCSampler(object):
    def __init__(self,fasta,logdir,nsims,nfrags,anneal_rate):
        """
        TO DO: initialize necessary variables
        The score function is given to you (Rosetta centroid score function)
        """
        self.os_dir = os.path.dirname(fasta)
        self.scorefxn = create_score_function('score3')
        self.fasta = fasta
        self.required_files_dir = None
        self.logdir = logdir
        self.nsims=nsims
        self.nfrags=nfrags
        self.anneal_rate = anneal_rate
        self.log_file_autograder = "simulation_summary.txt"
        self.kTstart_3 = 1
        self.kTend_3 = .1
        self.kTstart_9 = 100
        self.kTend_9 = 1
        self.anneal_rate=anneal_rate
        self.filename = self.fasta.split('/')[-1].split('.')[0]
        self.fragfile_9mers = os.path.join(self.os_dir,self.filename+"_9mers.frag")
        self.rmsdfile_9mers = os.path.join(self.os_dir,self.filename+"_9mers.rmsd")
        self.fragfile_3mers = os.path.join(self.os_dir,self.filename+"_3mers.frag")
        self.rmsdfile_3mers = os.path.join(self.os_dir,self.filename+"_3mers.rmsd")
        self.fragset9 = FragmentSet( self.fragfile_9mers,self.rmsdfile_9mers )
        self.fragset3 = FragmentSet( self.fragfile_3mers,self.rmsdfile_3mers )
        self.last_protein = None

    def make_decoy(self,current_protein,fraglist,pos):
        #print("make_decoy adding fragment to pos:",pos)
        decoy = Protein(pose= current_protein.get_pose())
        decoy.add_fragment(pos,fraglist)
        return decoy

    def clean_topN(self,list_with_position_rmsd):
        clean_me = []
        for idx in range(0,len(list_with_position_rmsd)):
            clean_me.append(list_with_position_rmsd[idx][2])
        return clean_me

    def fastA(self,fastA_file):
        '''
        input: fastA file name
        output: sequence in second line of fastA file
        '''
        with open(fastA_file,"r") as fh:
            lines = fh.readlines()
        #is this a relative or abs path they use? 
        print("***AUTOSHAMER*** FragmentSampler fastA**** lines[0].strip",lines[0].strip())
        return lines[1].strip()

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
        print("***AUTOSHAMER perturb fragment")

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
        print("***AUTOSHAMER anneal_temp")

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
        print("****AUTOSHAMER step*****")

    def metropolis_accept(self,kT,deltaE): # you may want to add more arguments
        """
        Params:
            kT, deltaE
        Returns:
            - probability which is compared to uniform distribution
        """
        #print("metropolis kT:",kT," deltaE:",deltaE)
        if deltaE > 0:
            prob=np.exp(-deltaE/kT)
            #print("metropolis accept prob:",prob)
            return prob
        elif deltaE<=0: 
            return 1.
        else:
            #print("metropolis accept should not see this")
            sys.exit()
         
    def single_step(self,current_protein,sample,topN,idx,kT):
        '''
        input:current_protein adding fragemnts to
        sample: position of sequence adding frag
        clean: list of 3 fragments
        idx: which of 3 fragments to add, index into clean
        kT: annealing temp for metropolis
        '''
        
        #print("single_step sample:",sample)
        accepted = []
        #replace and see if metropolis met. if yes, store in list, if not list is empty
        decoy_protein = self.make_decoy(current_protein,topN[idx],int(sample))
        #print(" decoy_protein:",decoy_protein)
        energy_before = self.scorefxn(current_protein.get_pose())
        energy_after = self.scorefxn(decoy_protein.get_pose())
        deltaE = energy_after-energy_before
        #print("energy_after:",energy_after," energy_before:",energy_before,"deltaE,",deltaE,"kT:",kT)
        prob = self.metropolis_accept(kT,deltaE)
        u = np.random.random()
        #print("prob metropolis:",prob, "u:",u)
        if u < prob:         
            #accept make current_Pose = decoy
            #print("metropolis single_step accepted adding to accepted list")
            accepted.append(decoy_protein)
        #this allows me more adjustment on controlling retries. higher means more search space
        #if prob >=0.9: 
        #    accepted.append(decoy_protein)
        #print("single_step accepted length:",len(accepted))
        return accepted
    
    def try_Pos(self,topN,sample,current_protein,kT):
        #print("topN",topN)
        tryMe = [x for x in range(0,3)]
        #print("try_Pos tryMe:",tryMe)
        #while loop keep trying all 3 till find accepted protein or none are accepted
        accepted=[]
        while len(tryMe)>0 and len(accepted)==0:
            #print("tryMe:",tryMe)
            if len(tryMe)>1:
                idx = tryMe[np.random.randint(0, len(tryMe))]
            else:
                idx = tryMe[0]
            #print("try_Pos idx:",idx)
            tryMe.remove(idx)
            #print("tryMe after removing idx:",tryMe,"try_Pos kT",kT,"try_Pos sample:",sample," tryPos clean:",topN," tryPos idx:",idx)
            accepted.extend(self.single_step(current_protein,sample,topN,idx,kT))
            #print("try_Pos len(accepted) after single_step:",len(accepted))
            if len(accepted)==1:
                #print("tryPos len(accepted):",len(accepted))
                decoy_protein = accepted[0]
                return decoy_protein
        #print("tryPos returning None!! all 3 tried")
        return None

    def sim_one(self,N,n,k,current_protein,original_protein,fh):
        
        if k==3:
            kT=self.kTstart_3 
            kTend = self.kTend_3
            
        elif k==9:
            kT=self.kTstart_9 
            kTend = self.kTend_9
            
        min_E= self.scorefxn(original_protein.get_pose())
        min_protein=None
        num_iter = 0
        while kT > kTend:
            #print("************kT:",kT)
            sample = np.random.randint(2, n-k+1)
            if k==3:
                #print("sample",sample,"N:",N)
                topN = self.fragset3.get_lowRMS_fragments(sample,N)
            elif k==9:
                topN = self.fragset9.get_lowRMS_fragments(sample,N)
            #print("kT sample:",sample)
            decoy_protein = self.try_Pos(topN,sample,current_protein,kT)
            if decoy_protein!=None:
                fh.write(str(num_iter)+"\t"+str(kT)+"\t"+str(self.scorefxn(decoy_protein.get_pose()))+"\n")
                kT = kT*self.anneal_rate
                current_protein = decoy_protein
                if self.scorefxn(decoy_protein.get_pose()) < min_E:
                    min_E = self.scorefxn(decoy_protein.get_pose())
                    #print("new minE:",min_E)
                    min_protein = decoy_protein
            elif(decoy_protein==None):
                #print("decoy protein not found sample:",sample)
                fh.write(str(num_iter)+"\t"+str(kT)+"\t"+str(self.scorefxn(self.last_protein.get_pose()))+"\n")
            else:
                print("should not see this")
            num_iter+=1
        
        #print("end 9mer energy:", self.scorefxn(decoy_protein.get_pose()))  
        #print("RMSD:",rosetta.core.scoring.CA_rmsd(original_protein.get_pose(), decoy_protein.get_pose()))
        #print("min_E:",min_E)
        #min_protein.save_pdb("minE_9mer.pdb")
        return min_protein
        

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
        print("******AUTOSHAMER simulate()")

        #parent_logdir = "log"+self.filename
        #print("parent_logdir:",parent_logdir)
        #os.makedirs(parent_logdir)
        #fh_summary = open(os.path.join(parent_logdir,"simulation_summary.txt"),"w")
        fh_summary = open(os.path.join(self.logdir,"simulation_summary.txt"),"a+")
        for idx in range(1,self.nsims+1):
            print("***AUTOSHAMER running sim:",idx)
            #self.sim_num = idx
            #sim_logdir = "sim"+str(idx)
            #path = os.path.join(parent_logdir, sim_logdir)
            #os.makedirs(path) 
            #fh = open(os.path.join(path,"sim"+str(idx)+"log.txt"),"w")
            fh = open("sim"+str(idx)+"log.txt","w")
            seq = self.fastA( self.fasta)
            print(seq)
            #from protein randomly pick an insert position from 2,n-k-1 and add a fragment at a time
            current_protein = Protein(sequence=seq)
            original_protein = Protein(sequence=seq)

            n=len(seq) #or protein.get_length()
            k=9
            min_protein=None

            min_protein=self.sim_one(self.nfrags,n,k,current_protein,original_protein,fh)
            self.last_protein = min_protein
            min_protein.save_pdb("minE_9mer.pdb")
            #3mre
            k=3
            minprotein_3 = self.sim_one(self.nfrags,n,k,min_protein,original_protein,fh)
            self.last_protein = min_protein
            #minprotein_3.save_pdb(os.path.join(path,"best.pdb"))
            #protein, rmsd, score = relax(os.path.join(path,"best.pdb"),os.path.join("../starter_data",self.filename+".pdb"))
            minprotein_3.save_pdb(os.path.join("best"+str(idx)+".pdb"))

            print("*******AUTOSHAMER FragmentSampler simulate:****** logdir:",self.logdir," self.os_dir:",self.os_dir)
            protein, rmsd, score = relax("best"+str(idx)+".pdb",os.path.join(self.os_dir,self.filename+".pdb"))
            
            #print("rmsd:",rmsd," score:",score)
            #protein.save_pdb(os.path.join(path,"best_fast_relax_aligned.pdb"))
            protein.save_pdb("best"+str(idx)+"_fast_relax_aligned.pdb")
            
            print("idx:",idx," score:",score, " rmsd:",rmsd)
            fh_summary.write(str(idx)+"\t"+str(score)+"\t"+str(rmsd)+"\n")
            fh.close()
        fh_summary.close()

    



