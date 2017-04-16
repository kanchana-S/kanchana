#include <sys/types.h>
#include <sys/ipc.h> 
#include <sys/shm.h> 
#include<stdio.h>
char *shm,*l;
void squa(int);
int main()
{
int shmid;
key_t key;
key=5678;


shmid=shmget(key,27,IPC_CREAT | 0666);
perror("shmget");

shm=shmat(shmid,NULL,0);
l=shmat(shmid,NULL,0);
shm++;
char num=*shm;
int n=(int)num;

squa(n);
shm++;

return 0;
}

void squa(int a)
{
int no,b,c;

b=a/10;
c=a%10;

int result=b*(a+c)*10+(c*c);
printf("square of no. is  server  %d",result);

*shm=result/100;
*l=result%100;




}
