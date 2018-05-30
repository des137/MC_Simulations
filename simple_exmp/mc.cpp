// -------Monte Carlo evaluation of pi-------
// By Amol Deshmukh, The City College of New York, 18 April 2018.

#include<iostream>
#include<ctime>
#include<cstdlib>

using namespace std;

int main()
{
	int N=100000;
	double a[N],b[N],c[N];
	srand( (unsigned)time( NULL ));
	for (int i = 0; i < N; ++i)
	{
		a[i]= ((double)rand() / (RAND_MAX));
		b[i]= ((double)rand() / (RAND_MAX));
		c[i]=a[i]*a[i]+b[i]*b[i];
		if (c[i]<1)
		{
			c[i]=1;
		}
		else
		{
			c[i]=0;
		}
	}
	double sum=0;
	for(int i=0;i<N;i++)
	{
	sum=sum+c[i];
	}
	double l=sum/N*4;
	std::cout<< l <<endl;
}
