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


    
def calcWait(t, b):
    return t - b

        


infoProcess = []

while(True):
    opcao = input('1 - FCFS\n2 - SJF\n3 - SRTF\n4 - Round Robin\n5 - Multinível\n6 - Sair\n')
    
    if opcao == '1':
        qProcess = int(input('Insira a quantidade de processos: '))

        for i in range(qProcess):
            print('P '+str(i+1))
            b = int(input('Burst: '))
            c = int(input('Tempo de chegada: '))
            proc = Processo(i, b, c)
            infoProcess.append(proc)


        print('\n')

        print('Informações dos processos:\n')
        print('Process',' Burst',' Tempo de chegada')

        count = 0
        for i in infoProcess:
            count+=1
        
            print(count,"      ", i.burst,"      ",i.tcheg)

        print('\n')

        turnAr = 0
        count= 0
        mediaWait = 0
        mediaTurnAr = 0
        for j in infoProcess:
            count+=1
            print('Process '+str(count))

            turnAr+= (j.burst - j.tcheg)

            print('TurnAround Time: '+str(turnAr))
            print('Waiting Time: ',calcWait(turnAr, j.burst))

            mediaWait+= calcWait(turnAr, j.burst)
            mediaTurnAr+= turnAr
            
            
        print('\nAVG Waiting Time: ',float(mediaWait/qProcess))
        print('AVG TurnAround Time: ', float(mediaTurnAr/qProcess))
        
        print('****************************\n')


        



    elif opcao == '2':
        pass
    
    elif opcao == '3':
        pass

    elif opcao == '4':
        pass

    elif opcao == '5':
        pass
    
    elif opcao == '6':
        break

    else:
        print('Insira uma opção válida do menu')
              
