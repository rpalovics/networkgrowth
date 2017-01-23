import matplotlib.pyplot as plt
import sys
import pandas as pd
import math
import numpy as np
import itertools
import sys

class NonZero:

	def __init__(self,data):
		self.data = data

	def run(self):
		d = ["oc","15","mh"]
		plt.figure(figsize=(10,5))
		marker = itertools.cycle(("o", "s", "^", "v", ">", "<", "D","*"))
		for dd in d:
			plt.plot(self.data[dd]["best"]["node_num"],self.data[dd]["best"]["nonzero"]/self.data[dd]["best"]["node_num"],marker=marker.next(),markersize=15,label=dd,linewidth=2)
			plt.xscale('log')
			plt.xlabel("number of nodes")
			plt.ylabel('$NZ(n)$')
			plt.ylim(0,1)
			plt.xlim(10,1200000)
			plt.legend(loc=4)
