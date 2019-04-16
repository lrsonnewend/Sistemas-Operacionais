#Semáfaro
from threading import Thread,Semaphore
import time

#s recebe um novo semáforo
s = Semaphore()

def regiaoCritica():
    time.sleep(1)

def processamentoA(times, delay):
    for x in range(times):
        
        print ("Secao de Entrada A - ",x+1)

        #coloca o processo que chama a operação na fila
        #de espera apropriada
        s.acquire()

        #código acessando recursos compartilhados
        print ("Regiao Critica A")        
        regiaoCritica()

        print ("Secao de Saida A")

        #remove o processo na fila de espera e o coloca
        #na fila de prontos
        s.release()

        #código acessando recursos exclusivos
        print ("Regiao nao critica A\n")
        time.sleep(delay)    

def processamentoB(times, delay):
    for x in range(times):
        
        print ("Secao de Entrada B - ",x+1)

        #coloca o processo que chama a operação
        #na fila de espera apropriada
        s.acquire()

        #código acessando recursos compartilhados
        print ("Regiao Critica B")        
        regiaoCritica()

        #remove o processo na fila de espera e
        #o coloca na fila de prontos
        print ("Secao de Saida B")
        s.release()

        #código acessando recursos exclusivos
        print ("Regiao nao critica B\n")
        time.sleep(delay)


print ("Exemplo de Semafaro")
execTimes = 5

#no processamento você pode passar quantas vezes que a exec e
#qual o tempo de delay para simular o efeito comboio

#variável tA recebe os parâmetros para fazer a função
#processamentoA
tA = Thread(target=processamentoA, args=(execTimes,1,))

#inicia processo
tA.start()

#variável tB recebe os parâmetros para fazer a função
#processamentoB
tB = Thread(target=processamentoB, args=(execTimes,5,))

#iniciar processo
tB.start()
