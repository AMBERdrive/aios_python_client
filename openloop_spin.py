import aios
import time
import threading
import numpy as np

Server_IP_list = ['192.168.2.40']
# Server_IP_list = []



def main():

    Server_IP_list = aios.broadcast_func()
    if Server_IP_list:
        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.current 2\n")
        print('\n')

        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.finish_on_vel 0\n") 
        print('\n')

        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.finish_on_distance 1\n") 
        print('\n')

        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.finish_distance 100000000\n") # 1600
        print('\n')

        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.vel 16000\n") # 1600
        print('\n')

        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.accel 400\n") # 400
        print('\n')

        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.requested_state 9\n")
        print('\n')

        # time.sleep(15)

        # for i in range(len(Server_IP_list)):
        #     aios.passthrough(Server_IP_list[i], "w axis1.requested_state 1\n")
        # print('\n')


if __name__ == '__main__':
    main()