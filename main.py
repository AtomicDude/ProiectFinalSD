import hashlib
import random
import socket
import struct

M = 6
#IP = '127.0.0.1'
#M = input("Insert M: ")
Network = []
Keys = []

class Data:
    def __init__(self):
        self.data = {}
    def insert_key(self, key, value):
        self.data[key] = value
    def delete_key

class FingerTable:
    def __init__(self, node_id):
        self.table = []

        for i in range(M):
            s = (node_id + pow(2,i)) % pow(2,M)
            node = None
            self.table.append([s, node])

class Node:
    def __init__(self, ip, port):
        self.Ip = ip
        self.Port = port
        self.Id = self.hash(ip + "|" + str(port))
        self.FingerTable = FingerTable(self.Id)

    def hash(self, net_add):
        digest = hashlib.sha1(net_add.encode()).hexdigest()
        digest = int(digest,16) % pow(2,M)
        return digest

def id_exists(id, Network):
    for i in Network:
        if i.Id == id:
            return True
    return False

def id_exists_returns_index(id,Network):
    for i in range(len(Network)):
        if Network[i].Id == id:
            return i
    return -1

def generate_nodes():
    while True:
        nr = int(input("Cate noduri doriti sa generati?: "))
        if nr <= pow(2, M):
            break
        print("Introduceti un numar mai mic decat " + str(pow(2, M)))
    i = 0
    while i < nr:
        ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        port = random.randint(0, 65535)
        temp_node = Node(ip,port)
        if id_exists(temp_node.Id,Network) is False:
            Network.append(temp_node)
            i += 1
    return Network

def ordonare_cresc():
    Retea_copy = []
    for i in range(0, pow(2, M)):
        if id_exists_returns_index(i, Retea) != -1:
            Retea_copy.append(Retea[id_exists_returns_index(i, Retea)])
    return Retea_copy

def generate_keys(nr):
    return 0

Retea = generate_nodes()
print("lungimea: " + str(len(Retea)))
Retea = ordonare_cresc()
for i in Retea:
    print(i.Id)