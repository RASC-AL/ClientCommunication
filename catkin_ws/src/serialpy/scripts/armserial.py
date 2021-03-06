#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import serial

com = serial.Serial('/dev/ttyS0',baudrate=115200)

def callback(data):
	rospy.loginfo(data)
	if 'HOME' in str(data):
		com.write('p')
	else:
		data = 'a,'+str(data) + '\n'
		com.write(data)
		com.flush()

def controller():
	rospy.init_node('arm')
	rospy.Subscriber('/ARM', String, callback)
	rospy.spin()

if __name__ == '__main__':
	controller()
