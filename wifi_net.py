import subprocess, time 

def w_c_b():
    subprocess.call('nmcli dev status', shell=True)
    i = input('Press "Enter" to continue... ')
    if i == '': time.sleep(1)

def e_c():
    subprocess.call('nmcli general status', shell=True)
    i = input('Press "Enter" to continue... ')
    if i == '': time.sleep(1)

def a_c():
    subprocess.call('nmcli connection show --active', shell=True)
    i = input('Press "Enter" to continue... ')
    if i == '': time.sleep(1)

def t_t():
    subprocess.call('nmcli device show | head -10', shell=True)
    i = input('Press "Enter" to continue... ')
    if i == '': time.sleep(1)

def wifi_list():
    subprocess.call('nmcli dev wifi list', shell=True)
    i = input('Press "Enter" to continue... ')
    if i == '': time.sleep(1)

def elecc():
    while 1:
        s = ''' WIFI_NET
            1. System Wifi connections and its bridge
            2. Type of enabled connection 
            3. Active network connections and its assigned IDs 
            4. Top ten lines of network devices
            5. Comprehensive List of wifi connections
            6. Exit
            '''
        print(s)
        u = int(input("Enter a number and press 'Enter':  "))
        try:        
            if u == 6:
                break
            if u == 1:w_c_b()
            elif u == 2:e_c()                
            elif u==3:a_c()
            elif u==4:t_t()
            elif u==5:print('Press "q" to exit'),wifi_list()
            else:print('Try again!\n')
        except:print('Error')

elecc()