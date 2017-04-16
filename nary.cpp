#include"omp.h"
#include"iostream"
using namespace std;

int a[100],s,test;
int global_size,global_x,n=4;
void nary_search(int,int);
int main()
{
	int size=100,x=0;
	for(int i=0;i<size;i++)
		a[i]=i*2;
	cout<<"\nenter the no. to be searched"<<endl;
	cin>>s;
	nary_search(size,x);
}
void nary_search(int size,int x)
{
	
     cout<<size;
if(size%n==0)
n=n;
else
n=n+(size%n);

	if(size<=n)
	{
	test=0;
# pragma omp parallel num_threads(n)
		{
			int tid=omp_get_thread_num();
			if(a[global_x+tid]==s)
			{
                       cout<<"found at \n"<<global_x+tid<<endl;
				test=1;
cout<<"Global_x: "<<global_x<<endl<<tid;
			}
		}
           if(test==0)
		{
            cout<<"not found\n"<<endl;
		}
	}
	else
	{
		test=0;
#pragma omp parallel num_threads(n)
	  {
		  int tid=omp_get_thread_num();
		  cout<<"checking ("<<a[tid*size/n] <<"--"<<a[tid*size/n+size/n-1]<<")with thread "<<tid<<" on cpu "<<sched_getcpu()<< "\n"<<endl;
		  if(s>=a[tid*size/n] && s<=a[tid*size/n+size/n-1])
		  {

			 global_size=size/n; 				       global_x=tid*global_size;
			       test=1;
		  }
         }
 if(test==1) 
	nary_search(global_size,global_x);
	
 else
	cout<<"not found"<<endl;
	

	}
}


