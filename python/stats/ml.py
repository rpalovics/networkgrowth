import sys
import math
import numpy as np

class ML:

  def __init__(self,data,idx,idy):
    self.data = data[data[:, 0].argsort()]
    self.idx = int(idx)
    self.idy = int(idy)
    self.alphas = []
    self.xmins = []
    self.KS = []
    self.num = 0

  def compute_alphas(self):
    if len(self.data) > 1:
      sum = 0
      for j in range(len(self.data)):
        i = int(len(self.data) - j - 1)
        x = self.data[i][self.idx]
        if x > 0:
          sum += self.data[i][self.idy] * math.log(x)
          self.num += self.data[i][self.idy] 
          norm = sum / float(self.num)
          if norm != math.log(x):
            alpha = 1 / float (norm - math.log(x)) + 1
            self.alphas.append(alpha)
            self.xmins.append(x)

  def compute_KS(self):
    for i in range(len(self.alphas)):
      alpha = self.alphas[i]
      xmin = self.xmins[i]
      CDF = 0
      KS = 0
      for j in range(len(self.data)):
        x = self.data[j][self.idx]
        if x > 0:
          if CDF > 0:
            diff = math.fabs(1 - math.pow(x,1-alpha) -CDF)
            if diff > KS:
              KS = diff
          CDF += self.data[j][self.idy] / float(self.num)
      self.KS.append(KS)

  def get_best_KS(self):
    min = 1
    min_id = -1
    for i in range(len(self.KS)):
      if self.KS[i] < min:
        min = self.KS[i]
        min_id = i
    return (self.alphas[min_id],self.xmins[min_id],self.KS[min_id])

  def get(self,x):
    for i in range(len(self.xmins)):
      if x == self.xmins[i]:
        return (self.alphas[i],self.xmins[i],self.KS[i])
