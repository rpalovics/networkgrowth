#ifndef NETWORK
#define NETWORK

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

#include "sparse_matrix.h"

using namespace std;

typedef MatrixRow Edges;
typedef RowIterator EdgeIterator;

class Network{
  
  private:
    SpMatrix * outEdges;
    SpMatrix * inEdges;
    vector <double> outWeights;
    vector <double> inWeights;
    int numberOfEdges; 
  public: 
    Network(){outEdges=NULL;inEdges=NULL;};
    ~Network(){};
    void readFromFile(string fileName);
    void writeIntoFile(string fileName);
    void createEdges();
    int getEdgeNum();
    int getNodeNum();
    int getRealOutNodeNum();
    int getRealInNodeNum();
    int getRealNodeNum();
    int getInNodeNum();
    int getOutNodeNum();
    int getDegreeNodeNum();
    int getOutDegreeNodeNum();
    int getInDegreeNodeNum();
    int getOutDegree(int nodeID);
    int getInDegree(int nodeID);
    Edges * getOutEdges(int nodeID);
    Edges * getInEdges(int nodeID);
    vector <int> getNodes();
    void addEdge(int nodeID1,int nodeID2,double  weight);    
    void eraseEdge(int nodeID1,int nodeID2);    
    void setEdgeWeight(int nodeID1,int nodeID2,double  weight);
    void setEdgeWeight(EdgeIterator ie, double  weight);
    double getEdgeWeight(int nodeID1,int nodeID2);
    void increaseEdgeWeight(int nodeID1,int nodeID2,double  weight);
    void resize(int size){outEdges->resize(size);}; 
    void createInEdges();

    void clear(){inEdges->clear();outEdges->clear();};
};

#endif
