#!/usr/bin/env python

from __future__ import print_function

import sys
import random
import rospy
from std_msgs.msg import String
from limo_status_translator.srv import GetLimoStatus, GetLimoStatusRequest


def publish(msg):
    pub1 = rospy.Publisher('/limo_status/vehicle_state', String, queue_size=50)
    pub2 = rospy.Publisher('/limo_status/control_mode', String, queue_size=50)
    pub3 = rospy.Publisher('/limo_status/battery_voltage', String, queue_size=50)
    pub4 = rospy.Publisher('/limo_status/error_code', String, queue_size=50)
    pub5 = rospy.Publisher('/limo_status/motion_mode', String, queue_size=50)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        str = msg
        rospy.loginfo(str)
        pub1.publish(str)
        pub2.publish(str)
        pub3.publish(str)
        pub4.publish(str)
        pub5.publish(str)
        rate.sleep()
        return
        

if __name__ == "__main__":

    rospy.init_node('client')
    service = rospy.ServiceProxy('service', GetLimoStatus)
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        a = random.randint(0,4)
        rospy.loginfo("sending [%d] " % a)
        req = GetLimoStatusRequest()
        req.get_status = a
        rospy.wait_for_service('service')
        resp = service(req)
        rospy.loginfo("Recieved: " + resp.status_string)
        r.sleep()
        publish(resp.status_string)
    
    


    
