
#include<stdio.h>
#include<omp.h>
omp_lock_t w;
omp_lock_t r;
char buf[10];
int nr=0,nre=0,nwr=0;

void number()
{
	printf("\n enter the number of readers and writers : - ");
	scanf("%d%d",&nre,&nwr);
}

void initwrite()
{
	printf("\n write something : - ");
	scanf("%s", &buf);
}

void startread()
{
	omp_set_lock(&r);
	nr++;
	if(nr==1)
	{
		omp_set_lock(&w);
	}
	omp_unset_lock(&r);
}

void endread()
{
	omp_set_lock(&r);
	nr--;
	if(nr==0)
		omp_unset_lock(&w);
	omp_unset_lock(&r);
}

void startwrite()
{

	omp_set_lock(&w);
}

void endwrite()
{
	omp_unset_lock(&w);
}

void reader()
{
	startread();
	printf(" reading content : -%s\n",buf);
	endread();
}

void writer()
{
	startwrite();
	printf("overwrite something : -");
	scanf("%s",&buf);
	endwrite();
}

int main()
{
	int i,id,numthr;
	omp_set_num_threads(8);
	number();
	initwrite();
	omp_init_lock(&w);
	omp_init_lock(&r);
	#pragma omp parallel 
	{
		#pragma omp for
		for(i=0;i<(nre+nwr);i++)
		{
			if(i<nre)
				reader();

			else
				writer();
		}
	}
	return 0;
}
