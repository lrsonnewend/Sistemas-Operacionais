#Estrita Alternância
from threading import Thread
import time

global turn

#função regiãoCritica recebe a simulação
#de processamento em 1 segundo
def regiaoCritica():
    time.sleep(1)

def processamentoA(times, delay):
    global turn
    for x in range(times):
        
        #permite a entrada na seção crítica        
        print ("Secao de Entrada A - ",x+1)

        #enquanto turn for direfente de 1, ele fica em
        #estado de espera infinita
        while (turn != 0):
            continue
        #código acessando recursos compartilhados 
        print ("Regiao Critica A")        
        regiaoCritica()

        #código executado após a saida da seção crítica
        #com o valor de turn = 1 para poder executar o
        #processamentoB
        print ("Secao de Saida A")
        turn = 1

        #código acessando recursos exclusivos
        print ("Regiao nao critica A\n")
        time.sleep(delay)    

def processamentoB(times, delay):
    global turn
    for x in range(times):
        #permite a entrada na seção crítica
        print ("Secao de Entrada B - ",x+1)

        #enquanto turn for direfente de 1, ele fica em
        #estado de espera infinita
        while (turn != 1):
            continue

        #código acessando recursos compartilhados 
        print ("Regiao Critica B")
        regiaoCritica()

        #código executado após a saida da seção crítica
        #com o valor de turn = 0 para poder executar o
        #processamentoA
        print ("Secao de Saida B")
        turn = 0

        #código acessando recursos exclusivos
        print ("Regiao nao critica B\n")
        time.sleep(delay)

#título do programa
print ("Exemplo de Estrita Aternancia")
execTimes = 10
turn = 0

#no processamento você pode passar quantas vezes que a exec e
#qual o tempo de delay para simular o efeito comboio

#variável tA recebendo os parâmetros para fazer a função
#processamentoA com tempo de delay de 1 seg
tA = Thread(target=processamentoA, args=(execTimes,1,))

#inicia a variável tA
tA.start()

#variável tB recebendo os parâmetros para fazer a função
#processamentoB com tempo de delay de 5 seg
tB = Thread(target=processamentoB, args=(execTimes,5,))

#inicia a variável tB
tB.start()
