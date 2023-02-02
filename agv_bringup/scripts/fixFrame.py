#!/usr/bin/env python3
import rospy
import sys
import tf
import tf2_ros
import geometry_msgs.msg

import termios
import tty
import os
import time
import math
import json

def main():
    return

def publish_status(broadcaster, status):
    static_transformStamped = geometry_msgs.msg.TransformStamped()
    static_transformStamped.header.stamp = rospy.Time.now()
    static_transformStamped.header.frame_id = from_cam

    static_transformStamped.child_frame_id = to_cam
    static_transformStamped.transform.translation.x = status['x']['value']
    static_transformStamped.transform.translation.y = status['y']['value']
    static_transformStamped.transform.translation.z = status['z']['value']

    quat = tf.transformations.quaternion_from_euler(math.radians(status['roll']['value']),
                                                    math.radians(status['pitch']['value']),
                                                    math.radians(status['azimuth']['value']))
    static_transformStamped.transform.rotation.x = quat[0]
    static_transformStamped.transform.rotation.y = quat[1]
    static_transformStamped.transform.rotation.z = quat[2]
    static_transformStamped.transform.rotation.w = quat[3]
    broadcaster.sendTransform(static_transformStamped)


if __name__ == '__main__':
    # arg1 = cam_1_link, arg2 = cam_2_link
    from_cam, to_cam = sys.argv[1:3]

    x, y, z, yaw, pitch, roll = [float(arg) for arg in sys.argv[3:9]]
    status = {'mode': 'pitch',
              'x': {'value': x, 'step': 0.1},
              'y': {'value': y, 'step': 0.1},
              'z': {'value': z, 'step': 0.1},
              'azimuth': {'value': yaw, 'step': 1},
              'pitch': {'value': pitch, 'step': 1},
              'roll': {'value': roll, 'step': 1},
              'message': ''}

    rospy.init_node('my_static_tf2_broadcaster')
    broadcaster = tf2_ros.StaticTransformBroadcaster()
    publish_status(broadcaster, status)
    while True:
        publish_status(broadcaster, status)
        rospy.spin()
