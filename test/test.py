import unittest
import sys
import time
import numpy as np
from colorama import Fore, Back, Style
sys.path.append('../')
from aios_python_example import aios as aios

test_ip = ['192.168.102.10']

class TestAIOS(unittest.TestCase):
    # 运行类中的测试之前自动调用该类方法
    @classmethod
    def setUpClass(cls):
        print('======= test begin =======')
        cls.server_ip_list = aios.broadcast_func()
        assert(cls.server_ip_list != False)
        
    # 每个方法执行前自动执行该方法
    def setUp(self):
        print("\n======= test {} begin =======".format(self._testMethodName))
        
    def test00_disable(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.disable(ip, 1)
            self.assertTrue(res)

    def test01_enable(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.enable(ip, 1)
            self.assertTrue(res)

    def test02_trapezoidal_move(self):
        # pos_list_1 = [1000, 2000, 3000, 5000, 2000, 6000, 10000, 0, 5000, 
        #    -10000, 15000, 20000, 0]
        # delay_list_1 = [0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 1, 1, 1, 2, 2, 2, 2]
        pos_list_1 = [1000, 3000]
        delay_list_1 = [0.3, 0.3]
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            for pos, delay in zip(pos_list_1, delay_list_1):
                start = time.time()
                res = aios.trapezoidalMove(pos, True, ip, 1)
                end = time.time()
                print((end - start) * 1000)
                time.sleep(delay)
                self.assertTrue(res)
        
    def test03_get_root(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.getRoot(ip)
            self.assertTrue(res)

    def test04_get_cvp(self):
        for _ in range(5):
            for ip in self.server_ip_list:
                if ip not in test_ip:
                    continue
                
                cvp = aios.getCVP(ip, 1)
                self.assertNotEqual(len(cvp), 0)
                print("Position = %.2f, Velocity = %.0f, Current = %.4f" %
                    (cvp[0], cvp[1], cvp[2]))
            time.sleep(0.02)
            
    def test05_control_mode(self, mode = aios.ControlMode.VELOCITY_CONTROL.value):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.controlMode(
                mode, ip, 1)
            self.assertTrue(res)

    def test06_get_trap_traj(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.getTrapTraj(ip, 1)
            self.assertTrue(res)

    def test07_set_trap_traj(self):
        trap_traj_param = {
            'accel_limit' : 80000,
            'decel_limit' : 80000,
            'vel_limit' : 200000
        }
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.setTrapTraj(trap_traj_param, ip, 1)
            aios.saveConfig(ip)
            aios.getTrapTraj(ip, 1)
            self.assertTrue(res)

    def test08_get_trap_traj(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.getTrapTraj(ip, 1)
            self.assertTrue(res)

    def test09_get_motion_controller_config(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.getMotionCtrlConfig(ip, 1)
            self.assertNotEqual(len(res), 0)

    def test10_set_motion_controller_config(self):
        motion_controller_config_param = {
            'pos_gain' : 50,
            'vel_gain' : 0.0002,
            'vel_integrator_gain' : 0.0002,
            'vel_limit' : 400000,
            'vel_limit_tolerance' : 1.2,
        }
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.setMotionCtrlConfig(motion_controller_config_param, ip, 1)
            aios.saveConfig(ip)
            self.assertTrue(res)
        time.sleep(2)
        self.test09_get_motion_controller_config()

    def test11_get_motor_config(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.getMotorConfig(ip, 1)
            self.assertNotEqual(len(res), 0)

    def test12_set_motor_config(self):
        motor_param = {
            'current_lim' : 8,
            'current_lim_margin' : 5,
            'inverter_temp_limit_lower' : 90,
            'inverter_temp_limit_upper' : 120,
            'requested_current_range' : 30,
            'current_control_bandwidth' : 500,
        }
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.setMotorConfig(motor_param, ip, 1)
            aios.saveConfig(ip)
            self.assertNotEqual(len(res), 0)
        time.sleep(2)
        self.test09_get_motion_controller_config()

    def test13_get_error(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.getError(ip, 1)
            self.assertTrue(res)

    def test14_clear_error(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.clearError(ip, 1)
            self.assertTrue(res)

    def test15_ramp_mode(self):
        vel_list = [10000, 20000, 30000, 50000, -80000, -10000, 0]
        delay_list = [1, 1, 1, 1, 1, 2, 1]
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            self.test05_control_mode()
            res = aios.velRampEnable(True, ip, 1)
            self.assertTrue(res)
            for vel, delay in zip(vel_list, delay_list):
                res = aios.velRampTarget(vel, ip, 1)
                self.assertTrue(res)
                time.sleep(delay)
            self.test00_disable()
            
    def test16_set_position(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            self.test01_enable()
            res = aios.trapezoidalMove(0, False, ip, 1)
            time.sleep(3)
            self.assertTrue(res)
            for i in range(800):
                start = time.time()
                pos = np.sin(i * 0.004 * np.pi) * 20000
                aios.setPosition(pos, 0, 0, True, ip, 1)
                res = aios.receive_func()
                self.assertTrue(res)
                latency = time.time() - start
                print(latency)
                if latency > 0.2:
                    print(Fore.RED + Style.BRIGHT + str(latency))
                time.sleep(0.001)
            res = aios.trapezoidalMove(0, False, ip, 1)
            self.assertTrue(res)
            time.sleep(2)
            self.test00_disable()

    def test17_set_velocity(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.velRampEnable(False, ip, 1)
            self.assertTrue(res)
            self.test01_enable()
            res = aios.setVelocity(5000, 0, True, ip, 1)
            self.assertTrue(res)
            time.sleep(3)
            res = aios.setVelocity(-5000, 0, True, ip, 1)
            time.sleep(3)
            self.test00_disable()
            
    def test18_set_current(self):
        current = [0.5, -0.5, 0.7, -0.7, 0]
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            self.test01_enable()
            for cur in current:
                res = aios.setCurrent(cur, True, ip, 1)
                self.assertTrue(res)
                time.sleep(1)
            self.test00_disable()
            
    def test19_get_iostate(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.getIOState(ip)
            self.assertTrue(res)

    def test20_set_iostate(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            for _ in range(1):
                start = time.time()
                io_param = {
                    'PWM0_CH' : 0,
                    'PWM1_CH' : 2048,
                    'SERVO0' : 80,
                    'SERVO1' : 90
                }
                res = aios.setIOState(io_param, True, ip)
                self.assertTrue(res)

                latency = time.time() - start
                print(latency)
                print('\n')
                time.sleep(1)

                io_param = {
                    'PWM0_CH' : 65535,
                    'PWM1_CH' : 60000,
                    'SERVO0' : 170,
                    'SERVO1' : 120
                }
                aios.setIOState(io_param, True, ip)
                self.assertTrue(res)
                print('\n')
                time.sleep(5)

    def test21_get_network_setting(self):
        for ip in self.server_ip_list:
            if ip not in test_ip:
                continue
            res = aios.getNetworkSetting(ip)
            self.assertTrue(res)

    # 在每个用例执行完毕后执行该方法
    def tearDown(self):
        print("======= test {} end =======\n".format(self._testMethodName))
        

    # 在全部用例执行完毕后执行该方法
    @classmethod
    def tearDownClass(cls):
        print('======= test end =======')

if __name__ == '__main__':
    unittest.main()
