#!/usr/bin/env python3

#SPDX-License-Identifier:BSD-2.0

#*Copyright(c)2021 Ryuich Ueda. All rights reserved.
import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up',Int32,queue_size=1)
rate = rospy.Rate(5)
n = 0
while not rospy.is_shutdown():
    n += 2
    pub.publish(n)
    rate.sleep()
