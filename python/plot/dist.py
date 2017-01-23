import matplotlib.pyplot as plt
import sys
import pandas as pd
import math
import numpy as np
import itertools
import sys
import copy
import collections
import seaborn as sns

class DistParser:

	def __init__(self,prefix):
		self.prefix = prefix
		self.data = {}

	def run(self):
		for d in ["oc","15","mh","fb","db","wi"]:
			self.data[d] = {}
                        keys = range(6,18)
			for i in keys:
				try:
  					dd = pd.read_csv(self.prefix + "dist_" + str(d) + "_" + str(i), sep=',', header=None,names=["x","y","yy"])
  					self.data[d][i] = dd
  					self.data[d][i] = self.data[d][i].sort_values(by='x')
  				except:
  					pass
  		self.norm()

  	def norm(self):
  		data_exp = {}
  		data_exp_ = {}
  		for d in self.data:
  			data_exp[d] = {}
  			data_exp_[d] = {}
  			for i in self.data[d]:
  				data_exp[d][i] = {}
  				data_exp_[d][i] = []
  				for index, row in self.data[d][i].iterrows():
  					key = int(math.log(row["x"])/math.log(2))
  					if key not in data_exp[d][i]:
  						data_exp[d][i][key] = 0
  					data_exp[d][i][key] += row["yy"]
  				for key in data_exp[d][i]:
  					data_exp[d][i][key] = data_exp[d][i][key] / math.pow(2,key)
  					data_exp_[d][i].append([math.pow(2,key),data_exp[d][i][key]])
  		for d in data_exp_:
  			for i in data_exp_[d]:
		   		data_exp_[d][i] = np.array(data_exp_[d][i])
   		self.data = data_exp_

   	def get(self):
   		return self.data

class Dist:

	def __init__(self,data):
		self.data = data

	def run(self):
		ii = 0 
		fig, axes = plt.subplots(figsize=(16,26))
		marker = itertools.cycle(("o", "s", "^", "v", ">", "<", "D","*"))
		for d in ["oc","15","mh","fb","db","wi"]:
			ii+=1
			plt.subplot(4,2,ii)
                        dd = collections.OrderedDict(sorted(self.data[d].items()))
			for i in dd:
                                plt.plot(self.data[d][i][:,0],self.data[d][i][:,1],'o-',label=str(int(i)),marker=marker.next(),markersize=15,linewidth=2)
                        for j in range(8-int(len(self.data[d]))%8):
                          marker.next()
			plt.yscale('log')
			plt.xscale('log')
			plt.xlabel("degree k")
			plt.ylabel("fraction of nodes with degree k")
			plt.grid(b=True, which='minor', linestyle='--')
                 	plt.title(d)
                        plt.legend()
                plt.tight_layout()
