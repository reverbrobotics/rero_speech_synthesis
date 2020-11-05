#!/usr/bin/env python
import time
from threading import Thread
import rospy
from std_msgs.msg import String
import numpy as np
from time import sleep
import subprocess
from espeakng import ESpeakNG


rospy.init_node('ros_tts_node', anonymous=True)

tts_topic_name = rospy.get_param('~topic_name')
rospy.loginfo("%s is %s", rospy.resolve_name('tts_topic_name'), tts_topic_name)

pitch = rospy.get_param('pitch')
rospy.loginfo("%s is %s", rospy.resolve_name('pitch'), pitch)

speed = rospy.get_param('speed')
rospy.loginfo("%s is %s", rospy.resolve_name('speed'), speed)

voice = rospy.get_param('voice')
rospy.loginfo("%s is %s", rospy.resolve_name('voice'), voice)

loop_rate = rospy.get_param('loop_rate')
rospy.loginfo("%s is %s", rospy.resolve_name('loop_rate'), loop_rate)

loop_rate = rospy.get_param('loop_rate')
rospy.loginfo("%s is %s", rospy.resolve_name('loop_rate'), loop_rate)

rate = rospy.Rate(loop_rate)  # 10hz

esng = ESpeakNG(voice=voice)
esng.pitch = pitch
esng.speed = speed

def callback(data):
	print(data)
	esng.say(data.data)

rospy.Subscriber(tts_topic_name, String, callback)

rospy.spin()
