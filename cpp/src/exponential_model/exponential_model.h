#ifndef EXMODEL
#define EXMODEL

#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
#include <cmath>

#include "utils/sparse_matrix.h"
#include "utils/network.h"

using namespace std;

struct ExponentialModelParameters{
  double N,H;
  double p,q,r,s;
};

struct ExponentialModelRunnerParameters{
  ExponentialModelParameters exponentialModelParameters;
  vector <double> sizes;
  string folder;
};

class ExponentialModel{
  private:
    Network G,F;
    double N,H,p,q,r,s,node_num;
    double G_edge_num, F_edge_num;
    double homo,ran,roo,inf;
  public:
    ExponentialModel(ExponentialModelParameters * parameters);
    void init_edges();
    void init_nodes();
    void run(int max_node_num);
    void random_edge();
    void random_influence();
    void random_root();
    void homophily();
    int pref(Network* net, double edge_num, int node);
    double compute_pref_value(Network * net, Edges* neighbors, double edge_num);
    int get_rand(double val);
    double rand_double();
    int rand_int(int a, int b);
    void add_edge(Network* net, int a , int b){
      net->addEdge(a,b,1);
      net->addEdge(b,a,1);
    };
    void writeIntoFile(string file_name){
      G.writeIntoFile(file_name);
      double zero = 0;
      for(uint ii=0; ii<node_num;ii++){
        if(G.getOutDegree(ii) == 0) zero++;
      }
      ofstream ofs(file_name + "_zero");
      ofs << zero << endl;
      ofs.close();
    };
    double deterministic(double num, double * sum);
};

class ExponentialModelRunner{
  public:
    ExponentialModelRunner(ExponentialModelRunnerParameters * parameters){
      srand(time(NULL));
      exponentialModelParameters = parameters->exponentialModelParameters; 
      sizes = parameters->sizes;
      folder = parameters->folder;
    };
    ~ExponentialModelRunner(){};
    void run();
  private:
    ExponentialModelParameters exponentialModelParameters;
    vector <double> sizes;
    string folder;
};

#endif
