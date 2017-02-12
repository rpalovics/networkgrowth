import sys
import math
import networkx as nx

class NetworkEvents:

  def __init__(self,file_name,out_file):
    self.f = open(file_name,'r')
    self.f_out = open(out_file,'w')
    self.node_num = 0
    self.zero_num = 0
    self.avg_degree = 0
    self.edge_num = 0
    self.G = nx.Graph() 
    self.nodes = {}
    self.influence_num = 0
    self.random_num = 0

  def run(self):
    scale = 1
    log_size = 0
    for line in self.f:
      records = line.split(" ")
      node_a = int(records[1])
      node_b = int(records[2])
      self.update(node_a,node_b)
      if len(self.nodes) > 0:
        log_size = int(math.log(len(self.nodes),2))
      if log_size >= scale:
        self.write_into_file()
        scale+=1

  def add_nodes(self,nodes):
    for node in nodes:
      if node != -1 and node not in self.nodes:
        self.zero_num+=1
        self.nodes[node] = 1
        self.G.add_node(node)

  def decrease_zero(self,nodes):
    for node in nodes:
      if self.G.degree(node) == 1:
        self.zero_num-= 1

  def influence(self):
    self.influence_num +=1

  def random(self):
    self.random_num += 1

  def homophily(self,node_a,node_b):
    pass

  def update(self,node_a,node_b):
    self.add_nodes([node_a,node_b])
    if node_b != -1:
      if self.G.degree(node_b) == 0 or self.G.degree(node_a) == 0:
        if self.G.degree(node_a) == 0 and self.G.degree(node_b) == 0:
          self.random()
        else:
          self.influence()
      else:
        self.homophily(node_a,node_b)
      self.G.add_edge(node_a,node_b)
      self.decrease_zero([node_a,node_b])
      self.edge_num += 1

  def write_into_file(self):
    self.node_num = self.G.number_of_nodes()
    self.non_zero_num = self.node_num - self.zero_num
    self.avg_degree = self.edge_num * 2 / float(self.node_num)
    self.homophily_num = self.edge_num - self.influence_num - self.random_num 
    self.f_out.write(str(self.node_num) + " ")
    self.f_out.write(str(self.non_zero_num) + " ")
    self.f_out.write(str(self.zero_num) + " ")
    self.f_out.write(str(self.avg_degree) + " ")
    self.f_out.write(str(self.edge_num) + " ")
    self.f_out.write(str(self.influence_num) + " ")
    self.f_out.write(str(self.homophily_num) + " " )
    self.f_out.write(str(self.random_num) + "\n" )
