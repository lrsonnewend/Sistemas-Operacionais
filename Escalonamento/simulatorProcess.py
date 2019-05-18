import random
import operator

class Processo(object):
    def __init__(self, nome, burst, tcheg):
        self.nome = nome
        self.burst = burst
        self.tcheg = tcheg

def setNome(nome):
    self.nome = nome

def setBurst(burst):
    self.burst = burst

def setTcheg(tcheg):
    self.tcheg = tcheg



def calcQ(quantum, burst):
    for i in burst:
        while i != quantum:
            if i != burst:
               sobraQ =  i - quantum
               i -= sobraQ
        break

def verificaBurst(listBurst, burst):
    pass    
    
        

def calcWait(t, b):
    if t < b:
        return b - t
    else:
        return t - b



def calcFCFS():
    infoProcessFCFS = []

    entrada = input('Digite o tipo de entrada: manual (M/m) arquivo (A/a): ')

    if entrada == 'm' or entrada == 'M':
        qProcess_FCFS = int(input('Insira a quantidade de processos: '))

        for i in range(qProcess_FCFS):
            print('P '+str(i+1))
            b = int(input('Burst: '))
            c = int(input('Tempo de chegada: '))
            proc = Processo(i, b, c)
            infoProcessFCFS.append(proc)

        print('\n')

        infoProcessFCFS.sort(key = operator.attrgetter("tcheg"), reverse = False)

        print('Informações dos processos:\n')
        print('Process\t','Burst\t','Tempo de chegada')

        for i in infoProcessFCFS:        
            print(int(i.nome+1),"\t", i.burst,"\t",i.tcheg)

        print('\n')

        mediaWait = 0
        mediaTurnAr = 0
        turnAr = 0
        for j in infoProcessFCFS:
           print('Process ',int(j.nome+1))
           turnAr += (j.burst - j.tcheg)
           print('TurnAround Time: ',turnAr)
           print('Waiting Time: ', calcWait(turnAr, j.burst))

           mediaWait+= calcWait(turnAr, j.burst)
           mediaTurnAr+= turnAr
                
                
        print('\nAVG Waiting Time: ',float(mediaWait/qProcess_FCFS))
        print('AVG TurnAround Time: ', float(mediaTurnAr/qProcess_FCFS))
            
        print('****************************\n')

    elif entrada == 'a' or entrada == 'A':
        arq = open('fcfs.txt')
        leituraArq = arq.read()
        tam = len(leituraArq)
        leituraArq
        for k in leituraArq:
            print(k)
        
def calcSJF():
    infoProcessSJF = []
    listaBurst = []

    qProcessSJF = int(input('Insira a quantidade de processos: '))
    
    for i in range(qProcessSJF):
        print('P '+str(i+1))
        b = int(input('Burst: '))
        c = int(input('Tempo de chegada: '))
        proc = Processo(i, b, c)
        infoProcessSJF.append(proc)
        listaBurst.append(b)

        infoProcessSJF.sort(key = operator.attrgetter("burst"), reverse = False)
        infoProcessSJF.sort(key = operator.attrgetter("tcheg"), reverse = False)

    print('\n')

    print('Informações dos processos:\n')
    print('Process\t','Burst\t','Tempo de chegada')

    for k in infoProcessSJF:        
        print(int(k.nome+1),'\t', k.burst,'\t',k.tcheg)

    print('\n')

    turnAr = 0
    mediaWait = 0
    mediaTurnAr = 0
    for j in infoProcessSJF:
        print('Process ',int(j.nome+1))
        turnAr+= (j.burst - j.tcheg)

        print('TurnAround Time: '+str(turnAr))
        print('Waiting Time: ',calcWait(turnAr, j.burst))

        mediaWait+= calcWait(turnAr, j.burst)
        mediaTurnAr+= turnAr
            
            
    print('\nAVG Waiting Time: ',float(mediaWait/qProcessSJF))
    print('AVG TurnAround Time: ', float(mediaTurnAr/qProcessSJF))
        
    print('****************************\n')



def calcSRTF():
    infoProcessSRTF = []
    listaBurst = []
    listaCheg = []
    
    qProcessSRTF = int(input('Insira a quantidade de processos: '))

    for i in range(qProcessSRTF):
        print('P '+str(i+1))
        b = int(input('Burst: '))
        c = int(input('Tempo de chegada: '))
        proc = Processo(i, b, c)
        infoProcessSRTF.append(proc)
        listaBurst.append(b)
        listaCheg.append(c)


    infoProcessSRTF.sort(key = operator.attrgetter("tcheg"), reverse = False)
    print('\n')
    
    print('Informações dos processos:\n')
    print('Process\t','Burst\t','Tempo de chegada')

    for k in infoProcessSRTF:        
        print(int(k.nome+1),'\t', k.burst,'\t',k.tcheg)

    print('\n')

    time = 0
    for i in range(len(listaBurst)):
        tempor = listaBurst[i]
        for k in range(tempor):          
            listaBurst[i] -=1
            time+=1
            
            if time in listaCheg and listaBurst[i+1] < listaBurst[i]:
                print('burst parou no ',listaBurst[i])
                print('tempo do próximo processo',time)
                tempor = listaBurst[i+1]
                print('vez do burst ',tempor)                                
            
        
    
'''def calcRoundR():
    infoProcessRR = []
    listaBurst = []
    
    qProcessRR = int(input('Insira a quantidade de processos: '))
    quantum = int(input('Insira o quantum de tempo :'))

    for i in range(qProcessRR):
        print('P '+str(i+1))
        b = int(input('Burst: '))
        c = int(input('Tempo de chegada: '))
        proc = Processo(i, b, c)
        infoProcessRR.append(proc)
        listaBurst.append(b)
    print('\n')

    print('Informações dos processos:\n')
    print('Process',' Burst',' Tempo de chegada')

        
    for i in infoProcessRR:        
        print(int(i.nome+1),"      ", i.burst,"      ",i.tcheg)

    print('\n')
    
    turnAr = 0
    mediaWait = 0
    mediaTurnAr = 0

    for j in infoProcessRR:
        while j.burst != 0:
            if j.burst != quantum:
                j.burst = caclQ(quantum, j.burst)
                turnAr += (j.burst - j.tcheg)
            else:
                break'''
                
            

while(True):
    opcao = input('1 - FCFS\n2 - SJF\n3 - SRTF\n4 - Round Robin\n5 - Multinível\n6 - Sair\n')
    
    if opcao == '1':
        calcFCFS()        

    

    elif opcao == '2':
        calcSJF() 
    
    elif opcao == '3':
        calcSRTF()
        


        
    elif opcao == '4':
        calcRoundR()

    elif opcao == '5':
        pass
    
    elif opcao == '6':
        break


    else:
        print('Insira uma opção válida do menu')
