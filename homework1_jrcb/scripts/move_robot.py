#!/usr/bin/env python
# S
# Revision $Id$

##

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10) # 10hz
    joint_msg = JointState()
    joint_msg.header = Header()
    joint_msg.name = ['head_to_core', 'core_to_left_arm', 'core_to_right_arm']
    joint_msg.velocity = []
    joint_msg.effort = []


    j = 0.01
    while not rospy.is_shutdown():
        
        if (j>3.13):
            j=0.01
        else:
            j=j+0.01

        joint_msg.header.stamp = rospy.Time.now()
        joint_msg.position = [1.57-j, (1.57-j), (-1.57+j)]
        rospy.loginfo(joint_msg)
        pub.publish(joint_msg)
        rate.sleep()



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
