import socket
import pickle

gamers = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5555

sock.bind((host, port))
sock.listen(100)

while True:
    if gamers == 0:
        codigo = {'sit': 'funciona'}
        sockg1, addr1 = sock.accept()
        gamers += 1
        sockg1.send(pickle.dumps(codigo))
    if gamers == 1:
        codigo = {'sit': 'funciona'}
        sockg2, addr2 = sock.accept()
        gamers += 1
        sockg2.send(pickle.dumps(codigo))
