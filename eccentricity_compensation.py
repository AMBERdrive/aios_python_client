import aios
import time
import threading
import numpy as np
import matplotlib.pyplot as plt

Server_IP_list = ['192.168.2.40']
# Server_IP_list = []
count_in_cpr_list = []
shadow_count_list = []
theta_ref_list = []

cpr = 4000
theta_ref = 0
NPP = 21
n = 128*NPP                                                    # number of positions to be sampled per mechanical rotation.  Multiple of NPP for filtering reasons (see later)
n2 = 4                                                         # increments between saved samples (for smoothing motion)
delta = 2*np.pi*NPP/(n*n2)                                     # change in angle between samples
error_f = []
error_b = []
raw_f = []
raw_b = []




def main():

    Server_IP_list = aios.broadcast_func()
    if Server_IP_list:

        for i in range(len(Server_IP_list)):
            direction = aios.getDirection(Server_IP_list[i])

        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.requested_state 12\n")  # 7
        print('\n')

        for j in range(len(Server_IP_list)):
            aios.setThetaRef(Server_IP_list[j], 0)
        time.sleep(1)

        global theta_ref
        global error_f

        # rotate forwards
        for i in range(n):
            for j in range(n2):
                theta_ref = theta_ref + delta
                start = time.time()
                for k in range(len(Server_IP_list)):
                    rx_list = aios.setThetaRef(Server_IP_list[k], theta_ref)
                    count_in_cpr = rx_list[0]
                    shadow_count = rx_list[1]
                latency = time.time() - start
                print(latency*1000)
                # time.sleep(0.002)
            theta_ref_count = (theta_ref*cpr/(2*np.pi*NPP))
            theta_ref_list.append(theta_ref_count)
            raw_f.append(count_in_cpr)
            shadow_count_list.append(shadow_count)
            print(count_in_cpr, shadow_count)
            error_f.append(theta_ref_count - direction * shadow_count)

        i = 0
        j = 0
        # rotate backwards
        for i in range(n):
            for j in range(n2):
                theta_ref = theta_ref - delta
                start = time.time()
                for k in range(len(Server_IP_list)):
                    rx_list = aios.setThetaRef(Server_IP_list[k], theta_ref)
                    count_in_cpr = rx_list[0]
                    shadow_count = rx_list[1]
                latency = time.time() - start
                print(latency*1000)
                # time.sleep(0.002)
            theta_ref_count = (theta_ref*cpr/(2*np.pi*NPP))
            theta_ref_list.append(theta_ref_count)
            raw_b.append(count_in_cpr)
            shadow_count_list.append(shadow_count)
            # print(count_in_cpr, shadow_count)
            error_b.append(theta_ref_count - direction * shadow_count)



        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.requested_state 1\n")
        print('\n')

        np.save('error_f.npy',error_f)  
        np.save('error_b.npy',error_b)
        np.save('raw_f.npy',raw_f)  
        np.save('raw_b.npy',raw_b) 
        np.save('direction.npy',direction)

        # print(theta_ref_list)
        # print(shadow_count_list)
        print(error_f)

        # error = [ref_distance_list[i] - count_in_cpr_list[i] for i in range(len(count_in_cpr_list))]
        plt.plot(raw_f + raw_b)
        # plt.plot(shadow_count_list)
        plt.plot(error_f + error_b)
        # plt.plot(error_b)
        plt.ylabel('error_f_b')
        plt.show()



if __name__ == '__main__':
    main()