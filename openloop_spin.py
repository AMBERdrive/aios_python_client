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
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.current 5\n")
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.finish_on_vel 0\n") 
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.finish_on_distance 1\n") 
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.finish_distance 800\n") # 1600
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.vel 320\n") # 1600
            aios.passthrough(Server_IP_list[i], "w axis1.config.general_lockin.accel 400\n") # 400
        print('\n')

        # for i in range(len(Server_IP_list)):
        #     aios.passthrough(Server_IP_list[i], "r axis1.config.general_lockin.current\n")
        #     aios.passthrough(Server_IP_list[i], "r axis1.config.general_lockin.finish_on_vel\n") 
        #     aios.passthrough(Server_IP_list[i], "r axis1.config.general_lockin.finish_on_distance\n") 
        #     aios.passthrough(Server_IP_list[i], "r axis1.config.general_lockin.finish_distance\n")
        #     aios.passthrough(Server_IP_list[i], "r axis1.config.general_lockin.vel\n")
        #     aios.passthrough(Server_IP_list[i], "r axis1.config.general_lockin.accel\n")
        # print('\n')

        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.requested_state 9\n")
        print('\n')

        time.sleep(5)

        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w axis1.requested_state 1\n")
        print('\n')


if __name__ == '__main__':
    main()