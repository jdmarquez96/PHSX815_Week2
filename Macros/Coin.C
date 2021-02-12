#include <iostream>
#include <fstream>

#include "../src/Random.cc"

using namespace std;

// main function for compiled executable CoinToss

void Coin(int Ntoss = 10 ,int Nexp = 10 ){


  bool printhelp = false;
  long seed = 5555;

  // single coin-toss probability for "1"
  double p = 0.5;

  // Number of coin tosses (per experiment)

  // Number of experiments

  bool doOutputFile = false;
  string OutputFileName;
  


  // declare an instance of our Random class
  Random  random(seed);

  if(doOutputFile){ // write experiments to file
    ofstream outfile;
    outfile.open(OutputFileName.c_str());
    for(int e = 0; e < Nexp; e++){
      for(int t = 0; t < Ntoss; t++){
	outfile << random.Bernoulli(p) << " ";
      }
      outfile << endl;
    }
    outfile.close();
  } else { // write experiments to stdout
    for(int e = 0; e < Nexp; e++){
      for(int t = 0; t < Ntoss; t++){
	cout << random.Bernoulli(p) << " ";
      }
      cout << endl;
    }
  }
  
}
