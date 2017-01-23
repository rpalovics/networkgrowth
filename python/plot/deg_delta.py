import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import math

class DegDelta:

  def __init__(self,data):
 	self.data = data
  sns.set_palette("dark")

  def subplotter(self,d,x,y,y_ref,x1,x2,y1,y2,xlabel,ylabel,loc,log,i):
    plt.subplot(1,2,i)
    plt.plot(self.data[d]["threshold"][x],self.data[d]["threshold"][y],'o',marker="D",label=r'$\hat{\alpha}_{0.05}$',alpha=0.95,markersize=15)
    plt.plot(self.data[d]["best"][x],self.data[d]["best"][y],'o',marker='s',label=r'$\hat{\alpha}(x_m)$',alpha=0.95,markersize=15)
    plt.plot(self.data[d][1][x],self.data[d][1][y],'o',marker='^',label=r'$\hat{\alpha}(x=1)$',alpha=0.95,markersize=15)
    plt.plot(self.data[d]["best"][x],self.data[d]["best"][y_ref],'-o',label="degree",markersize=15)
    plt.grid(b=True, which='minor', linestyle='--')
    plt.xlim(x1,x2)
    plt.ylim(y1,y2)
    plt.xlabel(xlabel,labelpad=0)
    plt.ylabel(ylabel,labelpad=0)
    if loc != 0:
      plt.legend(bbox_to_anchor=(0., 1, 2.3, 1), loc=3,ncol=2,mode="expand", borderaxespad=0.,markerscale=1.5,fontsize=28)
    if log == 1:
      plt.yscale('log')
    plt.xscale('log') 

  def plot(self,d,x1,x2,ey1,ey2,dy1,dy2,loc):
        flatui = [ "#2ecc71", "#34495e","#3498db", "#e74c3c"]
        sns.set_palette(sns.color_palette(flatui))
        fig, axes = plt.subplots(figsize=(12,4))
        fig.suptitle(d, fontsize=30)
  	self.subplotter(d,"node_num","deltadegR","degreeR",x1,x2,dy1,dy2,"number of nodes","average degree",loc,0,1)
        self.subplotter(d,"node_num","delta","degdelta",x1,x2,ey1,ey2,"number of nodes",r'$\Delta$',0,1,2)
        plt.tight_layout()

  def run(self):
    self.plot("oc",100,500000,0.1,6,0.8,10,1)
    self.plot("15",10,50000,0.1,4,0.8,6,0)
    self.plot("mh",100,1000000,0.1,20,0.8,6,0)
    self.plot("fb",10,100000,0.1,6,0.5,8,0)
    self.plot("db",10,2000000,0.01,20,1,8,0)
    self.plot("wi",10,2000000,0.01,3,1,10,0)
