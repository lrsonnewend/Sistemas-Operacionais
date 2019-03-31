#Cliente TCP
import socket
# Endereco IP do Servidor
SERVER = '127.0.0.1'
# Porta que o Servidor esta escutando
PORT = 5002

#variável tcp recebe a criação de um scket, usando a família
#de endereços e o tipo de socket que deseja criar
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#dest recebe o server e a porta para estabelecer a conexão
dest = (SERVER, PORT)

#faz a conexão com o conteúdo estabelecido com o servidor e a porta
tcp.connect(dest)

print ('Para sair use CTRL+X\n')

#pega a mensagem passada pelo cliente
msg = input()

#enquanto a entrada do teclado for diferente de CTRL+X, ele envia
#a mensagem para o servidor e fica em modo bloqueado esperando outra
#mensagem ser enviada
while msg != '\x18':
    tcp.send (msg.encode())
    msg = input()

#finaliza a conexão quando é dada a entrada CTRL+X
tcp.close()
