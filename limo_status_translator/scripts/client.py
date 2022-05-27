#!/usr/bin/env python

from __future__ import print_function

import sys
import random
import rospy
from limo_status_translator.srv import GetLimoStatus, GetLimoStatusRequest

def talker(a,resp):
        if a == 0:
            pub = rospy.Publisher('limo_status/vehicle_state', String, queue_size = 10)
            rate = rospy.Rate(1)
            pub.publish(resp.status_string)

        if a == 1:
            pub = rospy.Publisher('limo_status/control_mode', String, queue_size = 10)
            rate = rospy.Rate(1)
            pub.publish(resp.status_string)

        if a == 2:
            pub = rospy.Publisher('limo_status/battery_voltage', String, queue_size = 10)
            rate = rospy.Rate(1)
            pub.publish(resp.status_string)

        if a == 3:
            pub = rospy.Publisher('limo_status/error_code', String, queue_size = 10)
            rate = rospy.Rate(1)
            pub.publish(resp.status_string)

        if a == 4:
            pub = rospy.Publisher('limo_status/motion_mode', String, queue_size = 10)
            rate = rospy.Rate(1)
            pub.publish(resp.status_string)

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
        talker(a,resp)
        
        r.sleep()
    
