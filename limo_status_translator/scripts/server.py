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
    rospy.loginfo("vechicle state: " + str(result.vehicle_state))
    rospy.loginfo("control_mode:  " + str(result.control_mode))
    rospy.loginfo("battery_voltage: " + str(result.battery_voltage))
    rospy.loginfo("error_code: " + str(result.error_code))
    rospy.loginfo("motion_mode: " + str(result.motion_mode))

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("limo_status", LimoStatus, callback)
    rospy.spin()

def handle_req(req):
    print("GET_STATUS_VEHICLE_STATE = 0\n")
    print("GET_STATUS_CONTROL_MODE = 1\n")
    print("GET_STATUS_BATTERY_VOLTAGE = 1\n")
    print("GET_STATUS_ERROR_CODE = 1\n")
    print("GET_STATUS_MOTION_MODE = 1\n")
    print("get_status: ")
    
    text = ""

    if(result.vehicle_state == 0):
        text = "System Normal"
    else:
        text = "System Exception"
    
    if(result.control_mode == 0):
        text = "Standby"
    elif(result.control_mode == 1):
        text = "Command Control"
    elif(result.control_mode == 2):
        text = "App Control"
    else:
        text = "Remote Control"

    text = str(result.battery_voltage + "V")

    if(result.motion_mode == 0):
        text = "4 wheel differential"
    elif(result.motion_mode == 1):
        text = "Ackermann"
    else:
        text = "Mecanum"

    if(result.error_code == 0):
        text = "No fault"
    else:
        text = "fault"

    return GetLimoStatusResponse(text)

def server():
    #rospy.init_node('server')
    rospy.Service("server", GetLimoStatus, handle_req)
    rospy.spin()

if __name__ == '__main__':
    listener()
    server()
