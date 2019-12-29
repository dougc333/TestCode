# == Summary
#
#   Perform FEATURE like analysis of sites in protein.  The program
#   takes a sites file (PDB filenames and x, y, z coordinates) and
#   a similar non-sites file for training.  The '-v' adds verbose
#   output.  The program is invoked like this:
#
#       $ python feature.py -v -s sites.txt -n nonsites.txt -d pdbdir -p protein.pdb
#
#   By default the program outputs the following files:
#
#           {sitesfilename}_scores.txt    - just like sitesfilename but with the score appended
#           {nonsitesfilename}_scores.txt - just like nonsitesfilename but with the score appended
#           shell_0.txt                   - give the frequencies for each of the 5 shells
#           shell_1.txt
#           shell_2.txt
#           shell_3.txt
#           shell_4.txt
#           {protein}_100.txt                    - give the top 100 scores for the protein in protein.pdb
#
# == Examples
#
#   This command runs feature with CAsites.txt and
#   CAnonsites.txt, and looks for the PDB files in the
#   directory "./pdb/".  It also generates the top 100
#   scores for the protein 1FPW.pdb.  The output files
#   are all written to the directory './output'.  Note
#   that you do not specify the full path to 1FPW.pdb:
#
#       $ python feature.py -s CAsites.txt -n CAnonsites.txt -d pdb -p 1FPW.pdb -o output
#
#   This is a similar call, but has the files in different
#   subdirectories:
#
#       $ python feature.py -s data/CAsites.txt -n data/CAnonsites.txt -d data/pdb/ -p 1GGZ.pdb -o quizout
#
#   This command prints out help info:
#     python feature.py -h
#
# == Usage
#
#   python feature.py -s sites.txt -n nonsites.txt -d pdbdir -p protein.pdb
#
#   For help use: feature.py -h
#
# == Options
#
#   -s, --sitesfile     Specify the sites file to be used
#   -n, --nonsitesfile  Specify the non-sites file to be used
#   -d, --dir           Specify the directory for the PDB files
#   -p, --protein       Specify the name of the protein to evaluate (PDB filename, in pdbdir)
#   -o, --outputdir     Specify the directory to output the files ('.' is default)
#   -h, --help          Displays help message
#   -V, --verbose       Verbose output
#
# == Author
#   Guy Haskin Fernald
import sys
import re
import math
import operator
import getopt
import os.path
from functools import reduce

global verbose
verbose = False

RESIDUES = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS',
            'GLN', 'GLU', 'GLY', 'HIS', 'ILE',
            'LEU', 'LYS', 'MET', 'PHE', 'PRO',
            'SER', 'THR', 'TRP', 'TYR', 'VAL']


def usage():
    """print a usage message"""
    print("Usage: feature.py -s sites.txt -n nonsites.txt -d pdbdir -p protein.pdb -o outputdir")


class Vector(list):
    """A vector class to represent the features.  The feature vectors
       will just contain ones or zeros, but this vector class can be
       used more generally for vector arithmetic.  This class is also
       used to represent the x, y, z coordinates of the points."""

    def __init__(self, items):
        super(Vector, self).__init__(items)

    def __sub__(self, other):
        """return a new vector that is the result of adding other to this vector"""
        return Vector(map(operator.sub, self, other))

    def __add__(self, other):
        """return a new vector that is the result of adding other to this vector"""
        return Vector(map(operator.add, self, other))

    def __mul__(self, other):
        """return a new vector that is the result of mutliplying (by elt) other to this vector"""
        return Vector(map(operator.mul, self, other))

    def __div__(self, other):
        """return a new vector that is the result of mutliplying (by elt) other to this vector"""
        return Vector(map(operator.div, self, other))


class Point(object):
    """A class to represent a point in 3D space"""

    SHELL_DIAMETER = 1.5

    def __init__(self, x, y, z):
        super(Point, self).__init__()
        self.x, self.y, self.z = x, y, z

    def getShell(self, other):
        """return the shell number that point other is in,
           where shells are 1.5 Angstroms in diameter, this
           assumes the lower bound closed and the upper bound
           open."""
        distance = self._distance(other)
        shell = int(distance // Point.SHELL_DIAMETER)  # gives integer (floor)
        return shell

    def _distance(self, other):
        """Return the distance to point 'other'"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def __str__(self):
        return "<%.3f, %.3f, %.3f>" % (self.x, self.y, self.z)


class TopScores(object):
    """A class to keep top N items in an ordered list, the object
       keeps an ordered list of tuples (score, site), where score
       is the score for site.  The list is sorted highest to lowest."""

    def __init__(self, size=100):
        super(TopScores, self).__init__()
        self.size = size
        self.min = -(sys.maxsize - 1)             # current min score
        # initialize list to tuples with min
        self.list = [(self.min, None)] * size

    def insert(self, site, score):
        """Insert site with score into list.  This will
           will bump out the size element if necessary, ties
           are broken by sorting elements based on the
           values in their point vectors"""

        inserted = False

        # if the score is more than current
        # min score in top N then don't add

        if score > self.min:
            inserted = True

            # insert the new_vector, sort, drop the k+1
            # nearest and reset the max, here we settle ties
            # arbitrarily -- the numerical values of the
            # position vector determine sorting after
            # the distance

            self.list.append((score, site))
            self.list = sorted(self.list, reverse=True, key=lambda x: x[0])[
                0:self.size]  # tuples sort on 1st elt
            # trim the list
            self.min = self.list[self.size - 1][0]

        # return True if we inserted an element
        return inserted


class Protein(object):
    """Protein loaded from a PDB file.  It contains a attribute
         protein.alpha_carbons - which contains a list of the alpha
         carbons in the protein (a list of AlphaCarbon objects).
         We also keep track of the minimum and maximum values for
         each dimension so we know the extent of the protein.  (NB:
         for the purposes of this project we only consider the
         alpha carbons, not all of the atoms in the file.)"""

    # Define the parameters for grid generation.  We will generate a
    # grid from the min-6 to the max+6 for each dimension, at a spacing
    # of 2 Angstroms

    GRID_BORDER = 6
    GRID_SPACING = 2

    # keep a cache of the protein objects.  The interface for proteins
    # is through the Protein.getProtein static method, which will return
    # cached objects if possible.

    proteins = {}

    @staticmethod
    def getProtein(filename, path):
        """Get the protein associated with 'filename'.  If the protein has
           already been read in then it returns a cached version, otherwise
           it reads in the file and creates the object."""
        filepath = os.path.join(path, filename)
        if not Protein.proteins.__contains__(filepath):
            Protein.proteins[filepath] = Protein(filepath)
        return Protein.proteins[filepath]

    def __init__(self, filepath):
        """Load the protein information from the PDB file.
           This only loads the Alpha Carbon atoms information."""
        super(Protein, self).__init__()
        self.filepath = filepath
        self.alpha_carbons = []
        self.min = Point(sys.maxsize, sys.maxsize, sys.maxsize)
        self.max = Point(-(sys.maxsize - 1), -
                         (sys.maxsize - 1), -(sys.maxsize - 1))
        self._loadFile()

    def _loadFile(self):
        """Load the protein information from the PDB file.
           This only loads the Alpha Carbon atoms information."""

        for line in open(self.filepath):
            # Only look at the "ATOM" lines in the file
            if not re.search('^ATOM', line):
                continue

            # The indices here are for wwPDB format, see
            #
            #     http://www.wwpdb.org/documentation/format23/sect9.html
            #
            # for complete details.  Here we use:
            #
            #     13-16 is atom name
            #     18-20 is residue name
            #     31-38 is x coord
            #     39-46 is y coord
            #     47-54 is z coord

            atom_name = line[12:16]
            point = Point(float(line[30:38]), float(
                line[38:46]), float(line[46:54]))

            # for this program we only conisder the alpha carbons
            # these are indicated with 'CA' in the PDB file.  We ignore
            # any "MODEL" statements and just cover everything.

            if atom_name == " CA ":

                # If we have an alpha carbon we create a new
                # alpha carbon object and add it to our list of alpha
                # alpha carbons

                residue_name = line[17:20]
                alpha_carbon = AlphaCarbon(residue_name, point)
                self.alpha_carbons.append(alpha_carbon)

                # As we read in the file we keep track of the minimum and
                # maximum position for each dimension.
                #
                # NOTE: putting these updates in this if statements means
                # that we only consider the CA atoms for the protein (and thus
                # grid used for part 2 (prediction).  This was consistent with
                # the examples, but not with the instructions.  There was a TA
                # recommendation to do it this way.  To span the WHOLE protein
                # we would have to put these updates before this if statement.

                self._updateMin(point)
                self._updateMax(point)

    def _updateMin(self, point):
        """Update the min point with any new minimum values in 'point'."""
        self.min.x = min(self.min.x, point.x)
        self.min.y = min(self.min.y, point.y)
        self.min.z = min(self.min.z, point.z)

    def _updateMax(self, point):
        """Update the max point with any new maximum values in 'point'."""
        self.max.x = max(self.max.x, point.x)
        self.max.y = max(self.max.y, point.y)
        self.max.z = max(self.max.z, point.z)

    def grid(self):
        """Generator that returns points over entire protein."""

        # initialize a point -- the starting values get set at
        # level of the grid generation to the min value for that
        # dimension.
        point = Point(0, 0, 0)

        # Generate the grid.  We do this from Z to Y to X.  Start
        # at the min value - GRID_BORDER for each dimension and move
        # GRID_SPACING for each increment until we exceed the max
        # + GRID_BORDER.

        x_min = self.min.x - Protein.GRID_BORDER
        x_max = self.max.x + Protein.GRID_BORDER

        y_min = self.min.y - Protein.GRID_BORDER
        y_max = self.max.y + Protein.GRID_BORDER

        z_min = self.min.z - Protein.GRID_BORDER
        z_max = self.max.z + Protein.GRID_BORDER

        point.z = z_min
        while point.z <= z_max:

            point.y = y_min
            while point.y <= y_max:

                point.x = x_min
                while point.x <= x_max:

                    # YIELD the point from the generator
                    yield Point(point.x, point.y, point.z)
                    point.x = point.x + Protein.GRID_SPACING

                # Finished the X loop, increment Y
                point.y = point.y + Protein.GRID_SPACING

            # Finished the Y loop, increment Z
            point.z = point.z + Protein.GRID_SPACING

    def __str__(self):
        return "['%s'; %d ca]" % (self.filepath, len(self.alpha_carbons))


class AlphaCarbon(object):
    """A class to represent an alpha carbon.  It contains a point
       representing it's 3D location and a string property
       alpha_carbon.residue which is the three letter code for
       the amino acid."""

    def __init__(self, residue, point):
        super(AlphaCarbon, self).__init__()
        self.residue, self.point = residue, point

    def __str__(self):
        return "{%s, %s}" % (self.residue, str(self.point))


class Site(object):
    """A site is a Point within a Protein, it just contains a
       protein and a Point and provides a string representation."""

    def __init__(self, protein, point):
        super(Site, self).__init__()
        self.protein, self.point = protein, point

    def __str__(self):
        return "=%s; %s=" % (self.protein, self.point)


class Feature(object):
    """Main class to learn and predict"""

    # Define constant vectors that we can use in our calculations.  The
    # epsilon vectors are used for the scoring and ONES is used to
    # calculate probabilities
    #
    NUMERATOR_EPSILON = Vector([0.1] * 20 * 5)
    DENOMINATOR_EPSILON = Vector([0.2] * 20 * 5)
    ONES = Vector([1] * 20 * 5)

    def __init__(self, sites_file, nonsites_file, path="."):
        super(Feature, self).__init__()
        self.sites_file = sites_file
        self.nonsites_file = nonsites_file
        self.path = path

        # Count up the sites in each file, second result is total (denominator)
        site_counts, num_sites = self._countSites(self.sites_file)
        nonsite_counts, num_nonsites = self._countSites(self.nonsites_file)

        if verbose:
            print("len(site_counts)=%d num_sites=%d" %
                  (len(site_counts), num_sites))
            print("site_counts=%s" % ",".join([str(i) for i in site_counts]))
            print("len(nonsite_counts)=%d num_nonsites=%d" %
                  (len(nonsite_counts), num_nonsites))

        # Calculate the frequencies (estimated probabilities).  Just
        # divide by the total number of sites (or nonsites) and
        # add the epsilons to the numerator and denominator

        a = Vector(site_counts + Feature.NUMERATOR_EPSILON)
        b = Vector([num_sites] * 20 * 5) + Feature.DENOMINATOR_EPSILON
        res1 = []
        for i in range(len(a)):
            res1.append(a[i] / b[i])
        self.pr_in_site = Vector(res1)

        # Calculate the complementary probabilities by subtracting
        # from a vector of 1s

        self.pr_notin_site = Feature.ONES - self.pr_in_site

        c = Vector(nonsite_counts + Feature.NUMERATOR_EPSILON)
        d = Vector([num_nonsites] * 20 * 5) + Feature.DENOMINATOR_EPSILON
        res2 = []
        for i in range(len(c)):
            res2.append(c[i] / d[i])
        self.pr_in_nonsite = Vector(res2)

        self.pr_notin_nonsite = Feature.ONES - self.pr_in_nonsite

    def _countSites(self, filename):
        """Count the features in all of the sites.  Returns
           a tuple (counts, num_sites), where 'counts' is a vector
           of length 20*5 with the counts for each shell (the
           first 20 are shell 0, then shell 2 etc...), and
           'num_sites' is the total number of sites evaluated."""

        counts = Vector([0] * 20 * 5)
        num_sites = 0

        for site in self._sitesInFile(filename):
            num_sites = num_sites + 1
            features = self._featuresForSite(site)
            counts = counts + features

        return counts, num_sites

    def _featuresForSite(self, site):
        """Return a vector of features for this site.  The
           vector has length 20*5 (20 amino acid residues and
           5 shells).  Each entry is either 0 or 1.  For any
           index = shell*amino acid number, the value will
           be 1 if the amino acid is present in that shell,
           otherwise it is 0.  The order of amino acids is
           specified by the constant list 'RESIDUES'."""

        # start with an initialized vector of zeros
        features = Vector([0] * 20 * 5)

        # for each alpha carbon in the site's protein
        #    1. calculate the shell for that alpha carbon
        #    2. set the feature to '1' for that position in the feature vector

        for alpha_carbon in site.protein.alpha_carbons:
            shell = site.point.getShell(alpha_carbon.point)
            if 0 <= shell < 5:
                index = shell * 20 + RESIDUES.index(alpha_carbon.residue)
                features[index] = 1
        return features

    # SCORING FUNCTION.  Taken from the assignment instructions:
    #  If amino acid i is in shell j:
    #
    #    Sk = log(P(AA i in shell j | site)) -  log(P(AA i in shell j | non-site))
    #
    #  Otherwise:
    #
    #    Sk = log(P(AA i not in shell j | site)) - log(P(AA i not in shell j | non-site))
    #
    #  The final score for a query position is the sum score over all features:
    #
    #       sum(Sk) for 1<=k<=100

    def score(self, site):
        """docstring for score"""
        features = self._featuresForSite(site)

        # helper function that we use in the list generator below.  this
        # scores the feature based on whether or not it is present.
        def _scoreFeature(index, feature_is_present):
            if feature_is_present:
                return math.log(self.pr_in_site[index]) - math.log(self.pr_in_nonsite[index])
            return math.log(self.pr_notin_site[index]) - math.log(self.pr_notin_nonsite[index])

        scores = [_scoreFeature(index, value)
                  for index, value in enumerate(features)]

        return reduce(operator.add, scores, 0)

    def _sitesInFile(self, sites_filename):
        """Generator for yielding each site from a file.  Each site
           is yielded as a Site object."""

        # iterate over all the sites and yield a Site object for
        # each line.

        for line in open(sites_filename):
            protein_filename, x_str, y_str, z_str = line.split()
            x, y, z = float(x_str), float(y_str), float(z_str)
            site = Site(Protein.getProtein(
                protein_filename, self.path), Point(x, y, z))
            yield site

    def scoresForSitesFile(self, sites_filename):
        """Generator for computing scores for all sites in
           sites_filename, 'yield' is called for each site."""

        # use the sitesInFile generator to get all the sites and then
        # yield each site, score combination

        for site in self._sitesInFile(sites_filename):
            score = self.score(site)
            yield (site, score)

    def scoresForProteinFile(self, protein_filename):
        """Generator that yields scores for points over
           grid over whole protein."""

        # User the Protein.grid() generator to get the points over
        # the grid.  Then create a new site an score it.
        protein = Protein.getProtein(protein_filename, self.path)
        for point in protein.grid():
            site = Site(protein, point)
            yield site, self.score(site)


class Format(object):
    """Class to contain some formatting functions.  The example outputs
       have a variety of formats and these are designed to match those."""

    @staticmethod
    def float3strip(f):
        return "%s" % round(f, 3)

    @staticmethod
    def float3(f):
        return ("%.3f" % f)

    @staticmethod
    def float(f):
        return ("%f" % f)


class OutputWriter(object):
    """Class to handle output files for feature.  It
       contains a pointer to the feature objects and
       queries it to generate the output.  It also contains
       a list outputwriter.formats which contains the formats
       which are used for each of the floats in the output
       files these are adjusted so that they match the example
       output files that were provided."""

    def __init__(self, feature, outputdir):
        super(OutputWriter, self).__init__()
        self.feature = feature
        self.outputdir = outputdir
        formats = [Format.float3strip, Format.float3strip,
                   Format.float3strip, Format.float3]

    def outputShells(self, root_pathname):
        """Write out the AA frequencies for each shell in the
           root filename specified plus _{0,1,2,3,4}.txt"""

        # For each shell we create a new filename.
        for shell in range(5):
            output_filename = "%s_%d.txt" % (root_pathname, shell)
            output_filepath = os.path.join(self.outputdir, output_filename)
            output = open(output_filepath, "w")
            output.write("\t".join(["AA", "Sites", "NonSites"]))
            output.write("\n")

            # For each shell we go through each of the residues and
            # print(out the frequencies (probabilities).  We get these
            # by calculating the index: 20*shell+index(AA)

            for index, residue in enumerate(RESIDUES):
                output.write("\t".join(["%s" % residue,
                                        "%.3f" % self.feature.pr_in_site[
                                            20 * shell + index],
                                        "%.3f" % self.feature.pr_in_nonsite[20 * shell + index]]))
                output.write("\n")

    def outputScoresForFile(self, sites_filename):
        """Read in sites_filename and score each site, writing the output
           to an output file names 'sites_fileaname_scores.txt'."""

        sites_basename = os.path.basename(sites_filename)
        output_filename = OutputWriter.filename_append(
            sites_basename, "_scores")
        output_filepath = os.path.join(self.outputdir, output_filename)
        output = open(output_filepath, "w")

        # iterate through all of the sites and scores for the file.  This uses a
        # series of generators in Feature which 'yield' the sites and scores
        # here.
        for site, score in self.feature.scoresForSitesFile(sites_filename):
            output.write("\t".join([os.path.basename(site.protein.filepath),
                                    self.formats[0](site.point.x),
                                    self.formats[1](site.point.y),
                                    self.formats[2](site.point.z),
                                    self.formats[3](score)]))
            output.write("\n")

    def outputScoresForProteinFile(self, protein_filename):
        """Read in sites_filename and score each site, writing the output
           to an output file names 'protein_fileaname_100.txt'."""

        # make a TopScores object -- which will keep only the 100 best
        # scores as we insert them
        top100 = TopScores()

        # Score each site in the protein file, accumulating the top 100 scores.
        # This uses a series of generators, which yield the sites and the
        # scores, which are accumulated here.
        for site, score in self.feature.scoresForProteinFile(protein_filename):
            top100.insert(site, score)

        # Write the output file, the filename is generated by taking the basename
        # of the protein and appending '_100.txt'.
        protein_basename = os.path.basename(protein_filename)
        output_filename = OutputWriter.filename_append(
            protein_basename, "_100", ".txt")
        output_filepath = os.path.join(self.outputdir, output_filename)
        output = open(output_filepath, "w")
        for score, site in top100.list:
            output.write("\t".join([os.path.basename(site.protein.filepath),
                                    self.formats[0](site.point.x),
                                    self.formats[1](site.point.y),
                                    self.formats[2](site.point.z),
                                    self.formats[3](score)]))
            output.write("\n")

    @staticmethod
    def filename_append(filename, string, extension=None):
        """Helper function to append a string to a filename
           but leave the extension. Given 'filename.ext' and
           'string' returns the string, 'filename_string.ext'.
           if the optional extension is provided than that
           extension is used instead."""

        name_list = list(os.path.splitext(filename))
        name_list.insert(1, string)
        if extension:
            name_list[2] = extension
        return "".join(name_list)


def main(argv):
    """main function to run feature, do command line processing"""

    # Parse the command lines, example usage:
    # feature.py -s sites.txt -n nonsites.txt -d pdbdir -p protein.pdb -o
    # outputdir
    global verbose
    opts, args = getopt.getopt(argv[1:],
                               "hvs:n:d:p:o:",
                               ["help", "verbose", "sitesfile=",
                                "nonsitesfile=", "dir=", "protein=",
                                "outputdir="])

    # set defaults for the option list.  Later we check if these aren't set
    # and fail if they are not set.
    sites_filename = None
    nonsites_filename = None
    pdb_directory = None
    sites_filename = None
    protein_filename = None
    outputdir = None

    for o, a in opts:
        if o in ("-s", "--sitesfile"):
            sites_filename = a
        elif o in ("-n", "--nonsitesfile"):
            nonsites_filename = a
        elif o in ("-d", "--dir"):
            pdb_directory = a
        elif o in ("-p", "--protein"):
            protein_filename = a
        elif o in ("-o", "--outputdir"):
            outputdir = a
        elif o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            raise "unhandled option"

    # There are no other options, everything is set with a flag
    if len(args) != 0:
        usage()
        sys.exit(1)

    # sites_filename and nonsites_filename are required
    if not (sites_filename and nonsites_filename):
        usage()
        sys.exit(1)

    # set the pdb_directory to "." as a default
    if not pdb_directory:
        pdb_directory = "."

    # set the outputdir to "." as a default
    if not outputdir:
        outputdir = "."

    if verbose:
        print("Loading sites files (%s, %s, %s)..." %
              (sites_filename, nonsites_filename, pdb_directory))

    # RUN FEATURE.  Put this is a try so that
    # we can catch any problems with files.
    try:
        feature = Feature(sites_filename, nonsites_filename, pdb_directory)
        output_writer = OutputWriter(feature, outputdir)
    except Exception:
        print(sys.exc_info()[1])
        usage()
        sys.exit(1)

    if verbose:
        print("Writing out shells...")

    # OUTPUT THE RESULTS:
    #    1. First, the shells.
    output_writer.outputShells("shell")

    if verbose:
        print("Writing out scores for file '%s' ..." % sites_filename)

    #    2. Now ouput the scores for sites_filename
    output_writer.formats = [Format.float3strip,
                             Format.float3strip, Format.float3strip, Format.float3]
    output_writer.outputScoresForFile(sites_filename)

    if verbose:
        print("Writing out scores for file '%s' ..." % nonsites_filename)

    #    3. Now ouput the scores for nonsites_filename
    output_writer.formats = [
        Format.float, Format.float3strip, Format.float3strip, Format.float3]
    output_writer.outputScoresForFile(nonsites_filename)

    #    4. If a protein_filename is specified we generate the top 100
    #       scores and write those out too.
    if protein_filename:

        if verbose:
            print("Writing out top 100 scores for file '%s' ..." %
                  protein_filename)

        output_writer.formats = [Format.float3,
                                 Format.float3, Format.float3, Format.float3]
        output_writer.outputScoresForProteinFile(protein_filename)

if __name__ == '__main__':
    main(sys.argv)
