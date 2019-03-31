//para compilar -> gcc -pthread -o nomeArquivo nomeArquivo.c

#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#define numberThread  10

/*esta função imprime o identificador do thread e sai.*/
void *print_ola_mundo(void *tid){
	printf("Hello World. Greetings from thread %d\n",tid);
	pthread_exit(NULL);
}


/*o programa principal cira 10 threads e sai*/
int main(int argc, char argv[]){

	/*cria um vetor threads do tipo pthread_t
	pthread_t é utilizado para identificar um encadeamento e utilizado em chamadas
	de função que precisam de um identificador de thread*/
	pthread_t threads[numberThread];

	int status, i;

	for (i = 0; i < numberThread; i++){
		/*imprime o índice i*/
		printf("Main here. Creating thread %d\n",i);

		/*a variável status recebe um novo thread no processo de chamada
		passando um identificador de thread, NULL (parâmetro padrão), uma
		função para imprimir thread e um ponteiro.*/
		status = pthread_create(&threads[i], NULL, print_ola_mundo, (void *)i);

		/*o retorno de status precisa ser 0 para que possa ser o thread possa ser criado*/
		if (status != 0){
			printf("ops. pthread_create returned error code %d\n",status);
			exit(-1);
		}
	}

	exit(NULL);
}