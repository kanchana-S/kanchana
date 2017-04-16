#include <sys/types.h>
#include <sys/ipc.h> 
#include <sys/shm.h> 
#include<stdio.h>

int main()
{
int shmid,no;
key_t key;
key=5678;
char *shm,*l;

shmid=shmget(key,27,0666);

shm=shmat(shmid,NULL,0);
l=shmat(shmid,NULL,0);
printf("enter no ");
scanf("%d",&no);
char n=(char)no;
shm++;
*shm=n;
sleep(10);
shm++;
int result=(*shm)*100+ (*l);
printf("square of no. is   %d",result);

return 0;
}

