#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
from threading import Thread
import threading

SERVER = "127.0.0.1" # IP - адрес
PORT = 1488 # порт

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("Привет!", "UTF-8")) # отправляем сообщение

def task(): # чтобы "слушать", что отправляет сервер
    while True:
        in_data = client.recv(4096)
        print("ОТ сервера: ", in_data.decode())

def task2(): # чтобы самим вводить данные
    while True:
        out_data = input()
        client.sendall(bytes(out_data, "UTF-8"))
        print("Отправлено: ", + str(out_data))

t1 = Thread(target=task2) # т.к. должны работать одновременно, каждую функцию поместим в отдельный поток
t2 = Thread(target=task)

t1.start()
t2.start()

