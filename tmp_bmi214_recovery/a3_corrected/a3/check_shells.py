import os
import feature
import sys

filename = sys.argv[1]
pdbname = os.path.split(filename)[1]

ca_sites = [tuple(line.split()) for line in open("CAsites.txt")]
ca_nonsites = [tuple(line.split()) for line in open("CAnonsites.txt")]

all_sites = ca_sites + ca_nonsites

selected_sites = filter(lambda x: x[0] == pdbname, all_sites)

for i, site_tuple in enumerate(selected_sites):

    print("%s site %d" % (pdbname, i))

    site = feature.Point(*map(float, site_tuple[1:4]))
    prot = feature.Protein(filename)

    for aa in feature.RESIDUES:
        aa_present = ["n"] * 5
        for ca in prot.alpha_carbons:
            shell = site.getShell(ca.point)
            if shell < 5 and ca.residue == aa:
                aa_present[shell] = "y"

        print("  %s: %s" % (aa, ",".join(aa_present)))
