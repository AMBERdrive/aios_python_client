import aios
import time
import threading
import numpy as np
import json

Server_IP_list = []

def main():

    Server_IP_list = aios.broadcast_func() # 通过广播返回所有在线服务器的ip
    
    if Server_IP_list:

        for i in range(len(Server_IP_list)):
            aios.getRoot(Server_IP_list[i]) # 向所有server请求json数据报



if __name__ == '__main__':
    main()
