#Servidor UDP
import socket
#Endereco IP do Servidor (pega automaticamente)
HOST = ''
# Porta que o Servidor vai escutar
PORT = 500

#criando um novo socket, usando a família de
#endereços e tipo de socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#variável orig recebe o endereço IP pego automaticamente
#e a porta para fazer a conexão
orig = (HOST, PORT)

#associa o socket ao endereço do servidor e o número da porta
udp.bind(orig)

while True:
    #recebe os dados e exibe no terminal
    msg, cliente = udp.recvfrom(1024) #(1024)-> tamanho do buffer
    print (cliente, msg)
    
#encerra a conexão quando o terminal for fechado
udp.close()
