import sys
import math
import numpy as np

class AvgDegree:

  def __init__(self,data,col_1,col_2):
    self.data = data
    self.col_1 = col_1
    self.col_2 = col_2

  def run(self):
    self.sum = 0
    self.num = 0
    for i in range(len(self.data)):
      self.sum += self.data[i][self.col_1] * self.data[i][self.col_2]
      self.num += self.data[i][self.col_2]

  def get(self):
    return (self.sum / float(self.num))

  def get_number_of_nodes(self):
    return float(self.num)

