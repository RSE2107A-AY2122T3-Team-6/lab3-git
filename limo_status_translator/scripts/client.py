#!/usr/bin/env python

from __future__ import print_function
from http import server

import sys
import rospy
from limo_status_translator.srv import *

def client(x):
    rospy.init_node("client_node")
    rospy.wait_for_service("server")
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            get_state = rospy.ServiceProxy('server', GetLimoStatus)
            respl = get_state(x)
            rospy.loginfo(respl)
            rate.sleep()
        except rospy.ServiceException as e:
            print("Service call failed %s", e)
    

a = 0

if __name__ == '__main__':
    while a < 5:
        try:
            client(a)
            a += 1
        except rospy.ROSInterruptException:
            pass
