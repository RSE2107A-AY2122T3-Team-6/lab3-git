#!/usr/bin/env python

from __future__ import print_function
from http import server

import sys
import rospy
from limo_status_translator.srv import *

def client(x):
    rospy.wait_for_service('server')
    try:
        get_state = rospy.ServiceProxy('server', GetLimoStatus)
        respl = server(x)
        return respl