#include "exponential_model.h"

ExponentialModel::ExponentialModel(ExponentialModelParameters * parameters){
  p = parameters->p;
  q = parameters->q;
  r = parameters->r;
  s = parameters->s;
  N = (int)parameters->N;
  H = parameters->H;
  cerr << p << " " << q << " " << r << " " << s << " " << N << " " << H << endl;
  homo = 0;
  ran = 0;
  roo = 0;
  inf = 0;
  G_edge_num = 0;
  F_edge_num = 0;
  F_edge_num_float = 0;
  init_nodes();
  init_edges();
}

void ExponentialModel::init_nodes(){
  node_num = 0;
  G.createEdges();F.createEdges();
  G.resize(N);F.resize(N);
  node_num = int(N);
  node_num_float = int(N);
}

void ExponentialModel::init_edges(){
  int Nr = (double)N * 2 * r / (2*r + p + q);
  int Ni = (double)N * p / (2*r + p + q);
  int ii = 0; 
  for(ii = 0; ii<(int)(Nr); ii+=2){
    add_edge(&G,ii,ii+1);
    G_edge_num++;
  }
  for(int jj = 0; jj<Ni; jj++){
    int a = ii + jj;
    int b = rand_int(1,ii)-1;
    while(a == b){
      b = rand_int(1,ii)-1;
    }
    add_edge(&G,a,b);
    G_edge_num++;
  }
  for(int ii = 0; ii<(int)H; ii++){
    int a = rand_int(1,N)-1;
    int b = rand_int(1,N)-1;
    while(G.getEdgeWeight(a,b)==1 or a==b){
      a = rand_int(1,N)-1;
      b = rand_int(1,N)-1;
    }
    add_edge(&F,a,b);
    add_edge(&G,a,b);
    F_edge_num++;
    F_edge_num_float++;
    G_edge_num++;
  } 
}

void ExponentialModel::run(int max_node_num){
  while(node_num <max_node_num){
    node_num_old=node_num_float;
    random_edge();
    homophily();
    random_root();
    random_influence();
  } 
}

void ExponentialModel::random_edge(){
 double num =  r * (double)node_num_old;
 node_num_float+=2*num;
 num = deterministic(num,&ran);
 for(int ii=0; ii<num; ii++){
   add_edge(&G,node_num,node_num+1);
   node_num+=2;
   G_edge_num++;
 }
 F.resize(node_num);
}

void ExponentialModel::homophily(){
  double num = F_edge_num_float * 2 * s;
  F_edge_num_float+=num;
  num = deterministic(num,&homo);
  for(int ii=0; ii<num; ii++){
    int k = pref(&F,F_edge_num,-1);
    while(G.getOutDegree(k) >= node_num -2){
      k = pref(&F,F_edge_num,-1);
    }
    int l = pref(&G,G_edge_num,k); 
    add_edge(&G,k,l);
    add_edge(&F,k,l);
    F_edge_num++;
    G_edge_num++;
  }
}

void ExponentialModel::random_root(){
 double num =  q * (double)node_num_old;
 node_num_float+=2*num;
 num = deterministic(num,&roo);
 node_num+=num;
 G.resize(node_num);
 F.resize(node_num);
}

void ExponentialModel::random_influence(){
 double num =  p * (double)node_num_old;
 node_num_float+=2*num;
 num = deterministic(num,&inf);
 for(uint ii=0; ii<num; ii++){
   int a = rand_int(1,node_num)-1;
   node_num++; 
   add_edge(&G,node_num-1,a);
   F.resize(node_num);
 }
}

double ExponentialModel::compute_pref_value(Network * net, Edges * neighbors, double edge_num){
  double sum = edge_num * 2;
    if(neighbors != NULL){
      sum-=neighbors->size();
      for(EdgeIterator ie = neighbors->begin(); ie!= neighbors->end(); ie++){
        sum-= net->getOutDegree(ie->first); 
      }
    }
  double return_sum = 0;
  if(sum>0){
    while(return_sum==0){
      return_sum = rand_double() * sum;
    }
  }
  return return_sum; 
}

int ExponentialModel::pref(Network* net, double edge_num, int node){
  Edges * neighbors = NULL;
  if(node!=-1) neighbors = net->getOutEdges(node);
  double sum = compute_pref_value(net,neighbors,edge_num);
  int ii = -1;
  double summ = 0;
  while(summ < sum){
    ii+=1; 
    if (ii != node and (neighbors== NULL or neighbors->find(ii) == neighbors->end()))
      summ+=net->getOutDegree(ii);
  }
  if(ii == -1){
    ii++;
    while(net->getOutDegree(ii)>0) ii++;
  } 
  return ii;
}

int ExponentialModel::get_rand(double val){
  if(val < 1){
    if(val > 0){
      if(rand_double() < val) return 1;
      else return 0; 
    }
    else return 0;
  }
  else{
    if(rand_double() < val - (int)val) return (int) val + 1;
    else return (int) val;
  }
}

int ExponentialModel::rand_int(int a,int b){
  double f = (double)rand() / RAND_MAX;
  return a + (int)(f * (b - a));
}

double ExponentialModel::rand_double(){
  return (double)rand() / RAND_MAX;
}

void ExponentialModelRunner::worker(int _threadIdx){
  ExponentialModelParameters p = exponentialModelParameters;
  ExponentialModel model(&p);
  vector <double> s = sizes;
  for(uint ii=0;ii<s.size();ii++){
    model.run(s[ii]); 
    string fileName = folder + "/network_";
    fileName += to_string((int)(1000*p.p)) + "_";
    fileName += to_string((int)(1000*p.q)) + "_";
    fileName +=to_string((int)(1000*p.r)) + "_";
    fileName += to_string((int)(1000*p.s)) + "_";
    fileName += to_string((int)p.H) + "_";
    fileName += to_string((int)p.N) + "_";
    fileName += to_string((int)s[ii]) + "_";
    fileName += to_string((int)_threadIdx); 
    model.writeIntoFile(fileName);
  }
}

void ExponentialModelRunner::run(){
  CreateAndRun(repeat,repeat);
}


double ExponentialModel::deterministic(double num,double * sum){
  if(num < 0.5){
    *sum += num;
    num = (int)*sum;
    if(*sum > 1) *sum = *sum - (int)*sum;
  }
  else num = get_rand(num);
  return num;
 }
