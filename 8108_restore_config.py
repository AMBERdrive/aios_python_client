import aios
import time
import threading
import numpy as np

Server_IP_list = ['192.168.5.205']



def main():

    Server_IP_list = aios.broadcast_func()
    if Server_IP_list:


        for i in range(len(Server_IP_list)):
            aios.passthrough(Server_IP_list[i], "w config.dc_bus_undervoltage_trip_level 10.0\n")
            aios.passthrough(Server_IP_list[i], "w config.dc_bus_overvoltage_trip_level 55.0\n")
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.pre_calibrated 1\n")
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.pole_pairs 21\n")
            aios.passthrough(Server_IP_list[i], "w axis1.encoder.config.bandwidth 2000\n")
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.direction -1\n")
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.calibration_current 6\n") 
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.resistance_calib_max_voltage 4.0\n")
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.phase_inductance 0.00010607676085783169\n")
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.phase_resistance 0.2877658009529114\n")
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.torque_constant 1.0\n")
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.current_lim 15.0\n") 
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.current_lim_margin 4.0\n")   
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.requested_current_range 30.0\n")  
            aios.passthrough(Server_IP_list[i], "w axis1.motor.config.current_control_bandwidth 500.0\n")
            aios.passthrough(Server_IP_list[i], "w axis1.fet_thermistor.temp_limit_lower 80.0\n")
            aios.passthrough(Server_IP_list[i], "w axis1.fet_thermistor.temp_limit_upper 90.0\n")

            aios.passthrough(Server_IP_list[i], "w axis1.controller.config.pos_gain 60.0\n")
            aios.passthrough(Server_IP_list[i], "w axis1.controller.config.vel_gain 0.03999999910593033\n")
            aios.passthrough(Server_IP_list[i], "w axis1.controller.config.vel_integrator_gain 0.03999999910593033\n")
            aios.passthrough(Server_IP_list[i], "w axis1.controller.config.vel_limit 40.0\n")
            aios.passthrough(Server_IP_list[i], "w axis1.controller.config.vel_limit_tolerance 1.2000000476837158\n")
            aios.passthrough(Server_IP_list[i], "w axis1.controller.config.vel_ramp_rate 1.0\n")

            aios.passthrough(Server_IP_list[i], "w axis1.encoder.config.cpr 4000\n")

            aios.passthrough(Server_IP_list[i], "w axis1.trap_traj.config.vel_limit 30.0\n")
            aios.passthrough(Server_IP_list[i], "w axis1.trap_traj.config.accel_limit 80.0\n")
            aios.passthrough(Server_IP_list[i], "w axis1.trap_traj.config.decel_limit 80.0\n")

            # aios.passthrough(Server_IP_list[i], "se\n") # reboot motor drive
            aios.saveConfig(Server_IP_list[i])
        # print('\n')



        for i in range(len(Server_IP_list)):
            # aios.passthrough(Server_IP_list[i], "r config.dc_bus_undervoltage_trip_level\n")
            # aios.passthrough(Server_IP_list[i], "r config.dc_bus_overvoltage_trip_level\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.pre_calibrated\n")
            aios.passthrough(Server_IP_list[i], "r axis1.motor.config.pole_pairs\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.direction\n")
            aios.passthrough(Server_IP_list[i], "r axis1.encoder.config.bandwidth\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.calibration_current\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.resistance_calib_max_voltage\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.phase_inductance\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.phase_resistance\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.current_lim\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.current_lim_margin\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.requested_current_range\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.motor.config.current_control_bandwidth\n")

            # aios.passthrough(Server_IP_list[i], "r axis1.controller.config.control_mode\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.controller.config.pos_gain\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.controller.config.vel_gain\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.controller.config.vel_integrator_gain\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.controller.config.vel_limit\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.controller.config.vel_limit_tolerance\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.controller.config.vel_limit\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.controller.config.vel_ramp_enable\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.controller.config.vel_ramp_rate\n")

            aios.passthrough(Server_IP_list[i], "r axis1.motor.config.inverter_temp_limit_lower\n")
            aios.passthrough(Server_IP_list[i], "r axis1.motor.config.inverter_temp_limit_upper\n")

            aios.passthrough(Server_IP_list[i], "r axis1.encoder.config.cpr\n")

            # aios.passthrough(Server_IP_list[i], "r axis1.trap_traj.config.vel_limit\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.trap_traj.config.accel_limit\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.trap_traj.config.decel_limit\n")
            # aios.passthrough(Server_IP_list[i], "r axis1.trap_traj.config.A_per_css\n")

        print('\n')





if __name__ == '__main__':
    main()

