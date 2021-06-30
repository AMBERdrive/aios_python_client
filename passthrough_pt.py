import aios
import time
import threading
import numpy as np
import matplotlib.pyplot as plt

Server_IP_list = ['192.168.5.63']
# Server_IP_list = []
latency_list = []
pos_cmd_list = []
pos = []
vel = []
tor = []

time_range = 3000

def main():

    Server_IP_list = aios.broadcast_func()
    if Server_IP_list:
        for j in range(time_range):
            w = j*0.01/time_range
            pos_cmd = np.sin(j*w*np.pi)*0.3
            pos_cmd_list.append(pos_cmd)
            for i in range(len(Server_IP_list)):
                start = time.time()
                # aios.passthrough_pt(Server_IP_list[i], "p 1.23743 3.28342 28.28374")
                feedback = aios.passthrough_pt_bin(Server_IP_list[i], 0x0c, pos_cmd, 0, 0)
                pos.append(feedback[0])
                vel.append(feedback[1]/15)
                tor.append(feedback[2])
                print(feedback)
                latency = (time.time() - start)*1000
                latency_list.append(latency)
                print(latency)
            print('\n')
            # time.sleep(0.002)
    plt.plot(pos)
    plt.plot(pos_cmd_list)
    plt.plot(vel)
    plt.plot(tor)
    plt.plot(latency_list)
    plt.ylabel('list')
    plt.show()





if __name__ == '__main__':
    main()
