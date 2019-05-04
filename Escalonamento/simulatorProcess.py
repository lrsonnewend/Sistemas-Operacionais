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

infoProcess = []

opcao = input('1 - FCFS\n2 - SJF\n3 - SRTF\n4 - Round Robin\n5 - Multinível\n')

if opcao == '1':
    qProcess = int(input('Insira a quantidade de processos: '))

    for i in range(qProcess):
        b = int(input('Burst: '))
        c = int(input('Tempo de chegada: '))
        proc = Processo(i, b, c)
        infoProcess.append(proc)


print('\n')
print('Informações dos processos:\n')
print('Process',' Burst',' Tempo de chegada')

for i in infoProcess:
    print(i.nome,"      ", i.burst,"      ",i.tcheg)
