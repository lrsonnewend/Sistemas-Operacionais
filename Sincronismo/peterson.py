#Solucao Peterson
from threading import Thread
import time

global turn #indica de quem é a vez de entrar na seção crítica
global i, j
global flag #indica se um processo está pronto para entrar na seção crítica

#função regiãoCritica recebe a simulação
#de processamento em 1 segundo
def regiaoCritica():
    time.sleep(1)

def processamentoA(times, delay):
    global turn, i, j, flag
    for x in range(times):

        #permite a entrada na seção crítica
        print ("Secao de Entrada A - ",x+1)

        #estado do processo Pi está pronto
        flag[i] = True

        #indicando de quem é a vez de entrar na seção crítica
        turn = j

        #enquanto as duas condições forem verdadeiras, ele fica
        #em estado de espera infinita
        while (flag[j] and turn == j):
            continue

        #código acessando recursos compartilhados
        print ("Regiao Critica A")
        regiaoCritica()

        #código executado após a saída da seção crítica
        print ("Secao de Saida A")

        #Pi dá a vez para processamentoB ser executado
        flag[i] = False
        print ("Regiao nao critica A\n")
        time.sleep(delay)    

def processamentoB(times, delay):
    global turn, i, j, flag
    for x in range(times):
        print ("Secao de Entrada B - ",x+1)
        flag[j] = True
        turn = i        
        while (flag[i] and turn == i):
            continue
        print ("Regiao Critica B")        
        regiaoCritica()
        print ("Secao de Saida B")
        flag[j] = False
        print ("Regiao nao critica B\n")
        time.sleep(delay)


print ("Exemplo de Solucao de Peterson")
execTimes = 5
turn = 0
i = 0
j = 1
flag = []
flag.append(False)
flag.append(False)

#no processamento você pode passar quantas vezes que a exec e
#qual o tempo de delay para simular o efeito comboi
tA = Thread(target=processamentoA, args=(execTimes,1,))
tA.start()
tB = Thread(target=processamentoB, args=(execTimes,5,))
tB.start()
