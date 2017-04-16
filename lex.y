%{
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
void * scanner;
FILE *f, *t;
#define YYSTYPE int
%}
%pure-parser
%lex-param {void * scanner}
%parse-param {void * scanner}
%start list
%token NUMBER
%left '+' '-'
%left '*' '/' '%'
%left UMINUS 
%union {int i;}
%%

list:	                   
        |
        list stat '\n'
        |
        list error '\n'{ yyerrok; }
        ;

stat:   expr { printf("%d\n",$1);}
        ;
        
expr:   '(' expr ')'{ $$ = $2; }
        |
        expr '*' expr { $$ = $1 * $3; }
        |
        expr '/' expr { $$ = $1 / $3; }
        |
        expr '+' expr { $$ = $1 + $3; }
        |
        expr '-' expr { $$ = $1 - $3; }
        |
        '-' expr %prec UMINUS { $$ = -$2; }
	|
	    NUMBER
        ;        
%%

void* scanfunc(void * cnt)
{
    t=fopen("temp.txt","r");
    yylex_init(&scanner);
    yyset_in(t,scanner);
	yyparse(scanner);
    yylex_destroy(scanner);
    fclose(t);
}

main(int argc, char *argv[])
{
	if(argc!=2)
	{
		printf("Incorrect parameters!\n");
		return -1;
	}
	f=fopen(argv[1],"r");
	if(!f)
	{
		printf("File cannot be opened!\n");
		return -1;
	}
	pthread_t threads[10];
	int cnt=0,j=0;
	size_t n=100;
	char *s=malloc(n);
	while(!feof(f))
	{ 
	    getline(&s,&n,f);
	    t=fopen("temp.txt","w+");
       	    fprintf(t, "%s", s);
            fclose(t);
	    pthread_create(&threads[cnt], NULL, scanfunc, NULL);
	    sleep(1);
	    cnt++;
    }

    for(j=0;j<cnt;j++)
        pthread_join(threads[j],NULL);
}

yyerror()
{
	printf("Error!\n");
}

yywrap()
{
	return(1);
}
