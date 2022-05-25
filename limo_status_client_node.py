#!/usr/bin/env python
#details 

import rospy
from std_msgs.msg import String

#### requests details from translator node
def request(x):
    pub = rospy.Publisher('getStatus', String, queue_size=10)
    rospy.init_node('Client_Node', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        str = "%s" + x
        rospy.loginfo(str)
        pub.publish(str)
        rate.sleep()


#### getting response from translator node
def callback(data):
    rospy.loginfo("", data.data)
    global msg 
    msg = data.data
    
def response():
    rospy.Subscriber('status_string', String, callback)


#### Dictionary
topics = {1 : '/limo_status/vehicle_state', 2 : '/limo_status/control_mode', 3 : '/limo_status/battery_voltage', 4 : '/limo_status/error_code', 5 : '/limo_status/motion_mode'}

i = 1
#### publishing to the 5 topics
def publisher(x):
    while i < 6 :
        pub = rospy.Publisher(topics[i], String, queue_size = 10)
        rate = rospy.Rate(1) # 1hz
        while not rospy.is_shutdown():
            str = "%s" + x
            rospy.loginfo(str)
            pub.publish(str)
            rate.sleep()

a = 0

if __name__ == '__main__':
    while a < 5:
        try:
            request(a)
            publisher(msg)
        except rospy.ROSInterruptException:
            pass

