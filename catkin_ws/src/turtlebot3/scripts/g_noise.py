#!/usr/bin/env python
import rosbag
import rospy
from geometry_msgs.msg import Twist
import random

def add_noise(velocity):
    noisy_velocity = Twist()
    noisy_velocity.linear.x = velocity.linear.x + random.gauss(0, 0.1)  # Add Gaussian noise
    noisy_velocity.angular.z = velocity.angular.z + random.gauss(0, 0.05)
    return noisy_velocity

def main():
    rospy.init_node('g_noise')
    pub = rospy.Publisher('/turtlebot3/cmd_vel_noisy', Twist, queue_size=10)
    rate = rospy.Rate(10)  # Publish at 10 Hz

    bag = rosbag.Bag('only_vel.bag', 'r')
    for topic, msg, t in bag.read_messages(topics=['/turtlebot3/cmd_vel']):
        noisy_msg = add_noise(msg)
        pub.publish(noisy_msg)
        rospy.loginfo("Noisy Velocity: %s", noisy_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
