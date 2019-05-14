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
    return burst - quantum
    
        

def calcWait(t, b):
    if t < b:
        return b - t
    else:
        return t - b



def calcFCFS():
    infoProcessFCFS = []
    
    qProcess_FCFS = int(input('Insira a quantidade de processos: '))

    for i in range(qProcess_FCFS):
        print('P '+str(i+1))
        b = int(input('Burst: '))
        c = int(input('Tempo de chegada: '))
        proc = Processo(i, b, c)
        infoProcessFCFS.append(proc)

    print('\n')

    print('Informações dos processos:\n')
    print('Process',' Burst',' Tempo de chegada')

        
    for i in infoProcessFCFS:        
        print(int(i.nome+1),"      ", i.burst,"      ",i.tcheg)

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

    print('\n')

    print('Informações dos processos:\n')
    print('Process',' Burst',' Tempo de chegada')

    for k in infoProcessSJF:        
        print(int(k.nome+1),"      ", k.burst,"      ",k.tcheg)

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
    
    qProcessSRTF = int(input('Insira a quantidade de processos: '))

    for i in range(qProcessSRTF):
        print('P '+str(i+1))
        b = int(input('Burst: '))
        c = int(input('Tempo de chegada: '))
        proc = Processo(i, b, c)
        infoProcessSRTF.append(proc)
        listaBurst.append(b)
        

def calcRoundR():
    infoProcessRR = []
    
    qProcessRR = int(input('Insira a quantidade de processos: '))
    quantum = int(input('Insira o quantum de tempo :'))

    for i in range(qProcessRR):
        print('P '+str(i+1))
        b = int(input('Burst: '))
        c = int(input('Tempo de chegada: '))
        proc = Processo(i, b, c)
        infoProcessRR.append(proc)

    print('\n')

    print('Informações dos processos:\n')
    print('Process',' Burst',' Tempo de chegada')

        
    for i in infoProcessRR:        
        print(int(i.nome+1),"      ", i.burst,"      ",i.tcheg)

    print('\n')

    for j in infoProcessRR:
        j.burst = calcQ(quantum, j.burst)
        print('burst: ', j.burst)


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
              
