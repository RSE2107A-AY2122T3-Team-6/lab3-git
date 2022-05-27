#!/usr/bin/env python

from __future__ import print_function

import sys
import random
import rospy
from limo_status_translator.srv import GetLimoStatus, GetLimoStatusRequest



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
    
