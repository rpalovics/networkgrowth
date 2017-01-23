import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import math



class EdgeSamplingParser:

  def run(self,folder):
    header = ["node_num","non_zero_num","zero_num","avg_degree","edge_num","influence_num","homophily_num","random_num"]
    self.data = {}
    for d in ["oc","mh","15","fb","db","wi"]:
      self.data[d] = pd.read_csv(folder + "events_" + d, sep=' ', header=None,names=header)
      self.data["r_" + d] = pd.read_csv(folder + "events_r_" + d, sep=' ', header=None,names=header)
    return self.data


