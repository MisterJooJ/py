import socket
import pickle
from random import randint

gamers = 0
stream = [0]
streamj1 = [0]
streamj2 = [0]
vic = 0
jogadas = 0
win_condicion = [[0, 1, 2, 3],
                 [0, 4, 5, 6],
                 [0, 7, 8, 9],
                 [0, 1, 4, 7],
                 [0, 2, 5, 8],
                 [0, 3, 6, 9],
                 [0, 1, 5, 9],
                 [0, 3, 5, 7]]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6666

sock.bind((host, port))
sock.listen(100)


def final(mov):
    flag = 0
    for element in win_condicion:
        inter = list(set(element).intersection(mov))
        lar = len(inter)
        print(inter)
        if lar == 4:
            return 2

    return 0


def exe(p1, p2, ver, jstream):
    global jogadas
    global vic
    while ver == 1:
        jogada = pickle.loads(p1.recv(4096))
        ver = verify(jogada, jstream)
        p1.send(pickle.dumps(ver))
        if ver == 2:
            vic = 1
            p2.send(pickle.dumps(0))
        if jogadas == 9:
            vic = 1
            p2.send(pickle.dumps(10))
    p2.send(pickle.dumps(int(jogada)))


def msg_player(player1, player2):
    player1.send(pickle.dumps(1))
    player2.send(pickle.dumps(2))
    return player1, player2


def verify(jog, jstream):
    global jogadas
    res = 0
    if str(jog).isalpha():
        res = 1
    elif int(jog) < 1 or int(jog) > 9:
        res = 1
    elif int(jog) in stream:
        res = 1
    else:
        stream.append(int(jog))
        jstream.append(int(jog))
        res = final(jstream)
        jogadas += 1
    if jogadas == 9:
        return 3
    return res


def game_init():
    global vic
    ordem = randint(1, 2)
    if ordem == 1:
        print('jogador1 começa')
        p1, p2 = msg_player(sockg1, sockg2)
    else:
        print('jogador2 começa')
        p1, p2 = msg_player(sockg2, sockg1)
    while vic == 0:
        ver = 1
        exe(p1, p2, ver, streamj1)
        if vic == 1:
            break
        exe(p2, p1, ver, streamj2)


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
        if vic == 1:
            break
