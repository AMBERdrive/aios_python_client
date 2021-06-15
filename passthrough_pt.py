import aios
import time
import threading
import numpy as np

Server_IP_list = ['192.168.5.63']
# Server_IP_list = []



def main():

    Server_IP_list = aios.broadcast_func()
    if Server_IP_list:

        for j in range(1000):
            for i in range(len(Server_IP_list)):
                start = time.time()
                aios.passthrough_pt(Server_IP_list[i], "c 1 1.123\n")
                latency = time.time() - start
                print(latency*1000)
            print('\n')
            time.sleep(0.05)





if __name__ == '__main__':
    main()
