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
		self.fragfile = fragfile
		self.rmsdfile  = rmsdfile
		self._rmsd_dict, self.max_pos = self.get_rmsd_data(self.rmsdfile)
		self._frag_data = self.get_rmsd_data(self.rmsdfile)
		self._frag_rmsd= self.join_rmsd_frag(self.rmsdfile,self.fragfile)
		self._topN = self.topN(self._frag_rmsd,3)
		self.init()

	def init(self):
		print('***AUTOSHAMER FragmentSet.init()****')


	def get_rmsd_data(self,rmsdfile):
		'''
		input: kmer rmsd file
		output: rmsd dict key=(pos,neighbor) value=rmsd
		'''
		rmsd_dict = {}
		max_pos = 0
		with open(rmsdfile,"r") as fh:
			print("********AUTOSHAMER*******")
			print("OS PATH:",os.getcwd())
			print("OS PATH DIRNAME:",os.path.dirname(os.getcwd()))
			print("OS DIR:",os.listdir(os.getcwd()))
			print("WHERE ARE YOU? 1ubqhelix_9mers.rmsd:",os.listdir(os.path.dirname(os.getcwd())))
			print("********AUTOSHAMER END****")
			lines = fh.readlines()
			for l in lines:
				pos=int(l.split()[0])
				neighbor=int(l.split()[1])
				rmsd=float(l.split()[2])
				rmsd_dict[(pos,neighbor)] = rmsd
				if pos>max_pos:
					max_pos = pos
		return rmsd_dict,max_pos

	def get_frag_data(self,fragfile):
		'''
		key=positin, value=[(pos,neibhgor,phi,psi)]
		'''
		d = {}
		with open(fragfile,"r") as fh:
			lines = fh.readlines()
			for l in lines:
			    processMe = l.strip()
			    if "position" in processMe:
			        pos = int(processMe.split()[1])
			        num_neighbors = int(processMe.split()[3])
			        d[int(pos)]=[]
			    elif(len(processMe)>1):
			        neighbor=int(processMe.split()[-1][-3:])
			        #print("pos:",pos,"neighbor:",neighbor,"phi:",float(processMe.split()[5]),"psi:",float(processMe.split()[6]))
			        d[int(pos)].append((pos,neighbor,float(processMe.split()[5]),float(processMe.split()[6])))
		return d

	def get_max_pos(self):
		return self.max_pos

	def join_rmsd_frag(self,rmsdfile,fragfile):
		rmsd_dict,_ = self.get_rmsd_data(rmsdfile)
		d = self.get_frag_data(fragfile)
		frag_rmsd={}
		for jdx in range(1,self.max_pos+1):
		    for idx in range(0,len(d[jdx])):
		        pos = d[jdx][idx][0]
		        neighbor = d[jdx][idx][1]
		        #print(d[jdx][idx])
		        if (pos,neighbor) not in frag_rmsd:
		            frag_rmsd[(pos,neighbor)]=(rmsd_dict[(pos,neighbor)],[])
		        frag_rmsd[(pos,neighbor)][1].append((d[jdx][idx][2],d[jdx][idx][3]))
		return frag_rmsd

	def topN(self,frag_rmsd, N):
		rmsd={}
		#print("self.max_pos:",self.max_pos)
		#print("frag_rmsd[(jdx,idx)]:",frag_rmsd[(1,1)])
		for jdx in range(1,self.max_pos+1):
			s = []
			for idx in range(1,201):
				s.append(frag_rmsd[(jdx,idx)])
			#print("jdx:",jdx)
			rmsd[jdx]=sorted(s, key=lambda x: x[0])[:N]
		print(rmsd[1])
		return rmsd

	def clean(self,rmsd):
		clean={}
		for idx in range(1,self.max_pos+1):
		    clean[idx] = [x[1] for x in rmsd[idx]] #clean this
		return clean

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
		#print("get_lowRMS_fragmetns:",pos,N)
		#print("self.frag_rmsd:",len(self._frag_rmsd))
		tn = self.topN(self._frag_rmsd,N)
		#print("tn:",tn)
		c = self.clean(tn)
		#print("c:",c)
		return c[pos]
		





