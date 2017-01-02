import sys
import numpy as np
from stats.ml import ML
from stats.average_degree import AvgDegree
import math

prefix = sys.argv[1]
postfix = sys.argv[2]
infile = prefix + "_" + postfix
deli = sys.argv[3]
outfile = sys.argv[4]
col_1 = sys.argv[5]
col_2 = sys.argv[6]
base = float(sys.argv[7])

try:
  data = np.genfromtxt(infile,delimiter=deli)
  f_out = open(outfile,'a')

  if len(data) > 1:
    avg = AvgDegree(data,col_1,col_2)
    avg.run()
    degree = avg.get()
    nonzero = avg.get_number_of_nodes()

    ml = ML(data,col_1,col_2)
    ml.compute_alphas()
    ml.compute_KS()

    for i in range(len(ml.xmins)):
      alpha = ml.alphas[i]
      xmin = ml.xmins[i]
      ks = ml.KS[i]
      f_out.write(str(math.pow(base,int(postfix))) + " ")
      f_out.write(str(nonzero)  + " ")
      f_out.write(str(xmin)  + " ")
      f_out.write(str(ks)  + " ")
      f_out.write(str(alpha - 2) + " ")
      f_out.write(str(1 / float(alpha - 2))  + " ")
      f_out.write(str(degree)  + " ")
      f_out.write(str(1 / float(degree - 1))  + "\n")
  f_out.close()
except:
  print("no such file: " + infile)
