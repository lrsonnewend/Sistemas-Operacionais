#Servidor TCP
import socket
# Endereco IP do Servidor
HOST = '' #pega o IP do computador automaticamente
# Porta que o Servidor vai escutar
PORT = 5002

#criando um novo socket, usando a família de
#endereços e tipo de socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#variável orig recebe o endereço IP pego automaticamente
#e a porta para fazer a conexão
orig = (HOST, PORT)


#associa o socket ao endereço do servidor e o número da porta
tcp.bind(orig)

#coloca o socket no modo de serdiror
tcp.listen(1)
while True:
    #numa condição infinita,espera por uma conexão de entrada
    #para começar a comunicação e então exibir a mensagem dizendo
    #o endereço de quem está conectado.
    con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    while True:
        #recebendo os dados em pacotes e retransmitindo-os
        msg = con.recv(1024)

        #caso não tenha mais retorno do cliente, ele fica
        #em modo de espera
        if not msg:
            break
        print(msg)

    #sai da condição while quando a entrada do teclado for
    #CTRL+X
    print ('Finalizando conexao do cliente', cliente)
    
#desfaz a conexão com o cliente
con.close()
