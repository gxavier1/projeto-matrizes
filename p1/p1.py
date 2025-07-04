import socket
import time
import numpy as np
import pickle

HOST = '192.168.128.8'  # ← Substitua pelo IP real da máquina onde estará o p2
PORT = 6000

n = int(input("Digite o tamanho da matriz quadrada: "))
matriz = np.random.randint(1, 10, (n, n))
start_time = time.time()

# Empacota a matriz com o tempo
pacote = {
    'matriz': matriz,
    'start_time': start_time
}

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))
tcp.send(pickle.dumps(pacote))
tcp.close()
