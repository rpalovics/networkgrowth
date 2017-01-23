import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import math

class SwapEdge:

  def __init__(self,data):
 	self.data = data

  def subplotter(self,d,x1,x2,y1,y2,xlabel="number of nodes",ylabel = "average degree"):
    plt.plot(self.data[d]["best"]["node_num"],self.data[d]["best"]["deg"]+1,marker='o',markersize=10,label="original")
    plt.plot(self.data["r_" + d]["best"]["node_num"],self.data["r_" + d]["best"]["deg"]+1,marker='s',markersize=10,label="random")
    plt.grid(b=True, which='minor', linestyle='--')
    plt.xlim(x1,x2)
    plt.ylim(y1,y2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc=2)


  def plot(self,d,x1,x2,y1,y2):
    fig, axes = plt.subplots(figsize=(8,4))
    fig.suptitle(d, fontsize=24)
    plt.subplot(1,1,1)
    self.subplotter(d,x1,x2,y1,y2)
    plt.xscale('log')

  def run(self):
    self.plot("oc",10,500000,1,6)
    self.plot("mh",50,1200000,1,5)
    self.plot("15",10,100000,1,5)
    self.plot("fb",10,100000,1,10)
    self.plot("db",10,10000000,1,8)
    self.plot("wi",10,2000000,1,40)
