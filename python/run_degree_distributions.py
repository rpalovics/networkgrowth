import sys
from stats.degree_distributions import DegreeDistributions

file_name = sys.argv[1]
out_location = sys.argv[2]
prefix = sys.argv[3]

degree_distributions = DegreeDistributions(file_name,out_location,prefix)
degree_distributions.run()
