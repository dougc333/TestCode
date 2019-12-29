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

    def test_match_matrix(self):
        """
        Tests match matrix object
        """
        match_matrix = MatchMatrix()
        match_matrix.set_score("A", "C", 5)
        self.assertEqual(match_matrix.get_score("A", "C"), 5)

    def test_score_matrix_score(self):
        """
        Tests score matrix object score set + get methods
        """
        ### FILL IN ###
        # this should be very similar to test match matrix
        return

    def test_score_matrix_pointers(self):
        """
        Tests score matrix object pointer set + get methods
        """
        ### FILL IN ###
        return

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

        # create an alignment object
        align = Align("", "")
        align.align_params = align_params

        align.m_matrix = ScoreMatrix("M", 5, 4)
        align.ix_matrix = ScoreMatrix("Ix", 5, 4)
        align.m_matrix.set_score(2,2, 3)
        align.ix_matrix.set_score(2,2, 2.5)

        # run the method!
        align.update_ix(3, 2)

        score = align.ix_matrix.get_score(3,2)
        self.assertEqual(score, 2)

        ### FILL IN for checking pointers! ###
        # note - in this example, it should point to M -AND- Ix
        # check by hand!


    def test_update_m(self):
        """
        Test AlignmentAlgorithm's update M
        """
        ### FILL IN ###
        return
    
    def test_update_iy(self):
        """
        Test AlignmentAlgorithm's update Iy
        """
        ### FILL IN ###
        return

    def test_traceback_start(self):
        """
        Tests that the traceback finds the correct start
        Should test local and global alignment!
        """
        return


if __name__=='__main__':
    unittest.main()