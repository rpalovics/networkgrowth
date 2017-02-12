import sys
import math


class DegreeDistributions:

  def __init__(self,file_name,out_location,prefix):
    self.degree_distribution = {}
    self.degrees = {}
    self.out_location = out_location
    self.file_name = file_name
    self.prefix = prefix
    self.zero_num = 0

  def run(self):
    f = open(self.file_name,"r")
    scale = 1
    for line in f:
      records = line.split(" ")
      node_a = int(records[1])
      node_b = int(records[2])
      self.add_node(node_a)
      self.add_node(node_b)
      self.update_degrees(node_a,node_b)
      log_size = int(math.log(len(self.degrees),2))
      if log_size >= scale:
        self.compute_degree_distribution()
        self.write_into_file(log_size)
        scale+=1
    self.compute_degree_distribution()
    log_size = math.log(len(self.degrees),2)
    self.write_into_file(log_size)

  def add_node(self,node):
    if node != - 1 and node not in self.degrees:
      self.degrees[node] = 0
      self.zero_num +=1

  def add_degree(self,degree):
    if degree not in self.degree_distribution:
      self.degree_distribution[degree] = 0

  def update_degrees(self,node_a,node_b):
    if node_b != -1:
      self.degrees[node_a]+=1
      self.degrees[node_b]+=1
      if self.degrees[node_a] == 1:
        self.zero_num-=1
      if self.degrees[node_b] == 1:
        self.zero_num-=1

  def compute_degree_distribution(self):
    self.degree_distribution.clear()
    self.sum = 0
    for node in self.degrees:
      degree = self.degrees[node]
      if degree > 0:
        self.add_degree(degree)
        self.degree_distribution[degree]+=1
        self.sum +=1

  def write_into_file(self,scale):
    f_out = open(self.out_location + self.prefix + "_" + str(scale),'w')
    for degree in self.degree_distribution:
      frequency = self.degree_distribution[degree]
      f_out.write(str(degree) + "," + str(frequency) + "," + str(frequency/float(self.sum)) + "\n")
