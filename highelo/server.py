import socket
import pickle
from random import randint

gamers = 0
stream = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5555

sock.bind((host, port))
sock.listen(100)


def msg_player(player1, player2):
    player1.send(pickle.dumps(1))
    player2.send(pickle.dumps(2))
    return player1, player2


def game_init():
    ordem = randint(1, 2)
    if ordem == 1:
        print('jogador1 começa')
        p1, p2 = msg_player(sockg1, sockg2)
    else:
        print('jogador2 começa')
        p1, p2 = msg_player(sockg2, sockg1)
    while True:
        print(' ')
        jogada = pickle.loads(p1.recv(4096))
        stream.append(jogada)
        p2.send(pickle.dumps(jogada))
        jogada = pickle.loads(p2.recv(4096))
        stream.append(jogada)
        p1.send(pickle.dumps(jogada))


while True:
    if gamers == 0:
        codigo = {'sit': 'funciona'}
        sockg1, addr1 = sock.accept()
        print('jogador 1 conectado')
        gamers += 1
        sockg1.send(pickle.dumps(codigo))
    if gamers == 1:
        codigo = {'sit': 'funciona'}
        sockg2, addr2 = sock.accept()
        print('jogador 2 conectado')
        gamers += 1
        sockg2.send(pickle.dumps(codigo))
        game_init()
