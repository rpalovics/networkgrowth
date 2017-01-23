import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import math
import itertools

class NetworkGrowth:

  def __init__(self,data):
    self.data = data

  def plot(self,d):
    marker = itertools.cycle(("o", "s", "^", "v", ">", "<", "D","*")) 
    plt.figure(figsize=(20,8))
    plt.subplot(1,2,1)
    for dd in d:
      plt.plot(self.data[dd]["best"]["node_num"],self.data[dd]["best"]["degree"],marker=marker.next(),markersize=20,label=dd)
    plt.xscale('log')
    plt.xlabel("number of nodes")
    plt.ylabel("average degree")
    plt.ylim(0.01,15)
    plt.yticks(np.arange(1, 15, 1.0))
    plt.xlim(1,1000000)
    plt.grid(b=True, which='minor', linestyle='--')
    plt.legend(bbox_to_anchor=(0., 1, 1, 1), loc=3,ncol=3,mode="expand", borderaxespad=0.,markerscale=1.,fontsize=28) 
    plt.subplot(1,2,2)
    for dd in d:
      plt.plot(self.data[dd]["best"]["node_num"],self.data[dd]["best"]["nonzero"]*self.data[dd]["best"]["degree"]*0.5,marker=marker.next(),markersize=20,label=dd)
    plt.xlabel("number of nodes")
    plt.ylabel("number of edges")
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1,1000000)
    plt.grid(b=True, which='minor', linestyle='--')
    plt.tight_layout()

  def run(self):
    d = ["oc","15","mh","fb","db","wi"]
    self.plot(d)
