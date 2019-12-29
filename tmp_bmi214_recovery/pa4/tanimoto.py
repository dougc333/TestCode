
import argparse


class Tanimoto:
    def __init__(self):
        #nothing here so far



if __name__=="__main__":
    parser = argparse.ArgumentParser()
	parser.add_argument(arg1, type=str, default='drugs.csv' help='drugs.csv location')
	parser.add_argument(arg2, type=str, default='targets.csv', help='targets.csv location')
	parser.add_argument(arg3, type=str, default='outputfile.csv', help='outputfile.csv location')
    t = Tanimoto(arg1,arg2,arg3)
