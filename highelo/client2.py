# from pygame import mixer
# import thorpy
import socket
import pickle

# mixer.init()
# mixer.music.load("C:\\Users\\LAN HOUSE\\Desktop\\agoravai\\fly me to the moon instrumental.mp3")
# mixer.music.play(-1)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5555

sock.connect((host, port))
data = pickle.loads(sock.recv(4096))
print(data['sit'])
input()
