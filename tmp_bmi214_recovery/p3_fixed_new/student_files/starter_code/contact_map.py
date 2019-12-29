import Bio.PDB
import numpy as np
import sys
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


def calc_dist(res1, res2):
    dist = res1["CA"].coord - res2["CA"].coord
    return np.sqrt(np.sum(dist**2))

def calc_dist_matrix(structure):
    chainA = structure[0]['A']
    dists = np.zeros((len(chainA), len(chainA)), dtype=np.float)
    for i, resi in enumerate(chainA):
        for j, resj in enumerate(chainA):
            dists[i,j] = calc_dist(resi, resj)
    return dists

def plot_matrix(mat, outfile):
    plt.figure(figsize=(10,10))
    sns.heatmap(mat)
    plt.savefig(outfile)


def main(pdb, outfile):
    pdb_name = pdb.split('/')[-1][:-4]
    structure = Bio.PDB.PDBParser().get_structure(pdb_name, pdb)
    dist_mat = calc_dist_matrix(structure)
    plot_matrix(dist_mat, outfile)

if __name__=='__main__':
    pdb = sys.argv[1]
    outfile = sys.argv[2]
    main(pdb, outfile)

    