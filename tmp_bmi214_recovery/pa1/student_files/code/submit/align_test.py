"""
Unit tests provide a way of testing individual components of your program.

This will help you with debugging and making sure you don't break your code!


Here, we provide some unit tests and a skeleton for a few others.
Note that you do not have to follow these exactly, they are designed to help you.


What other unit tests might you want to write?
 - Think about the traceback and writing the output file. 
 - Try to write at least one or two additional tests as you think of them.


To run:
  python align_test.py

Make sure align_key.py is located in the same directory, and the test_example.input file is present!
"""

import unittest
from align import *

TEST_INPUT_FILE="test_example.input"

class TestAlignmentClasses(unittest.TestCase):
    self.m = []
    self.m.append([0.,0.,0.,0.,0.])
    self.m.append([0.,1.0,0.,0.,0.])
    self.m.append([0.,1.0,1.0,0.9,0.4])
    self.m.append([0.,0.,1.0,1.0,0.9])
    self.m.append([0.,0.,1.4,2.0,1.0])
    self.m.append([0.,-1.0.,-0.2,1.1,3.0])

    self.ix = []
    self.ix.append([0.,0.,0.,0.,0.])
    self.ix.append([0.,-0.3,-0.3,-0.3,-0.3])
    self.ix.append([0.,0.4,-0.6,-0.6,-0.6])
    self.ix.append([0.,0.4,0.4,0.3,-0.2])
    self.ix.append([0.1,0.4,0.4,1.4,0.3])
    self.ix.append([0.,-0.2,0.9,1.4,0.4])

    self.iy = []
    self.iy.append([0.,-0.1,0.,0.,0.])
    self.iy.append([0.,-0.1,0.9,0.4,-0.1])
    self.iy.append([0.,-0.1,0.9,0.9,0.8])
    self.iy.append([0.,-0.1,-0.1,0.9,0.9])
    self.iy.append([0.,-0.1,-0.1,1.3,1.9])
    self.iy.append([0.,-0.1,-0.6,-0.3,1.0])
    
    def test_match_matrix(self):
        """
        Tests match matrix object
        """
        match_matrix = MatchMatrix("A","C",1,1)
        match_matrix.set_score("A", "C", 5)
        #should do an assert of all the entries!
        self.assertEqual(match_matrix.get_score("A", "C"), 5)

    
    def test_score_matrix_score(self):
        """
        Tests score matrix object score set + get methods
        """
        ### FILL IN ###
        # this should be very similar to test match matrix
        M = ScoreMatrix("M",2,2)
        M.set_score(1,1,3)
        self.assertEqual(M.get_score(1,1),3)
        
    
    def test_score_matrix_pointers(self):
        """
        Tests score matrix object pointer set + get methods
        """
        ### FILL IN ###
        M = ScoreMatrix("M",2,2)
        M.set_pointers(1,1,"M(0,0)")
        self.assertEqual(M.get_pointers(1,1),["M(0,0)"])

        
    
    def test_param_loading(self):
        """
        Tests AlignmentParameters "load_params_from_file()" function
        """
        align_params = AlignmentParameters()
        align_params.load_params_from_file(TEST_INPUT_FILE)
        self.assertEqual(align_params.seq_a, "AATGC")
        self.assertEqual(align_params.seq_b, "AGGC")
        self.assertTrue(align_params.global_alignment)
        self.assertEqual(align_params.dx, 0.1)
        self.assertEqual(align_params.ex, 0.5)
        self.assertEqual(align_params.dy, 0.6)
        self.assertEqual(align_params.ey, 0.3)
        self.assertEqual(align_params.alphabet_a, "ATGC")
        self.assertEqual(align_params.alphabet_b, "ATGCX")
        self.assertEqual(align_params.len_alphabet_a, 4)
        self.assertEqual(align_params.len_alphabet_b, 5)

        # test that the match match is set up correctly
        #  if this fails, make sure you are loading the asymmetric matrix properly!
        match_mat = align_params.match_matrix
        self.assertEqual(match_mat.get_score("A", "X"), 0.3)
        self.assertEqual(match_mat.get_score("C", "G"), -0.3)
        self.assertEqual(match_mat.get_score("G", "C"), 0)

    
    def test_update_ix(self):
        """
        Test AlignmentAlgorithm's update Ix
        """
        # configure alignment params
        align_params = AlignmentParameters()
        align_params.dy = 1
        align_params.ey = 0.5
        align = Align("", "")
        align.align_params = align_params
        align.m_matrix = ScoreMatrix("M", 5, 4)
        #we need to change this back to lower case!! Ix vs ix. Wasted a day
        align.ix_matrix = ScoreMatrix("Ix", 5, 4)
        align.m_matrix.set_score(2,2, 3)
        align.ix_matrix.set_score(2,2, 2.5)

        # run the method! this is row=3,col=2
        align.update_ix(3, 2)
        self.assertEqual(align.ix_matrix.get_score(3,2), 2)

        ### FILL IN for checking pointers! ###
        # note - in this example, it should point to M -AND- Ix
        # check by hand!
        #what is the format, 2 lists or 1 list? If they are equal we should have branched


    
    def test_update_m(self):
        """
        Test AlignmentAlgorithm's update M
        """
        ### FILL IN ###
       
        align_params = AlignmentParameters() 
        align_params.seq_a="ATGC"
        align_params.seq_b="ATGC"
        align = Align("", "")
        align.align_params = align_params
        mm = MatchMatrix("ATGC","ATGC",4,4)
        mm.set_score("A","A",1)
        mm.set_score("T","T",1)
        mm.set_score("G","G",1)
        mm.set_score("C","C",1) 
        align_params.match_matrix=mm
        align.m_matrix = ScoreMatrix("M", 5, 4)
        align.m_matrix.set_score(2,2, 3.)
        align.ix_matrix = ScoreMatrix("Ix", 5, 4)
        align.ix_matrix.set_score(2,2, 2.)
        align.iy_matrix = ScoreMatrix("Iy", 5, 4)
        align.iy_matrix.set_score(2,2, 1.)
        # run the method!
        align.update_m(3, 3)
        self.assertEqual(align.m_matrix.get_score(3,3), 4)
        
    
    def test_update_iy(self):
        """
        Test AlignmentAlgorithm's update Iy
        """
        ### FILL IN ###
        align_params = AlignmentParameters()
        align_params.dx = 1
        align_params.ex = 0.5

        align = Align("", "")
        align.align_params = align_params

        align.m_matrix = ScoreMatrix("M", 5, 4)
        align.iy_matrix = ScoreMatrix("Iy", 5, 4)
        align.m_matrix.set_score(2,2, 3)
        align.iy_matrix.set_score(2,2, 2.5)

        # run the method!
        align.update_iy(2, 3)
        self.assertEqual(align.iy_matrix.get_score(2,3), 2)
        #this is equal also, M and Iy. Not sure what convention is
        
    
    def init_matrix(self):


    def get_traceback_start(self):


    '''
    def check_score(self):
        """
        check final score
        """
        #the problem is teh left corner can be a gap? then the score is 0? 
        return None
    
    
    def test_traceback_start(self):
        """
        Tests that the traceback finds the correct start
        Should test local and global alignment!
        """

        return
    
    def test_NodePath(self):
        #do we need alignmentparameters to exist? 
        align = Align("","")
        nodepath = align.NodePath() 
        nodepath.append((1,1))
        self.assertEqual([[(1,1)]],nodepath.paths)
        nodepath.branch()
        self.assertEqual([[(1,1)],[(1,1)]],nodepath.paths)
    ''' 
    #def test_NodePath_duplicate(self):
        
if __name__=='__main__':
    unittest.main()