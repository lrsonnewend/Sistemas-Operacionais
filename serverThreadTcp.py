#Servidor TCP
import socket
from threading import Thread

def conexao(con,cli):
    while True:

        #recebendo os dados em pacotes e retransmitindo-os
        msg = con.recv(1024)

        #caso não tenha mais retorno do cliente,
        #ele finaliza a conexão
        if not msg: break
        
        #imprime as mensagens enviadas pelo cliente
        print (msg)

    #finaliza a conexão    
    print ('Finalizando conexao do cliente', cli)
    con.close() 

# Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT = 5002

#variável tcp recebe a criação de um scket, usando a família
#de endereços e o tipo de socket que deseja criar
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#orig recebe o host e a porta para estabelecer a conexão
orig = (HOST, PORT)

#faz a associação do socket ao endereço do servidor
#e o numero da porta
tcp.bind(orig)

#coloca o socket no modo de servidor
tcp.listen(1)

while True:
    #estabelece a conexão com o cliente, certificando a
    #transmissão de dados (handshake)
    con, cliente = tcp.accept()

    #imprime o cliente que está conectado 
    print ('Concetado por ', cliente)

    #recebe o thread que foi criado
    t = Thread(target=conexao, args=(con,cliente,))

    #inicia o thread e exibe a mensagem enviada pelo cliente
    t.start()
