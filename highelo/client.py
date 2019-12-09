# from pygame import mixer
# import thorpy
import socket
import pickle

# mixer.init()
# mixer.music.load("C:\\Users\\LAN HOUSE\\Desktop\\agoravai\\fly me to the moon instrumental.mp3")
# mixer.music.play(-1)


pos = ['_', '_', '_', '_', '_', '_', ' ', ' ', ' ']
stream = []


def ingame(ordem):
    while True:
        print('escolha uma posição de 1 à 9')
        jogada = int(input())
        sock.send(pickle.dumps(jogada))
        verify = pickle.loads(sock.recv(4096))
        if verify == 1:
            print('jogada invalida')
            continue
        update(jogada, ordem)
        if verify == 2:
            sock.close()
            print('você ganhou')
            return verify
        if verify == 3:
            sock.close()
            print('deu velha')
            return verify
        return verify


def wait(alter):
    print('esperando o outro jogador')
    resp = pickle.loads(sock.recv(4096))
    if resp == 0:
        print('você perdeu')
        jogada = pickle.loads(sock.recv(4096))
        update(jogada, alter)
        return 0
    elif resp == 10:
        print('deu velha')
        jogada = pickle.loads(sock.recv(4096))
        update(jogada, alter)
        return 10
    update(resp, alter)
    return 1


def tab():
    print("{}|{}|{}\n"
          "{}|{}|{}\n"
          "{}|{}|{}\n"
          .format(pos[0], pos[1], pos[2], pos[3], pos[4], pos[5], pos[6], pos[7], pos[8]))


def mod():
    print("{}|{}|{}\n"
          "{}|{}|{}\n"
          "{}|{}|{}\n"
          .format(1, 2, 3, 4, 5, 6, 7, 8, 9))


def update(jogada, jogador):
    pos[jogada - 1] = jogador
    mod()
    tab()


def init(vez):
    while True:
        if vez == 1:
            v = ingame('X')
            if v == 2 or v == 3:
                break
            v = wait('O')
            if v == 0 or v == 10:
                break
        else:
            v = wait('X')
            if v == 0 or v == 10:
                break
            ingame('O')
            if v == 2 or v == 3:
                break


def gui():
    tab()
    mod()
    ordem = pickle.loads(sock.recv(4096))
    print(ordem)
    init(ordem)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6666

sock.connect((host, port))
data = pickle.loads(sock.recv(4096))
print(data['sit'])
gui()
