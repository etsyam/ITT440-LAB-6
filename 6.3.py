import socket

ClientSocket = socket.socket()
host = '192.168.56.102'
port = 8886

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
    print('Connected!!')
except socket.error as ex:
    print(str(ex))

Response = ClientSocket.recv(1024).decode() 
print(Response)

while True:
    print (' 1 - Logarithmic \n 2 - Square Root \n 3 - Exponential \n 4 - Terminate')
    Input = input('\nChoose a mathematical function : ')
    
    if Input == '1':
        option = "log"
        value = input('Value : ')
        l = option + '.' + value
        ClientSocket.send(str.encode(l))
        
    elif Input == '2':
        option = "sq"
        value = input('Value : ')
        s = option + '.' + value
        ClientSocket.send(str.encode(s))
        
    elif Input == '3':
        option = "exp"
        value = input('Value : ')
        e = option + '.' + value
        ClientSocket.send(str.encode(e))

    elif Input == "4":
        option = "ter"
        ClientSocket.send(str.encode(option))
        print ('Thank you!! \n')
        ClientSocket.close()
    else :
        print ('Invalid funtion! Try Again \n')
        
    Response = ClientSocket.recv(1024)
    print(Response.decode())

ClientSocket.close()
