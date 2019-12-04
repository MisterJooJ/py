# from pygame import mixer
# import thorpy
import socket
import pickle

# mixer.init()
# mixer.music.load("C:\\Users\\LAN HOUSE\\Desktop\\agoravai\\fly me to the moon instrumental.mp3")
# mixer.music.play(-1)


pos = ['_', '_', '_', '_', '_', '_', ' ', ' ', ' ']
stream = []


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
        verify = 0
        if vez == 1:
            ordem = 'X'
            print('você começa')
            print('escolha uma posição de 1 à 9')
            jogada = int(input())
            update(jogada, ordem)
            sock.send(pickle.dumps(jogada))
            verify = pickle.loads(sock.recv(4096))
            if verify == 1:
                print('jogada invalida')
                continue
            jogada = pickle.loads(sock.recv(4096))
            update(jogada, 'O')
        else:
            ordem = 'O'
            print('esperando o outro jogador')
            jogada = pickle.loads(sock.recv(4096))
            update(jogada, 'X')
            print('sua vez')
            print('escolha uma posição de 1 à 9')
            jogada = int(input())
            update(jogada, ordem)
            sock.send(pickle.dumps(jogada))
            if verify == 1:
                print('jogada invalida')
                continue


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
