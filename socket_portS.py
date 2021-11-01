import threading, queue
from socket import *

t = input(str('Enter host Addrese for scanning:'))
ib = input('Enter Intervall port beginn: ')
ie = input('Enter Intervall port End: ')
t_IP = gethostbyname(t)
print(f'Starting scan on host: from IP {t}')
print(f'Starting on port {ib} and ending on {ie}')

q = queue.Queue()
for i in range(int(ib),int(ie)):
    q.put(i)

def scanning():
    while not q.empty():
        i = q.get()
        s = socket(AF_INET, SOCK_STREAM)
        try: 
            c = s.connect_ex((t_IP, i))
            if c == 0:
                print(f'Open-Port: {i}')
        except:
            print('ERROR')#pass
        q.task_done()

def thread():
    for i in range(50):
        threading.Thread(target=scanning, daemon=True).start()

thread()

q.join()
