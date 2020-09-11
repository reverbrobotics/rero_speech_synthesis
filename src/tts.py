#!/usr/bin/env python
import time
from threading import Thread
import rospy
from std_msgs.msg import String
import numpy as np
from time import sleep
import subprocess

rospy.init_node('ros_tts_node', anonymous=True)

tts_topic_name = rospy.get_param('~topic_name')
rospy.loginfo("%s is %s", rospy.resolve_name('tts_topic_name'), tts_topic_name)

loop_rate = rospy.get_param('loop_rate')
rospy.loginfo("%s is %s", rospy.resolve_name('loop_rate'), loop_rate)

rate = rospy.Rate(loop_rate)  # 10hz

def callback(data):
	print(data)

	process = subprocess.run(args=['mimic', '-t',  str(data.data)], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)



rospy.Subscriber(tts_topic_name, String, callback)

rospy.spin()
