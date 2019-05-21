import random
import operator

class Processo(object):
    def __init__(self, nome, burst, tcheg, prioridade, q):
        self.nome = nome
        self.burst = burst
        self.tcheg = tcheg
        self.prioridade = prioridade
        self.q = q

def setNome(nome):
    self.nome = nome

def setBurst(burst):
    self.burst = burst

def setTcheg(tcheg):
    self.tcheg = tcheg

def setPrioridade(prioridade):
    self.prioridade = prioridade

def setQ(q):
    self.q = q




def calcQ(quantum, burst):
    for i in burst:
        while i != quantum:
            if i != burst:
               sobraQ =  i - quantum
               i -= sobraQ
        break



def verificaBurst(listBurst, burst):
    pass    
    



def leArq(file):
    listaArquivo = []
    arq = open(file)
    line = arq.readline()
    while line:
        proc = line.split("&")[0]
        proc = proc.split(";")
        nome = proc[0].split("@")[1]
        burst = int(proc[1])
        tcheg = int(proc[2])
        pri = int(proc[3])
        quantum = int(proc[4])
        #print(nome, burst, tche, pri, quant)
        proc = Processo(nome, burst, tcheg, pri, quantum)
        listaArquivo.append(proc)
        line = arq.readline()

    return listaArquivo



def calcWait(t, b):
    if t < b:
        return b - t
    else:
        return t - b


def imprimiInfo(lista):
    turnAr = 0
    mediaWait = 0
    mediaTurnAr = 0

    for i in lista:
        turnAr += (i.burst - i.tcheg)
                
        print(i.nome,"\t", i.burst,"\t",i.tcheg,"\t\t\t",turnAr,"\t\t",calcWait(turnAr,i.burst))
                
        mediaWait+= calcWait(turnAr, i.burst)
        mediaTurnAr+= turnAr

    print('\n')
                              
    print('\nAVG Waiting Time: ',float(mediaWait/len(lista)))
    print('AVG TurnAround Time: ', float(mediaTurnAr/len(lista)))             
    print('****************************\n')

    
    

def calcFCFS():
    infoProcessFCFS = []

    while True:
        entrada = input('Digite o tipo de entrada: manual (M/m) arquivo (A/a): ')
      

        if entrada == 'm' or entrada == 'M':
            qProcess_FCFS = int(input('Insira a quantidade de processos: '))

            for i in range(qProcess_FCFS):
                print('P '+str(i+1))
                b = int(input('Burst: '))
                c = int(input('Tempo de chegada: '))
                pr = 0
                q = 0
                proc = Processo(i, b, c, pr, q)
                infoProcessFCFS.append(proc)

            print('\n')

            infoProcessFCFS.sort(key = operator.attrgetter("tcheg"), reverse = False)

            mediaWait = 0
            mediaTurnAr = 0
            turnAr = 0
            
            print('Informações dos processos:\n')
            print('Process\t','Burst\t','Tempo de chegada\t','TurnAround\t','Wait Time')
            imprimiInfo(infoProcessFCFS)
            break

        elif entrada == 'a' or entrada == 'A':
            arquivoFCFS = []
            arquivoFCFS = leArq('fcfs.txt')
            print('\n')

            arquivoFCFS.sort(key = operator.attrgetter("tcheg"), reverse = False)

            mediaWait = 0
            mediaTurnAr = 0
            turnAr = 0

            print('Informações dos processos:\n')
            print('Process\t','Burst\t','Tempo de chegada\t','TurnAround\t','Wait Time')
            imprimiInfo(arquivoFCFS)
            break

        else:
            print('Entrada inválida!')
                   
                

            
def calcSJF():
    infoProcessSJF = []
    listaBurst = []

    while True:
        entrada = input('Digite o tipo de entrada: manual (M/m) arquivo (A/a): ')

        if entrada == 'm' or entrada == 'M':
            qProcessSJF = int(input('Insira a quantidade de processos: '))
            
            for i in range(qProcessSJF):
                print('P '+str(i+1))
                b = int(input('Burst: '))
                c = int(input('Tempo de chegada: '))
                p = 0
                q = 0
                proc = Processo(i, b, c, p, q)
                infoProcessSJF.append(proc)
                listaBurst.append(b)

                infoProcessSJF.sort(key = operator.attrgetter("burst"), reverse = False)
                infoProcessSJF.sort(key = operator.attrgetter("tcheg"), reverse = False)

            print('\n')

           

            print('Informações dos processos:\n')
            print('Process\t','Burst\t','Tempo de chegada\t','TurnAround\t','Wait Time')
            imprimiInfo(infoProcessSJF)
            break

        elif entrada == 'A' or entrada == 'a':
            arquivoSJF = []
            arquivoSJF = leArq('fcfs.txt')
            print('\n')

            arquivoSJF.sort(key = operator.attrgetter("burst"), reverse = False)
            arquivoSJF.sort(key = operator.attrgetter("tcheg"), reverse = False)

            mediaWait = 0
            mediaTurnAr = 0
            turnAr = 0

            print('Informações dos processos:\n')
            print('Process\t','Burst\t','Tempo de chegada\t','TurnAround\t','Wait Time')
            imprimiInfo(arquivoSJF)
            break

        else:
            print('Entrada inválida!')
            



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
   
    for i in infoProcessSRTF:
        while(i.burst != 0):
            i.burst-=1
            print(i.burst)
            

        if i.burst == 0:
            print('acabou')
            
            
    '''for i in range(len(listaBurst)):
        tempor = listaBurst[i]
        for k in range(tempor):          
            listaBurst[i] -=1
            time+=1
            
            if time in listaCheg and listaBurst[i+1] < listaBurst[i]:
                print('burst parou no ',listaBurst[i])
                print('tempo do próximo processo',time)
                tempor = listaBurst[i+1]
                print('vez do burst ',tempor)
                break'''

                
                
            
        
    
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
