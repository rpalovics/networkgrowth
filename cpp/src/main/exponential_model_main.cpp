
#include<string>
#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>

#include "exponential_model/exponential_model.h"

int main (int argc, char* argv[]) {
  string folder = argv[1];
  double N = atof(argv[2]);
  double H = atof(argv[3]);
  double r = atof(argv[4]);
  double s = atof(argv[5]);
  double p = atof(argv[6]);
  double q = atof(argv[7]);
  double max_size = atof(argv[8]);
  int log_max_size = int((float)log(max_size) / log(2)) + 1;
  int log_min_size = log(N) / log(2) + 1;
  vector <double> sizes;
  for(int ii=log_min_size; ii<log_max_size+1; ii++){
    sizes.push_back(pow(2,ii));
  }
  ExponentialModelParameters parameters;
  parameters.H = H;
  parameters.N = N;
  parameters.r = r;
  parameters.q = q;
  parameters.p = p;
  parameters.s = s;
  ExponentialModelRunnerParameters parameters_;
  parameters_.exponentialModelParameters = parameters;
  parameters_.folder = folder;
  parameters_.sizes = sizes;
  ExponentialModelRunner model(&parameters_);
  model.run();
}


