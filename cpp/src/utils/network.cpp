#include  "network.h"

void Network::readFromFile(string fileName){
  outEdges= new SpMatrix;
  outEdges->readFromFile(fileName.c_str());
}

void Network::writeIntoFile(string fileName){
  outEdges->writeIntoFile(fileName);
}

int Network::getOutDegree(int nodeID){
  return outEdges->rowSize(nodeID);
}

int Network::getInDegree(int nodeID){
  return inEdges->rowSize(nodeID);
}

Edges * Network::getOutEdges(int nodeID){
  if(outEdges!=NULL) return outEdges->get(nodeID);
  else return NULL;
}

Edges * Network::getInEdges(int nodeID){
  if(inEdges!=NULL) return inEdges->get(nodeID);
  else return NULL;
}

void Network::setEdgeWeight(int nodeID1,int nodeID2,double  weight){
  if(outEdges==NULL) outEdges = new SpMatrix;
  outEdges->update(nodeID1, nodeID2, weight); 
  if(inEdges!=NULL) inEdges->update(nodeID2, nodeID1, weight);
}

void Network::setEdgeWeight(EdgeIterator ie, double weight){
  ie->second = weight;
}

double Network::getEdgeWeight(int nodeID1,int nodeID2){
  return outEdges->get(nodeID1, nodeID2); 
}

void Network::increaseEdgeWeight(int nodeID1, int nodeID2, double weight){
  if(outEdges==NULL) outEdges = new SpMatrix;
  outEdges->increase(nodeID1, nodeID2, weight);
  if(inEdges!=NULL) inEdges->increase(nodeID2, nodeID1, weight);
}
void Network::createEdges(){
  inEdges = new SpMatrix;
  outEdges = new SpMatrix;
}

void Network::createInEdges(){
  if(inEdges==NULL){
    inEdges = new SpMatrix;
    if(outEdges!=NULL){
      int rowNum=outEdges->size();
      for(int nodeID=0; nodeID<rowNum; nodeID++){
        Edges * edges = outEdges->get(nodeID);
        if(edges!=NULL){
          for(EdgeIterator et=edges->begin(); et!=edges->end(); et++){
            int neighborID=et->first;
            double weight=et->second;
            inEdges->update(neighborID,nodeID,weight);
          }
        }
      }
    }
  }
}

int Network::getNodeNum(){
  return max(getOutNodeNum(),getInNodeNum());
}

int Network::getOutNodeNum(){
  if(outEdges!=NULL) return outEdges->size();
  else return 0;
}

int Network::getInNodeNum(){
  if(inEdges!=NULL) return inEdges->size();
  else return 0;
}

int Network::getEdgeNum(){
  if(outEdges==NULL) return 0;
  else{
    int edgeNum=0;
    for (int nodeID=0; nodeID<getOutNodeNum(); nodeID++) edgeNum+=getOutDegree(nodeID);
    return edgeNum;
  }
}

int Network::getDegreeNodeNum(){
  return max(getOutDegreeNodeNum(),getInDegreeNodeNum());
}

int Network::getOutDegreeNodeNum(){
  if(outEdges!=NULL){
    int num=0;
    for(int nodeID=0; nodeID<outEdges->size(); nodeID++){
      if(getOutDegree(nodeID)>0) num++;
    }
    return num;
  }
  else return 0;
}

int Network::getInDegreeNodeNum(){
  if(inEdges!=NULL){
    int num=0;
    for(int nodeID=0; nodeID<inEdges->size(); nodeID++){
      if(getInDegree(nodeID)>0) num++;
    }
    return num;
  }
  else return 0;
}

void Network::addEdge( int nodeID1, int nodeID2, double weight){
  if(outEdges==NULL) outEdges = new SpMatrix;
  outEdges->insert(nodeID1, nodeID2, weight);
  if(inEdges!=NULL) inEdges->insert(nodeID2, nodeID1, weight); 
}

int Network::getRealOutNodeNum(){
  if(outEdges!=NULL){
    int nodeNum = 0;
    for(uint ii=0; ii<outEdges->size(); ii++){
      Edges * neighbors = outEdges->get(ii);
      if(neighbors!=NULL) nodeNum++;
    }
    return nodeNum;
  }
  else return 0;
}

int Network::getRealInNodeNum(){
  if(inEdges!=NULL){
    int nodeNum = 0;
    for(uint ii=0; ii<inEdges->size(); ii++){
      Edges * neighbors = inEdges->get(ii);
      if(neighbors!=NULL) nodeNum++;
    }
    return nodeNum;
  }
  else return 0;
}

int Network::getRealNodeNum(){
  int nodeNum = getNodeNum();
  createInEdges();
  if(inEdges!=NULL && outEdges!=NULL){ 
    int sum=0;
    for(uint ii=0; ii<nodeNum; ii++){
      if(outEdges->get(ii)!=NULL || inEdges->get(ii)!=NULL) sum++;
    }
    return sum;
  }
  else return 0;
}

vector <int> Network::getNodes(){
  int nodeNum = getNodeNum();
  vector <int> nodes;
  nodes.clear();
  createInEdges();
  if(inEdges!=NULL && outEdges!=NULL){ 
    for(uint ii=0; ii<nodeNum; ii++){
      if(outEdges->get(ii)!=NULL || inEdges->get(ii)!=NULL){
        nodes.push_back(ii);
      }
    }
  }
  return nodes;
}


void Network::eraseEdge(int nodeID1,int nodeID2){
  if(outEdges != NULL){
    outEdges->erase(nodeID1,nodeID2);
  }
  if (inEdges !=NULL){
    inEdges->erase(nodeID1,nodeID2);
  }
}
