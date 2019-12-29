
"""

This file provides skeleton code for align.py. 

Locations with "FILL IN" in comments are where you need to add code.

Note - you do not need to follow this set up! It is just a suggestion, and may help for program design and testing.


Usage: python align.py input_file output_file
round(3e-74,3)
"""


import sys
import copy 
from pprint import pprint

#### ------ USEFUL FUNCTIONS ------- ####
def fuzzy_equals(a, b):
    """
    Checks if two floating point numbers are equivalent.
    """
    epsilon = 10**(-6) 
    return (abs(a - b) < epsilon)
    

#### ------- CLASSES ------- ####

class MatchMatrix(object):
    """
    Match matrix class stores the scores of matches in a data structure
    """
    def __init__(self,alphabet_a, alphabet_b,len_alphabet_a, len_alphabet_b):
        ### FILL IN ###
        self.matrix = [[0 for i in range(0,len_alphabet_b)] for j in range(0,len_alphabet_a)]
        self.alphabet_a=[x for x in alphabet_a] #this is the vertical part of matrix Altman convention, num_rows
        self.alphabet_b=[x for x in alphabet_b] #this is row across top of martix Altman convention, num_cols

    def set_score(self, a, b, score):
        """
        Updates or adds a score for a specified match

        Inputs:
           a = the character from sequence A
           b = the character from sequence B
           score = the score to set it for
        """
        ### FILL IN ###
        row = self.alphabet_a.index(a)
        col = self.alphabet_b.index(b)
        self.matrix[row][col] = float(score)

    def get_score(self, a, b):
        """
        Returns the score for a particular match, where a is the
        character from sequence a and b is from sequence b.

        Inputs:
           a = the character from sequence A
           b = the character from sequence B
        Returns:
           the score of that match
        """
        ### FILL IN ###
        return self.matrix[self.alphabet_a.index(a)][self.alphabet_b.index(b)]


class Node:  
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.weight = 0.
    self.M_pointer = []
    self.Ix_pointer = []
    self.Iy_pointer = []
    
class ScoreMatrix(object):
    """
    Object to store a score matrix, which generated during the alignment process. The score matrix consists of a 2-D array of
    ScoreEntries that are updated during alignment and used to output the maximum alignment.
    """

    def __init__(self, name, nrow, ncol):
        self.name = name # identifier for the score matrix - Ix, Iy, or M
        self.nrow = nrow
        self.ncol = ncol
        #this is wrong? off by one? because they start at 1 when counting len(alphabet_a)
        self.score_matrix =[[Node(i,j) for i in range(0,ncol)] for j in range(0,nrow)]
        
        # FILL IN 
        # you need to figure out a way to represent this and how to initialize
        # Hint: it may be helpful to have an object for each entry
    def M_pointer_add(self,row,col,tupl):
        self.score_matrix[row][col].M_pointer.append(tupl)
    
    def getM_pointer(self,row,col):
        return self.score_matrix[row][col].M_pointer
    
    def Ix_pointer_add(self,row,col,tupl):
        self.score_matrix[row][col].Ix_pointer.append(tupl)

    def getIx_pointer(self,row,col):
        return self.score_matrix[row][col].Ix_pointer

    def Iy_pointer_add(self,row,col,tupl):
        self.score_matrix[row][col].Iy_pointer.append(tupl)

    def getIy_pointer(self,row,col):
        return self.score_matrix[row][col].Iy_pointer

    def get_score(self, row, col):
        return self.score_matrix[row][col].weight
        
    def set_score(self, row, col, score):    
        ### FILL IN ###
        self.score_matrix[row][col].weight = float(score)
    
    def get_pointers(self, row, col):
        """
        Returns the indices of the entries that are pointed to
        This should be formatted as a list of tuples:
         ex. [(1,1), (1,0)]
        """
        ### FILL IN ###
        #needs to be flattened?
        #print("asdf",self.getM_pointer(row,col),self.getIx_pointer(row,col), self.getIy_pointer(row,col))
        return [self.getM_pointer(row,col), self.getIx_pointer(row,col), self.getIy_pointer(row,col)]

    def set_pointers(self, row, col,M_tupl, Ix_tupl, Iy_tupl): 
        ### FILL IN - this needs additional arguments ###
        ### FILL IN ###
        self.M_pointer_add(row,col,M_tupl)
        self.Ix_pointer_add(row,col,Ix_tupl)
        self.Iy_pointer_add(row,col,Iy_tupl)

    def print_scores(self):
        """
        Returns a nicely formatted string containing the scores in the score matrix. Use this for debugging!

        Example:
        M=
            0.0, 0.0, 0.0, 0.0, 0.0
            0.0, 1.0, 0.0, 0.0, 0.0
            0.0, 1.0, 1.0, 1.0, 1.0
            0.0, 0.0, 1.0, 1.0, 1.0
            0.0, 0.0, 2.0, 2.0, 1.0    
            0.0, 0.0, 1.0, 2.0, 3.0

        """
        ### FILL IN ###  
        print(self.name+" = ")
        for row in self.score_matrix:
            print(" ".join([str(x.weight) for x in row]))
    #import csv
    def write_scores(self,file_name):
        with open(file_name,'w',newline='\n') as fh:
            for row in self.score_matrix:
                fh.write(",".join([str(x.weight)[0:4] for x in row]))
                fh.write("\n")
    
    def get_max(self):
        max = -float("inf")
        tuple_loc = None
        for i in range(0,self.nrow):
            for j in range(0,self.ncol):
                if self.score_matrix[i][j].weight > max:
                    max = self.score_matrix[i][j].weight
                    tuple_loc=(i,j)
        return max,tuple_loc
    
    #for global search in last row and last col
    def get_last_column_row_max(self):
        
        max = -float("inf")
        max_tuple=(None,None)
        max_find=-float("inf")
        
        #search last col
        #print("get_last_column_row_max nrow,ncol",self.nrow,self.ncol)
        for i in range(0,self.nrow):
            #print("i,self.ncol-1",i,self.ncol-1,self.score_matrix[i][self.ncol-1].weight)
            if self.score_matrix[i][self.ncol-1].weight > max:
                max = self.score_matrix[i][self.ncol-1].weight
                #print("new max: i:",max,i)
                max_find = (i,self.ncol-1)
        #search last row
        for j in range(0,self.ncol):
            #print("nrow-1,j",self.nrow-1,j,self.score_matrix[self.nrow-1][j].weight)
            if self.score_matrix[self.nrow-1][j].weight > max:
                max = self.score_matrix[self.nrow-1][j].weight
                max_find = (self.row-1,j)
                #print("new max: j:",max)
        
        #format_tuple = (tuple_loc[1],tuple_loc[0])
        #print("get_last_column_row_max:",max,max_find)
        return max, max_find

    def print_pointers_old(self):
        """
        debugging!
        """
        for i in range(0,self.nrow):
            for j in range(0,self.ncol):
                print("i j",i,j,self.score_matrix[i][j].pointers)

    def print_pointers(self):
        #convention for printing matrix
        print("pointers:",self.name)
        for i in range(1,self.nrow):
            for j in range(1,self.ncol):
                #merge all 3 into a list to remove empty list
                #print(i,j,["M"+str(x) for x in self.getM_pointer(i,j)],
                #["Ix"+str(x) for x in self.getIx_pointer(i,j)],
                #["Iy"+str(x) for x in self.getIy_pointer(i,j)])
                print(i,j,["M"+str(x) for x in self.score_matrix[i][j].M_pointer],
                ["Ix"+str(x) for x in self.score_matrix[i][j].Ix_pointer],
                ["Iy"+str(x) for x in self.score_matrix[i][j].Iy_pointer])
                

class AlignmentParameters(object):
    """
    Object to hold a set of alignment parameters from an input file.
    """
    def __init__(self):
        # default values for variables that are filled in by reading
        # the input alignment file
        self.seq_a = ""
        self.seq_b = ""
        self.global_alignment = False
        self.dx = 0
        self.ex = 0
        self.dy = 0
        self.ey = 0    
        self.alphabet_a = "" 
        self.alphabet_b = ""
        self.len_alphabet_a = 0
        self.len_alphabet_b = 0
        self.match_matrix = MatchMatrix(self.alphabet_a, self.alphabet_b, self.len_alphabet_a, self.len_alphabet_a)
        

    def load_params_from_file(self, input_file): 
        """
        Reads the parameters from an input file and stores in the object

        Input:
           input_file = specially formatted alignment input file
        """
        #with open(input_file,"r") as fh
        #   for l in fh:
        #       lines = l.rstrip('\n')
        lines = [line.rstrip('\n') for line in open(input_file)]
        self.seq_a = lines[0] 
        self.seq_b = lines[1] 
        global_alignment = int(lines[2]) 
        if global_alignment == 0:
            self.global_alignment = True
        else:
            self.global_alignment = False
        de_list = lines[3].split()
        self.dx = float(de_list[0])
        self.ex = float(de_list[1])
        self.dy = float(de_list[2])
        self.ey = float(de_list[3]) 
        self.len_alphabet_a = int(lines[4])
        self.alphabet_a = lines[5] 
        self.len_alphabet_b = int(lines[6])
        self.alphabet_b = lines[7]
        self.match_matrix = MatchMatrix(self.alphabet_a, self.alphabet_b, self.len_alphabet_a, self.len_alphabet_b)
        for x in range(8,len(lines)):
            if(len(lines[x].strip())>0):
                parse_input = lines[x].split()
                row = parse_input[0] #row in match matrix from 1 not used for defined interface
                col = parse_input[1] # col in match matrix from 1 not used for defined interface
                firstAA = parse_input[2] 
                secondAA = parse_input[3]
                similarity = parse_input[4]
                self.match_matrix.set_score(firstAA, secondAA, similarity)

class Align(object):
    """
    Object to hold and run an alignment; running is accomplished by using "align()"
    """

    def __init__(self, input_file, output_file):
        """
        Input:
            input_file = file with the input for running an alignment
            output_file = file to write the output alignments to
        """
        self.input_file = input_file
        self.output_file = output_file
        self.align_params = AlignmentParameters()
        self.m_matrix = None
        self.ix_matrix = None
        self.iy_matrix = None
        self.score = 0.0
        self.final_path=[]
        self.start_i = None #start_pos i(row) where to start printing for traceback
        self.start_j = None #start_pos j(col) where to start printing for traceback
        #node = [[(4,5)],[],[]] becuse we need a notation for an empty tuple 
        #path=[[node1],[node2],[node3]]
        #paths = [[path],[path] = [ [[node1],[node2],[node3]], [[node1],[node2],[node3]] ]
        self.paths=[[]] #blue = node, pink=path, yellow=paths

    #we have to delay init till we load parameters in file because of align_test.py  
    def init_matrix(self):
        self.m_matrix = ScoreMatrix("M",len(self.align_params.seq_a)+1, len(self.align_params.seq_b)+1)
        self.ix_matrix = ScoreMatrix("Ix",len(self.align_params.seq_a)+1, len(self.align_params.seq_b)+1)
        self.iy_matrix = ScoreMatrix("Iy",len(self.align_params.seq_a)+1, len(self.align_params.seq_b)+1)
        
    def align(self):
        """
        Main method for running alignment.
        """

        # load the alignment parameters into the align_params object
        self.align_params.load_params_from_file(self.input_file)
        self.init_matrix()
        # populate the score matrices based on the input parameters
        self.populate_score_matrices()
        self.traceback()
        #move to main for online grading
        #self.write_output()
        
        ### FILL IN ###
    
    def populate_score_matrices(self):
        """
        Method to populate the score matrices based on the data in align_params.
        Should call update(i,j) for each entry in the score matrices
        """
        ### FILL IN ###
        #careful to use len_alphabet_a vs. len(align_params.seq_a) for align_test
        #we dont specify seqa, only size of alphabet for testing update_ix, update_m, update_iy
        for i in range(0,len(self.align_params.seq_a)+1):
            for j in range(0,len(self.align_params.seq_b)+1):
                self.update(i,j)   
        #self.debug_print()
        #self.m_matrix.write_scores("m.csv")
        #self.ix_matrix.write_scores("ix.csv")
        #self.iy_matrix.write_scores("iy.csv")       
    
    def debug_print(self):           
        print("----------------")
        self.m_matrix.print_scores()
        print("----------------")
        self.ix_matrix.print_scores()
        #print("maxIx:",max([max(x)  for x in self.ix_matrix.score_matrix]))
        print("----------------")
        self.iy_matrix.print_scores()
        print("----------------")
        self.m_matrix.print_pointers()
        self.ix_matrix.print_pointers()
        self.iy_matrix.print_pointers()
        print("-------------------------")
    
    def update(self, row, col):
        """
        Method to update the matrices at a given row and column index.

        Input:
           row = the row index to update
           col = the column index to update
        """
        self.update_m(row, col)
        self.update_ix(row, col)
        self.update_iy(row, col)
        
    def update_m(self, row, col):
        ### FILL IN ###
        if (row==0 and col==0):
            self.m_matrix.set_score(row,col,0.0)
        elif(row!=0 and col!=0):
            M =  round(self.m_matrix.get_score(row-1,col-1) + (self.align_params.match_matrix.get_score(self.align_params.seq_a[row-1],self.align_params.seq_b[col-1])),3)
            Ix = round(self.ix_matrix.get_score(row-1,col-1) + (self.align_params.match_matrix.get_score(self.align_params.seq_a[row-1],self.align_params.seq_b[col-1])),3)
            Iy =  round(self.iy_matrix.get_score(row-1,col-1) + (self.align_params.match_matrix.get_score(self.align_params.seq_a[row-1],self.align_params.seq_b[col-1])),3)
            maxM = max(M,Ix,Iy)
            #print(self.align_params.seq_a[row],self.align_params.seq_a[row-1])
            #print()
            #print("m(row-1,col-1):",self.m_matrix.get_score(row-1,col-1),,self.align_params.seq_b[col-1])
            #self.align_params.match_matrix.get_score(self.align_params.seq_a[row-1])
            #print("update_m:",row,col,M,Ix,Iy,maxM)
            self.m_matrix.set_score(row,col, maxM)
            #local
            if self.align_params.global_alignment==False:
                #print("*********M pointer M local")
                if self.m_matrix.get_score(row,col) < 0.:
                    self.m_matrix.set_score(row,col,0.) 
            #set pointers       
            if fuzzy_equals(M,maxM):
                #print("update_m m_M pointer update:",row-1,col-1)
                self.m_matrix.M_pointer_add(row,col,(row-1,col-1))
            if fuzzy_equals(Ix,maxM):
                #print("update_m m_Ix pointer update:",row-1,col-1)
                self.m_matrix.Ix_pointer_add(row,col,(row-1,col-1))
            if fuzzy_equals(Iy,maxM):
                #print("update_m m_Iy pointer update:",row-1,col-1)
                self.m_matrix.Iy_pointer_add(row,col,(row-1,col-1))
                
                
                    
    def update_ix(self, row, col):
        if (row==0 and col==0):
            self.ix_matrix.set_score(row,col,0.0)
        elif(row!=0 and col!=0):
            M = round(self.m_matrix.get_score(row-1,col) - self.align_params.dy,3)
            Ix = round(self.ix_matrix.get_score(row-1,col) - self.align_params.ey,3)
            maxIx = max(M,Ix)
            #print("update_ix:",row,col,M,Ix,maxIx)
            self.ix_matrix.set_score(row,col, maxIx)
            #local 
            if self.align_params.global_alignment==False:
                #print("*********Ix pointer Ix local")
                if self.ix_matrix.get_score(row,col) < 0.:
                    self.ix_matrix.set_score(row,col,0.) 
            #set pointers
            if fuzzy_equals(M,maxIx):
                #print("update_ix ix_M pointer update:",row-1,col)
                self.ix_matrix.M_pointer_add(row,col,(row-1,col))
            if fuzzy_equals(Ix,maxIx):
                #print("update_ix ix_Ix pointer update:",row-1,col)
                self.ix_matrix.Ix_pointer_add(row,col,(row-1,col))

    def update_iy(self, row, col):        
        if (row==0 and col==0):
            self.iy_matrix.set_score(row,col,0.0)
        elif(row!=0 and col!=0):
            M = round(self.m_matrix.get_score(row,col-1) - self.align_params.dx,3)
            Iy = round(self.iy_matrix.get_score(row,col-1) - self.align_params.ex,3)
            maxIy = max(M,Iy)
            #print("update_iy:",row,col,M,Iy,maxIy)
            self.iy_matrix.set_score(row,col, maxIy)
            #local
            if self.align_params.global_alignment==False:
                #print("*********Iy pointer Iy local")
                if self.iy_matrix.get_score(row,col) < 0.:
                    self.iy_matrix.set_score(row,col,0.) 
            #set pointers
            if fuzzy_equals(M,maxIy):
                #print("update_iy iy_M pointer update:",row,col-1)
                self.iy_matrix.M_pointer_add(row,col,(row,col-1))
            if fuzzy_equals(Iy,maxIy):
                #print("update_iy iy_Iy pointer update:",row,col-1)
                self.iy_matrix.Iy_pointer_add(row,col,(row,col-1))   

    def find_traceback_start(self):
        """
        Finds the location to start the traceback..
        Think carefully about how to set this up for local 

        Returns:
            (max_val, max_loc) where max_val is the best score
            max_loc is a list [] containing tuples with the (i,j) location(s) to start the traceback
             (ex. [(1,2), (3,4)])
        """
        ### FILL IN ###
        #very tricky the max for alignment.example2 is not at teh last square. 
        #did not know this was a case. not clear. Assime he means on teh last row
        #and column only since we are starting there
        if self.align_params.global_alignment==True:
            #print("global M find max")
            M_score,M_loc=self.m_matrix.get_last_column_row_max()
            #print("Ix find max")
            Ix_score,Ix_loc=self.m_matrix.get_last_column_row_max()
            #print("Iy find max")
            Iy_score,Iy_loc=self.m_matrix.get_last_column_row_max()
            self.score = round(max(M_score,Ix_score,Iy_score),2)


            #print("*****global M score:",M_score,M_loc)
            #print("*****global Ix score:",Ix_score,Ix_loc)
            #print("*****global Iy score:",Iy_score,Iy_loc)
            #print("*****self.score:",self.score)
            #start position can be from Ix,Iy,M location. Meed to modify to start there 
            # Need test case to start in Ix, Iy        
            if max(M_score,Ix_score,Iy_score)==M_score:
                return M_loc
            elif max(M_score,Ix_score,Iy_score)==Ix_score:
                return Ix_loc
            elif max(M_score,Ix_score,Iy_score):
                return Iy_loc
        else:
            #print("start traceback local")
            maxM,M_loc = self.m_matrix.get_max()
            maxIx,Ix_loc = self.ix_matrix.get_max()
            maxIy,Iy_loc = self.iy_matrix.get_max()
            
            max_all= max(maxM, maxIx, maxIy)
            #print("local start maxM,maxIx,maxIy:",maxM,maxIx,maxIy)
            self.score = max_all
            return M_loc

    def add_one(self,last_node, node):
        #print("add_one last_node:",last_node)
        #print("add_one node",node)
        for idx in range(0,len(self.paths)):
            #print("add_one testing last node:",self.paths[idx][-1])
            if (self.paths[idx][-1]==last_node):
                #print("adding!!!!")
                self.paths[idx].append(node)
            
    def branch(self,last_node,node1,node2):
        #print("branch node1:",node1,"branch node2:",node2)
        for idx in range(0,len(self.paths)):
            #print("branch testing last node:",self.paths[idx][-1])
            if (self.paths[idx][-1]==last_node):
                #print("adding!!!!")
                dup = copy.deepcopy(self.paths[idx]) #copies path
                dup.append(node1)
                self.paths[idx].append(node2)
                self.paths.append(dup)

    def branch2(self,last_node,node1,node2,node3):
        '''
        termination of path, add the final node with M,Ix,Iy set. This is an invalid
        node because it requires you to be in all 3 matrices which is physically
        impossible but this is defintion of termination condition on the graph.  
        '''
        
        #print("branch2 last_node:",last_node,"branch2 node1:",node1,"branch2 node2:",node2,"branch2 node3:",node3)
        remove_index=0
        for idx in range(0,len(self.paths)):
           # print("branch2 paths:",self.paths[idx])
            #print(len(self.paths),idx)
            if (self.paths[idx][-1]==last_node):
                remove_index=idx
                #print("found!!!",idx)
                #remove this path from self.paths to print out
        #print("remove_index:",remove_index)
        self.paths[remove_index].append([node1[0],node2[1],node3[2]])
        self.final_path.append(self.paths[remove_index])
        self.paths.remove(self.paths[remove_index])


    def addM(self,tupl):
        node = [[tupl],[],[]]
        for x in range(0,len(self.paths)):
            self.paths[x].append(node)
    def addIx(self,tupl):
        node = [[],[tupl],[]]
        for x in range(0,len(self.paths)):
            self.paths.append(node)
    def addIy(self,tupl):
        node = [[],[],[tupl]]
        for x in range(0,len(self.paths)):
            self.paths.append(node)
    def last_nodes(self):
        '''
        returns last node tuples for next iteration in score matrix till end of path
        '''
        nodes=[]
        for idx in range(0,len(self.paths)):
            #print("path:",self.paths[idx])
            last_node =self.paths[idx][-1]
            #print("last_node:",last_node)
            nodes.append(last_node)
        return nodes

    def print_paths(self):
        #print("num_paths:",len(self.paths))
        for idx in range(0,len(self.paths)):
            print(self.paths[idx])
    
    def print_final(self):
        #print("num_paths:",len(self.final_path))
        for idx in range(0,len(self.final_path)):
            print(self.final_path[idx])

    def traceback(self): ### FILL IN additional arguments ###
        """
        Performs a traceback.
        Hint: include a way to printing the traceback path. This will be helpful for debugging!
           ex. M(5,4)->Iy(4,3)->M(4,2)->Ix(3,1)->Ix(2,1)->M(1,1)->M(0,0)
        """
        ### FILL IN ###
        start = self.find_traceback_start()
        #print("traceback_start:",start)
        i = start[0]
        j = start[1]
        self.start_i = i
        self.start_j = j

        #print("self.paths before adding start:",self.paths)
        self.addM(start)
        #print("self.paths after adding start node",self.paths)
        #each node [[path] [path] [path]]=[[M] [Ix] [Iy]]
        #print( "m_M_pointer",self.m_matrix.getM_pointer(i,j),"m_Ix_pointer:",self.m_matrix.getIx_pointer(i,j),"m_Iy_pointer:",self.m_matrix.getIy_pointer(i,j))
        #print("getpointers:",self.m_matrix.get_pointers(i,j))

        num_iter=0
        while(len(self.paths)>0 ):
            #print("start loop self.path:")
            #self.print_paths()
            last_nodes = self.last_nodes()
            #print("num_iter:",num_iter,"i j",i,j,"last_nodes:",last_nodes)
            
            for n in last_nodes:
                #use n[0],n[1],n[2] to figure out if tis is M,Ix or Iy
                #print("last node:",n,"len n[0],n[1],n[2]",len(n[0]),len(n[1]),len(n[2]))
                l=[]
                if len(n[0])==1:
                    #print("lookup M")
                    i,j = n[0][0]
                    diag = [self.m_matrix.get_pointers(i,j)[0],[],[]] #M
                    top = [[],self.m_matrix.get_pointers(i,j)[1],[]] #ix
                    left = [[],[],self.m_matrix.get_pointers(i,j)[2]] #iy
                    l.extend(diag)
                    l.extend(top)
                    l.extend(left)
                elif(len(n[1])==1):
                    #print("lookup Ix")
                    i,j = n[1][0]
                    diag = [self.ix_matrix.get_pointers(i,j)[0],[],[]] #M
                    top = [[],self.ix_matrix.get_pointers(i,j)[1],[]] #ix
                    #print("lookup Ix diag:",diag," top:",top)
                    l.extend(diag)
                    l.extend(top)
                elif(len(n[2])==1):
                    #print("lookup Iy")
                    i,j = n[2][0]
                    diag = [self.iy_matrix.get_pointers(i,j)[0],[],[]] #M
                    left = [[],[],self.iy_matrix.get_pointers(i,j)[2]] #iy
                    l.extend(diag)
                    l.extend(left)
                    #print("lookupIy diag:",diag," left:",left)
                else:
                    print("*******should not see this*********")
                flatten = [x for x in l if len(x)>0]
                num_diag = [len(x) for x in diag]
                num_top = [len(x) for x in top]
                num_left = [len(x) for x in left]
                #print("diag:",diag," top:",top," left",left," flatten:",flatten,"len(flatten):",len(flatten))
                #print("num_diag,num_top,num_left",num_diag,num_top,num_left)            
                #if more than one have to branch
                if (len(flatten))==0:
                    #print("len(flatten) =0")
                    #print("error flatten 0")
                    sys.exit()
                elif(len(flatten))==1:
                    #append single flatten list and append once
                    #print("len(flatten)=1")
                    single_node = []
                    if (1 in num_diag):
                        single_node.append(diag)
                    if (1 in num_top):
                        single_node.append(top)
                    if (1 in num_left):
                        single_node.append(left)
                    self.add_one(n,single_node[0])
                    #print("after 1 add path:")
                    #self.print_paths()
                elif (len(flatten)==2 ):
                    #branch multiple entries need to branch and add separate tuple to each one. flatten, branch
                    #to number of tuples and remove tuple and add to path list
                    #print("branch len(flatten)==2")
                    two_nodes=[]
                    if (1 in num_diag):
                        two_nodes.append(diag)
                    if (1 in num_top):
                        two_nodes.append(top)
                    if (1 in num_left):
                        two_nodes.append(left)
                    #print("len==2 two_nodes:",two_nodes)
                    self.branch(n,two_nodes[0],two_nodes[1])
                    #print("after branch self.paths:")
                    #self.print_paths()
                elif(len(flatten)==3):
                    #termination condition
                    node=[]
                    if (1 in num_diag):
                        node.append(diag)
                    if (1 in num_top):
                        node.append(top)
                    if (1 in num_left):
                        node.append(left)
                    #print("before branch2 self.paths:")
                    self.branch2(n,diag,top,left)
                    #print("after branch2 self.paths:")
                    #self.print_paths()
                    #print("after branch2 self.final_paths")
                    #self.print_final()
                else:
                    print("should not see this if len flatten - tie")
            num_iter+=1
            #remove complete paths
            #self.remove_paths()
        #print("after while loop self.paths:",num_iter)

    def write_output(self):
        #self.final_paths 
        #offset to start at start position minus index from end for both A and B strings
        #print("write output final paths")
        #print("the start position is wrong")
        #print(len(self.align_params.seq_a),len(self.align_params.seq_b))
        #print("self.start_i:",self.start_i," self.start_j:",self.start_j,"diff self.nrow-self.start_i:",len(self.align_params.seq_a)-self.start_i," self.ncol-self.start_j:",len(self.align_params.seq_b)-self.start_j)
        #self.print_final()
        #print("============")
        fh = open(self.output_file,"w")
        fh.write(str(self.score))
        fh.write("\n")
        fh.write("\n")
        for idx in range(0,len(self.final_path)):
            firstString=[]
            secondString=[]
            first_idx=len(self.align_params.seq_a)-self.start_i #this is wrong
            second_idx=len(self.align_params.seq_b)-self.start_j #this is wrong
            #print(self.align_params.seq_a,self.align_params.seq_b)
            #print("idx:",idx," path:",self.final_path[idx])
            
            for node_idx in range(0,len(self.final_path[idx])-1):
                node = self.final_path[idx][node_idx]
                #print("node_idx:",node_idx,"node:",node)
                #print("first_idx:",first_idx," second_idx:",second_idx)
                if (len(node[0])==1):
                    #M
                    #print("M firstString:",self.align_params.seq_a[-(1+first_idx)]," secondString:",self.align_params.seq_b[-(1+second_idx)])
                    firstString.append(self.align_params.seq_a[-(1+first_idx)])
                    secondString.append(self.align_params.seq_b[-(1+second_idx)])
                    first_idx +=1
                    second_idx +=1
                elif(len(node[1])==1):
                    #Ix 
                    #print("Ix firstString:",self.align_params.seq_a[-(1+first_idx)]," secondString: _",)
                    firstString.append(self.align_params.seq_a[-(1+first_idx)])
                    secondString.append('_')
                    first_idx +=1
                elif(len(node[2])==1):
                    #Iy
                    #print("Iy firstString: _ secondString:",self.align_params.seq_b[-(1+second_idx)])
                    firstString.append('_')
                    secondString.append(self.align_params.seq_b[-(1+second_idx)])
                    second_idx +=1
                elif(len(node[0]) and len(node[1]) and len(node[2])):
                    #termination not guaranteed
                    #print("3 node termination")
                    first_idx=0
                    second_idx=0
                    firstString=[]
                    secondString=[]
                else:
                    #other termination
                    print("else termination missing condition")
                #print("final string")
                str1 = ("".join (x for x in firstString))
                str2 = ("".join (x for x in secondString))
                str2_rev = str2[::-1]  
                str1_rev = str1[::-1]
                #print(("".join (x for x in firstString)),("".join (x for x in secondString)))
                #print("----------")
            #print("rev:",str1_rev,str2_rev)
            fh.write(str1_rev)
            fh.write("\n")
            fh.write(str2_rev)
            fh.write("\n")
            fh.write("\n")
            #print("----------")
         
            #print("end of path")
            #print("/n")
            
        first_idx=0
        second_idx=0
        firstString=[]
        secondString=[]

        fh.close()
        
def main():
    # check that the file is being properly used
    if (len(sys.argv) !=3):
        print("Please specify an input file and an output file as args.")
        return
        
    # input variables
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # create an align object and run
    align = Align(input_file, output_file)
    align.align()
    align.write_output()    
    

if __name__=="__main__":
    main()
