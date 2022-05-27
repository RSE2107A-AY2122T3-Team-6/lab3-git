#!/usr/bin/env python

from __future__ import print_function
from limo_status_translator.srv import GetLimoStatus, GetLimoStatusResponse
import rospy

from limo_status_translator.msg import LimoStatus
from std_msgs.msg import String

result = LimoStatus()

def callback(data):
    result.vehicle_state = data.vehicle_state
    result.control_mode  = data.control_mode
    result.battery_voltage = data.battery_voltage
    result.error_code = data.error_code
    result.motion_mode = data.motion_mode
#   rospy.loginfo("vechicle state: " + str(result.vehicle_state))
#    rospy.loginfo("control_mode:  " + str(result.control_mode))
#    rospy.loginfo("battery_voltage: " + str(result.battery_voltage))
#    rospy.loginfo("error_code: " + str(result.error_code))
#    rospy.loginfo("motion_mode: " + str(result.motion_mode))

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("limo_status", LimoStatus, callback)
    rospy.spin()

def set_vehicle_msg(vehicle_state):
    msg = ""
    if (vehicle_state == 0):
        msg = "System Normal"
    else:
        msg = "System Exception"
    return msg

def set_control_msg(control_mode):
    msg = ""
    if (control_mode == 0):
        msg = "Standby"
    elif (control_mode == 1):
        msg = "Command Control"
    elif (control_mode == 2):
        msg = "App Control"
    else:
        msg = "Remote Control"
    return msg
    
def set_error_msg(error_code):
    error_msg = ""
    if error_code == 0:
        error_msg = "no faults"
    else:
        binary_code = bin(error_code)[2:].zfill(10)
        for i, c in enumerate(binary_code):
            if i == 0:
                if c == '1': 
                    error_msg = "Upper layer communication status"
            if i == 1:
                if c =='1':
                    if error_msg != "":
                        error_msg += "\n"
                    error_msg += "Driver failure"
            if i == 3:
                if c == '1':
                    if error_msg != "":
                        error_msg += "\n"
                    error_msg += "(Motor No.4) Motor driver communication failure"
            if i == 4:
                if c == '1':
                    if error_msg != "":
                        error_msg += "\n"
                    error_msg += "(Motor No.3) Motor driver communication failure"
            if i == 5:
                if c == '1':
                    if error_msg != "":
                        error_msg += "\n"
                    error_msg += "(Motor No.2) Motor driver communication failure"
            if i == 6:
                if c == '1':
                    if error_msg != "":
                        error_msg += "\n"
                    error_msg += "(Motor No.1) Motor driver communication failure"
            if i == 7:
                if c == '1':
                    error_msg += "Remote control connection loss"
            if i == 8:
                if c == '1':
                    if error_msg != "":
                        error_msg += "\n"
                    error_msg += "Battery undervoltage warning (<9.5V)"
            if i == 9:
                if c == '1':
                    if error_msg != "":
                        error_msg += "\n"
                    error_msg += "Battery undervoltage fault"
    return error_msg

def set_motion_msg(motion_mode):
    motion_msg = ""
    if (motion_mode == 0):
        motion_msg = "4-wheeled differential"
    elif (motion_mode == 1):
        motion_msg = "Ackermann"
    else: 
        motion_msg = "Mecanum"
    return motion_msg
    
def handle_req(req):
        if (req == 0):
            text = set_vehicle_msg(result.vehicle_state)
            return GetLimoStatusResponse(text)
        if (req == 1):
            text = set_control_msg(result.control_mode)
            return GetLimoStatusResponse(text)
        if (req == 2):
            text = "%f" % result.battery_voltage + "V"
            return GetLimoStatusResponse(text)
        if (req == 3):
            text = set_error_msg(result.error_code)
            return GetLimoStatusResponse(text)
        if (req == 4):
            text = set_motion_msg(result.motion_mode)
            return GetLimoStatusResponse(text)

def server():
    #rospy.init_node('server')
    rospy.Service("server", GetLimoStatus, handle_req)
    print("GET_STATUS_VEHICLE_STATE = 0\n")
    print("GET_STATUS_CONTROL_MODE = 1\n")
    print("GET_STATUS_BATTERY_VOLTAGE = 1\n")
    print("GET_STATUS_ERROR_CODE = 1\n")
    print("GET_STATUS_MOTION_MODE = 1\n")
    print("get_status: ")
    rospy.spin()

if __name__ == '__main__':
    listener()
    server()
