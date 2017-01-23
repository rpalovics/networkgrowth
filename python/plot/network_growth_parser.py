
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import math

class Parser:

  def read(self,prefix):
    header=['node_num','nonzero','xmin','ks','delta','deltadeg','deg','degdelta'] 
    self.data = {}
    for d in ["oc","mh","15","fb","db","wi"]:
      self.data[d] = pd.read_csv(prefix + "dist_stats_" + d, sep=' ', header=None,names=header)
      self.data["r_" + d] = pd.read_csv(prefix + "dist_stats_r_" + d, sep=' ', header=None,names=header)

  def parse(self):
    for d in self.data:
      self.data[d] = self.data[d][self.data[d]['delta']>=0]
      self.data[d]["degree"]=self.data[d]["deg"]
      self.data[d]["deg"]=self.data[d]["deg"]-1
      self.data[d]["R"]=self.data[d]["nonzero"] / self.data[d]["node_num"]
      self.data[d]["degR"] = self.data[d]["R"] * (self.data[d]["deg"])
      self.data[d]["degreeR"] = self.data[d]["R"] * (self.data[d]["degree"])
      self.data[d]["deltadegR"] = self.data[d]["R"] * (self.data[d]["deltadeg"] + 1)

  def compute_best_ks(self):
    min_values = {}
    self.min_ks = {}
    for d in self.data:
      min_values[d] = self.data[d].groupby("node_num",as_index=False).min()
      self.min_ks[d] = {}
      for index, row in min_values[d].iterrows():
        self.min_ks[d][row["node_num"]] = row["ks"]

  def filter(self):
    self.filtered_data = {}
    for d in self.data:
      self.filtered_data[d] = {}
      self.filtered_data[d]["best"] = self.data[d][self.data[d].apply(lambda row: True if self.min_ks[d][row["node_num"]] == row["ks"] else False, axis=1)]
      self.filtered_data[d]["threshold"] = self.data[d][self.data[d].apply(lambda row: True if math.fabs(self.min_ks[d][row["node_num"]] - row["ks"]) < 0.05  else False, axis=1)]
      self.filtered_data[d][1] = self.data[d][self.data[d]["xmin"] == 1]


  def run(self,prefix):
    self.read(prefix)
    self.parse()
    self.compute_best_ks()
    self.filter()
    return self.filtered_data

