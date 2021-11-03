import nmap

s = nmap.PortScanner()
d = {'a': ['-v -sS -sV -sC -A -O'], 'b': ['-v -sS'], 'c':['-O']}
u_ip = input('Enter IP-A: ')
s_option = '''NMAP
        1. Full scan
        2. OS Detection
        3. Syn-Ack scan
        '''
print(s_option)
el = input('Enter a number: ')
if el == '1':
    s.scan(u_ip, '1-1024', d['a'][0])  # '-v -sS -sV -sC -A -O')
    print('Scan Info: ', s.scaninfo())
    print('Protocol(s): ', s[u_ip].all_protocols())
    print("Open Port(s): ", s[u_ip]['tcp'].keys())
elif el == '2':
    op = s.scan(u_ip, arguments=d['c'][0])
    print('OS name: ',op['scan'][u_ip]['osmatch'][0]['osclass'][0]['osfamily'])
    print('Target and service detection: ',op['scan'][u_ip]['osmatch'][1])
elif el == '3':
    s.scan(u_ip, '1-1024', d['b'][0])
    print('Info: ',s.scaninfo())
    print('Protocol(s)', s[u_ip].all_protocols())
    print('Open Ports: ', s[u_ip]['tcp'].keys())
else:
    print('Error')
