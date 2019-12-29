
"""

This file provides skeleton code for align.py. 

Locations with "FILL IN" in comments are where you need to add code.

Note - you do not need to follow this set up! It is just a suggestion, and may help for program design and testing.


Usage: python align.py input_file output_file

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
    self.east=None
    self.se=None
    self.south=None
    self.weight = 0.
    self.M_pointer = []
    self.Ix_pointer = []
    self.Iy_pointer = []
    self.pointers = []

  def set_weights(self,east, se, south):
    self.east = east
    self.se = se
    self.south = south

  def node_print():
    print("node_print:",self.x, self.y, self.east, self.se, self.south. self.weight)
    print("pointers:",pointers)


class ScoreMatrix(object):
    """
    Object to store a score matrix, which generated during the alignment process. The score matrix consists of a 2-D array of
    ScoreEntries that are updated during alignment and used to output the maximum alignment.
    """

    def __init__(self, name, nrow, ncol):
        self.name = name # identifier for the score matrix - Ix, Iy, or M
        self.nrow = nrow
        self.ncol = ncol
        self.score_matrix =[[Node(i,j) for i in range(0,ncol)] for j in range(0,nrow)]
        self.pointer_list = [] #for traceback path only not for forward pointer storage!
        
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
        return self.score_matrix[row][col].Iy_pointer

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
        return [self.getM_pointer(row,col), self.getIx_pointer(row,col), self.getIy_pointer(row,col)]

    def set_pointers(self, row, col,M_tupl, Ix_tupl, Iy_tupl): ### FILL IN - this needs additional arguments ###
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
        #add node property printout
        #for i in range(0,self.nrow):
        #    for j in range(0,self.ncol):
        #        print("i j",i,j,self.score_matrix[i][j].weight)
         
        print(self.name+" = ")
        for row in self.score_matrix:
            print(" ".join([str(x.weight) for x in row]))

    
    def print_pointers_old(self):
        """
        Returns a nicely formatted string containing the pointers for each entry in the score matrix. Use this for debugging!
        """
        for i in range(0,self.nrow):
            for j in range(0,self.ncol):
                print("i j",i,j,self.score_matrix[i][j].pointers)

    def print_pointers(self):
        for i in range(1,self.nrow):
            for j in range(1,self.ncol):
                #merge all 3 into a list to remove empty list
                print(i,j,["M"+str(x) for x in self.score_matrix[i][j].M_pointer],["Ix"+str(x) for x in self.score_matrix[i][j].Ix_pointer],["Iy"+str(x) for x in self.score_matrix[i][j].Iy_pointer])
                
                

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
        #print("num_lines:",len(lines))
        self.match_matrix = MatchMatrix(self.alphabet_a, self.alphabet_b, self.len_alphabet_a, self.len_alphabet_b)
        for x in range(8,len(lines)):
            #print(lines[x])
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
        self.m_matrix=None
        self.ix_matrix=None
        self.iy_matrix=None

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
        #self.traceback()
        #self.write_output()
        # perform a traceback and write the output to an output file
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
                print("i j:",i,j)
                if (i==0 or j==0):
                    self.m_matrix.set_score(i,j,0.0)
                    self.ix_matrix.set_score(i,j,0.0)
                    self.iy_matrix.set_score(i,j,0.0)
                elif(i!=0 and j!=0):
                    print("i j",i,j,"seqa:",self.align_params.seq_a, "seqb:",self.align_params.seq_b)
                    print("seq_a[i-1]",self.align_params.seq_a[i-1])
                    print("seq_b[j-1]",self.align_params.seq_b[j-1])
                    print(self.align_params.match_matrix.get_score(self.align_params.seq_a[i-1],self.align_params.seq_b[j-1]))
                    
                    
                    firstM =  self.m_matrix.get_score(i-1,j-1) + (self.align_params.match_matrix.get_score(self.align_params.seq_a[i-1],self.align_params.seq_b[j-1]))
                    secondM = self.ix_matrix.get_score(i-1,j-1) + (self.align_params.match_matrix.get_score(self.align_params.seq_a[i-1],self.align_params.seq_b[j-1]))
                    thirdM =  self.iy_matrix.get_score(i-1,j-1) + (self.align_params.match_matrix.get_score(self.align_params.seq_a[i-1],self.align_params.seq_b[j-1]))
                    maxM = max(firstM,secondM,thirdM)
                    self.m_matrix.set_score(i,j, maxM)
                    if firstM==maxM:
                        self.m_matrix.M_pointer_add(i,j,(i-1,j-1))
                    if(secondM==maxM):
                        self.m_matrix.Ix_pointer_add(i,j,(i-1,j-1))
                    if(thirdM==maxM):
                        self.m_matrix.Iy_pointer_add(i,j,(i-1,j-1))

                    firstIx = self.m_matrix.get_score(i-1,j) - self.align_params.dy
                    secondIx = self.ix_matrix.get_score(i-1,j) - self.align_params.ey
                    maxIx = max(firstIx,secondIx)
                    self.ix_matrix.set_score(i,j, maxIx)
                    
                    if firstIx == maxIx:
                        self.m_matrix.M_pointer_add(i,j,(i-1,j))
                    if secondIx == maxIx:
                        self.m_matrix.Iy_pointer_add(i,j,(i-1,j))

                    firstIy = self.m_matrix.get_score(i,j-1) - self.align_params.dx
                    secondIy = self.iy_matrix.get_score(i,j-1) - self.align_params.ex
                    maxIy = max(firstIy,secondIy)
                    self.iy_matrix.set_score(i,j, maxIy)
                    if firstIy == maxIy:
                        self.m_matrix.M_pointer_add(i,j,(i,j-1))
                    if secondIy == maxIy:
                        self.m_matrix.Iy_pointer_add(i,j,(i,j-1))
                else:
                    print("should not see this")
        print("----------------")
        self.m_matrix.print_scores()
        print("----------------")
        self.ix_matrix.print_scores()
        #print("maxIx:",max([max(x)  for x in self.ix_matrix.score_matrix]))
        print("----------------")
        self.iy_matrix.print_scores()
        #print("maxIy:",max([max(x)  for x in self.iy_matrix.score_matrix]))
        #print("M pointers")
        #self.m_matrix.print_pointers_old()
        #print("----------------")
        #print("Ix pointers")
        #self.ix_matrix.print_pointers_old()
        #print("----------------")
        #print("Iy pointers")
        #self.iy_matrix.print_pointers_old()
        #print("----------------")
        #this is better. all the pointers in one line this is for traceback not all tehe pointers.
        self.m_matrix.print_pointers()
        
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
        self.m_matrix.set_score(row,col, max(
            self.m_matrix.get_score(row-1,col-1) + 
            self.align_params.match_matrix.get_score(self.align_params.seq_a[row-1],self.align_params.seq_b[col-1]),
            self.ix_matrix.get_score(row-1,col-1) + 
            self.align_params.match_matrix.get_score(self.align_params.seq_a[row-1],self.align_params.seq_b[col-1]),
            self.iy_matrix.get_score(row-1,col-1) + 
            self.align_params.match_matrix.get_score(self.align_params.seq_a[row-1],self.align_params.seq_b[col-1])
        ))
        #set the pointers can do here or have to wait until updated? Need other values for pointers

    def update_ix(self, row, col):
        self.ix_matrix.set_score(row,col, max(
        self.m_matrix.get_score(row-1,col) - self.align_params.dy,
        self.ix_matrix.get_score(row-1,col) - self.align_params.ey
        ))

    def update_iy(self, row, col):        
        self.iy_matrix.set_score(row,col, max(
        self.m_matrix.get_score(row,col-1) - self.align_params.dx,
        self.iy_matrix.get_score(row,col-1) - self.align_params.ex
        ))

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
        if self.align_params.global_alignment==1:
            return (self.m_matrix.nrow, self.m_matrix.ncol)
        else:
            print("there can be only 1 local max? NO")
            maxM = max([max(x)  for x in self.m_matrix.score_matrix])
            maxIx = max([max(x)  for x in self.ix_matrix.score_matrix])
            maxIy = max([max(x)  for x in self.iy_matrix.score_matrix])
            max_all=max(maxM, maxIx, maxIy)
            max_loc =[(ix,iy) for ix, row in enumerate(a) for iy, i in enumerate(row) if i == 0]
            print("max_loc:",max_loc)
            return max_loc

    def traceback(self): ### FILL IN additional arguments ###
        """
        Performs a traceback.
        Hint: include a way to printing the traceback path. This will be helpful for debugging!
           ex. M(5,4)->Iy(4,3)->M(4,2)->Ix(3,1)->Ix(2,1)->M(1,1)->M(0,0)
        """
        ### FILL IN ###
        start = self.find_traceback_start()
        print("traceback_start:",start)
        i = start[0]
        j = start[1]
        node_path=NodePath()
        node_path.append([(i,j)])
        current=0 #0=M, 1=Ix, 2=Iy
        while(i>0 and j>0):
            print("backtrack i j:",i,j)
            if(i>0 and j>0):
                M = self.m_matrix.getM_pointer(i,j)
                Ix = self.m_matrix.getIx_pointer(i,j)
                Iy = self.m_matrix.getIy_pointer(i,j)
                
                
            else:
                print("backtrach origin i j",i,j)
        print("node_path:",node_path)

    def write_output(self):
        ### FILL IN ###
        return None


class NodePath:
    def __init__(self):
        '''
        paths contain all the paths
        '''
        self.paths = [[]]
    
    def branch(self):
        dup = []
        print("before dup:",len(self.paths))
        for x in self.paths:
            copy_me = copy.deepcopy(x)
            dup.append(copy_me)
        for x in dup:
            self.paths.append(x)
        print("after dup:",len(self.paths))
    def append(self, node_tuple):
        '''
        append single node to self.path
        '''
        for x in self.paths:
            x.append(node_tuple)



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
    #align.traceback()

if __name__=="__main__":
    main()
