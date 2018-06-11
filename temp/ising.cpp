/*
Simulates Ising model using Monte Carlo techniques
Amol Deshmukh
*/

#include <iostream>
#include <ctime>
#include <cmath>
#include <cstdlib>

using namespace std;

int main()
{
	// Size of the lattice
	long int N_size {pow(10,3)};
	int Latt[N_size][N_size];

	// Random seed
	srand(time(NULL));

	// A complicated way of generating a lattice of +1s and -1s
	for (int i = 0; i < N_size; ++i)
	{
		for (int j =0; j < N_size; j++)
		{
			double a;
			a = ((double)rand() / (RAND_MAX));
			if (a<0.5)
				{
					a=-1;
				}
			else
				{
					a=1;
				}
			Latt[i][j]= a;
		}
	}	

	// Monte Carlo sweeps
	long int N_sweeps {pow(10,3)};
	for (int i=1; i < N_sweeps; ++i)
	{	
		int k,l;
		int sum[N_sweeps];
		float temp = 1.1;
		double local_energy;

		// Choosing a random spin on a lattice
		k=rand()%N_size;
		l=rand()%N_size;

		// Local energy 
		local_energy = 2*Latt[k][l]*
			(Latt[(k+1)%N_size][l]
			+Latt[k][(l+1)%N_size]
			+Latt[(k-1)%N_size][l]
			+Latt[k][(l-1)%N_size]);

		// Metropolis step
		if (local_energy<0 || exp(-local_energy/temp)>rand())
		{
			Latt[k][l]*=(-1);
		}
		else
		{
			Latt[k][l]*=(1);	
		}	

		// Magnetization: (has issues)
		for(int m=0; m<N_size; m++)
		{
			for(int k=0; k<N_size; k++)
			{
				sum[i] = sum[i] + Latt[m][k];
			}
		}
		cout<< sum[i] <<endl;	
	}	
}