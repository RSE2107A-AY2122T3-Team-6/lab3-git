#!/usr/bin/env python

import rospy 
import NumPy
from std_msgs.msg import String 

topics[5] = ['/limo_status/vehicle_state', '/limo_status/control_mode', '/limo_status/battery_voltage', '/limo_status/error_code', '/limo_status/motion_mode']

def fiveTopics():
    pub1 = rospy.Publisher(topics[0], String, queue_size = 40)
    pub2 = rospy 