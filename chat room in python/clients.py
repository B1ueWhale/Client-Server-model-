import socket
import threading

nickname = input('choose a nickname:')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 58555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An Error Occurred ")')
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_threads = threading.Thread(target=receive)
receive_threads.start()

writeThreads = threading.Thread(target=write)
print("hello")
writeThreads.start()