import aios
import time
import threading
import numpy as np

Server_IP_list = []



def main():

    Server_IP_list = aios.broadcast_func()
    
    if Server_IP_list:

        for i in range(len(Server_IP_list)):
            aios.getRoot(Server_IP_list[i])
        print('\n')

        for i in range(len(Server_IP_list)):
            aios.getMotionCtrlConfig(Server_IP_list[i], 1)
        print('\n')

        motion_controller_config_param = {
            'pos_gain' : 50,
            'vel_gain' : 0.0002,
            'vel_integrator_gain' : 0.0002,
            'vel_limit' : 400000,
            'vel_limit_tolerance' : 1.2,
        }
        for i in range(len(Server_IP_list)):
            aios.setMotionCtrlConfig(motion_controller_config_param, Server_IP_list[i], 1)
        print('\n')

        for i in range(len(Server_IP_list)):
            aios.saveConfig(Server_IP_list[i])
            # aios.rebootMotorDrive(Server_IP_list[i])

        print('\n')
        time.sleep(2)

        for i in range(len(Server_IP_list)):
            aios.getMotionCtrlConfig(Server_IP_list[i], 1)
        print('\n')




if __name__ == '__main__':
    main()
