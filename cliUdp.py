#Cliente UDP
import socket

# Endereco IP do Servidor
SERVER = '127.0.0.1'

# Porta que o Servidor esta escutando
PORT = 5002

#criando um novo socket, usando a família de
#endereços e tipo de socket 
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#variável dest recebe o endereço IP do servidor
#e a porta para fazer a conexão 
dest = (SERVER, PORT)

print ('Para sair use CTRL+X\n')

#já com a conexão feita, enquanto a mensagem for
#diferente de CTRL+X, o servidor vai receber mensagem
#sem precisar verificar se está tudo ok entre a conexão
#de SERVERE e PORT
msg = input()
while msg != '\x18':
    udp.sendto (msg.encode(), dest)
    msg = input()

#termina a conexão quando é dado o comando CTRL+X
udp.close()
