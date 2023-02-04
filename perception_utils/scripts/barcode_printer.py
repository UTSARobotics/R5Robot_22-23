#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
 # node_name/argsname
    camName = rospy.get_param("~camera_name")
    print(camName + ": " + data.data)
    
def listener():
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('barcode_printer', anonymous=True)

    rospy.Subscriber('barcode', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
