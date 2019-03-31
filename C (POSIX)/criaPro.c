#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){

	/*cria uma variável pid do tipo pid_t*/
	pid_t pid;
	

	/*a variável pid recebe uma chamada de sistema (syscall)fork() para criar um novo processo
	P-filho (cópia do mesmo processo sendo executado)*/
	pid = fork(); 


	/*se o valor de pid for menor que 0, o programa encerra imediatamente, exibindo uma mensagem na tela
	dizendo que houve falha em criar o processo.*/
	if(pid < 0){
		
		fprintf(stderr, "Fork failed.\n");

		exit(-1);
	}

	/*Se o valor de pid for igual a 0, o comando execlp cria um novo programa, substituindo o espaço de 
	memória do processo*/
	else if(pid == 0) 
		execlp("bin/ls","ls", NULL);


	/*Caso nenhuma das condições acima seja satisfeita, o processo pai sai da fila de prontos e 
	espera até que o processo filho termine sua execução (wait()) e exiba na tela a mensagem
	de que o processo filho foi terminado.*/
	else{
		wait(NULL);
		
		printf("Child complete\n");
		
		exit(0);
	}
}
