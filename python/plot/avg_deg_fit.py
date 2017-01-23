from scipy.optimize import curve_fit
import math
import pandas as pandas
import numpy as np
import matplotlib
from matplotlib import pyplot as plt 


class AvgDegFit:

  def __init__(self,data):
  	self.data = data
  	for d in data:
  		self.data[d][1]["log_n"] = np.log(self.data[d][1]["node_num"])/np.log(10)
  		self.data[d][1]["ln_n"] = np.log(self.data[d][1]["node_num"])

  def fit_func(self,x,*p):
    [a,b,c] = p
    return a + np.exp(b*x + c)

  def plot(self):
  	plt.figure(figsize=(16,14))
	i = 0
	for d in ["oc", "15", "mh", "fb", "db", "wi"]:
		i+=1
		pp = [1,1,1]
		bin_centres = self.data[d][1]["ln_n"]
		hist = self.data[d][1]["degree"]
		plt.subplot(3,2,i)
		plt.title(d)
		plt.plot(self.data[d][1]["log_n"],self.data[d][1]["degree"],'o',label="data",markersize=20)
		coeff, var_matrix = curve_fit(self.fit_func, bin_centres, hist, p0=pp)
                hist_fit = self.fit_func(bin_centres, *coeff) 
		plt.plot(self.data[d][1]["log_n"],hist_fit,'-',label="fitted curve")
		plt.xlabel(r"$\log_{10}($" + "number of nodes" + r"$)$")
		plt.ylabel("average degree")
		xmin = int(min(self.data[d][1]["log_n"]))
		xmax = int(max(self.data[d][1]["log_n"]))+1 
		plt.xticks(np.arange(xmin,xmax+1, 1.0))
		if i ==1:
			plt.legend(bbox_to_anchor=(-0.1, 1, 2.5, 1), loc=3,ncol=2,mode="expand", borderaxespad=1,markerscale=2,fontsize=30)
		plt.tight_layout()
