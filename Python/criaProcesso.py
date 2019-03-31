import os

#cria um processo filho
pid = os.fork() 

#declarando variável param para ser usada como
#parâmetro na função execlp()
param = 1

#se o valor da variável pid for menor que 0, ele
#emite uma mensagem de erro na tela e fecha o programa
if(pid < 0):
    print('Falha ao criar processo.')
    os._exit(-1)

#se o valorda variável pid for igual a 0 (p-filho), o
#comando execlp cria um novo processo (gedit) e recebe
#o conteúdo da variável como parâmetro
elif(pid == 0):
    os.execlp('gedit', str(param))

#caso nenhuma das condições acima sejam satisfeitas,
#o processo pai espera até a conclusão do processo
#filho e, depois disso, ele emite uma mensagem dizendo
#que o processo filho foi encerrado.
else:
    os.wait()
    print('Processo filho completo.')
