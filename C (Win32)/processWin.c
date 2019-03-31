#include <stdio.h>
#include <windows.h>

int main(VOID)
{
	/*Estruturas do Windows*/
	STARTUPINFO si; 
	PROCESS_INFORMATION pi;
	
	/*Deixa o valor dos ponteiros das variáveis como 0*/
	ZeroMemory(&si, sizeof(si));

	/*cb -> variável membro do windows utilizada para 
	definir o tamanho de uma estrutura*/
	si.cb = sizeof(si); 

	/*Deixa o valor dos ponteiros das variáveis como 0*/
	ZeroMemory(&pi, sizeof(pi));
	
	
	/*Criando um processo filho (paint)
	Caso dê erro, exibe uma mensagem na tela e */
	if (!CreateProcess(NULL,"C:\\WINDOWS\\systemd32\\mspaint.exe",NULL,NULL,FALSE,0,NULL,NULL,&si,&pi))
	{
		printf("Create process failed %s", stderr);
		return -1;
	}
	
	
	/*Assim que o processo for finalizado, ele exibe a
	mensagem de "Child complete na tela."*/
	WaitForSingleObject(pi.hProcess, INFINITE);
	printf("Child complete");
	
	/*Fechando as janelas do processo e seu respectivos threads*/
	CloseHandle(pi.hProcess);
	CloseHandle(pi.hThread);
}