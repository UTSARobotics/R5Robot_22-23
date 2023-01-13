Created: 2022-10-13
tags:[[Robotics]]
links: [[_UTSA MOC]]
___
# R5 Robotics Competition
---

## Week 1 - 8-10/10/22
### Assigned Task:
> drone operation and familiarization (flight characteristics, knowledge of general aerial behavior, etc.).
> this will be mostly to get us comfortable with how the drone flies in the air, so that we can hopefully be familiar with any quirks when it is time to program.

### DJI Tello Specs
Weight: ~80g (w/ propellers and battery)
Dimensions: 98x92.5x41mm

#### Flight Limits
Max flight distance: 100m
Max speed: 8m/s
Max flight time: 13 minutes
Max flight height: 30m

### Drone Movement
The two pairs of propellers spin in different directions. This is to prevent the drone body from spinning (*reaction torque*).
When moving on the yaw axis, one propeller pair moves faster than the other in order to spin the drone body.
- Spin clockwise => increase rpm of propellers spinning counter-clockwise, decrease clockwise
- Spin counter-clockwise => increase rpm of propellers spinning clockwise, decrease counter-clockwise
Same principle for pitch and roll.
Hover => weight = lift force

## Week 2 - 14/10/22
Localization:
- SLAM
- ROS Nav
- LIDAR
	- Kinect
- IR emitter on drone
- Sensors:
	- Ultrasonic

Wheels:
- Omni wheels
	- Possibly inaccurate
	- Less friction
- "Tank" tracks
- Pneumatic wheels

### Assigned Task
> On Jetson Nano, establishing a connection to the Tello and hopefully getting some basic commands in to fly it.

https://tello.oneoffcoder.com/
#### Connect to Tello
UDP, Port 8889, Version 1.0

## Week 3 - 24/10/22
### Assigned Task
> ould love to have yall continue with drone programming and trying to pull video data off of the Tello.

### ROS Workshop - Fri
##### ROS Terminal Commands for Debugging
- `roscore` - start ROS Master
- `rosrun 'package_name' 'executable_node'` - run executable_node

1, 2

## Week 4 - 31/10/22
### Assigned Task
> finding and familiarizing yourself with some kind of Microsoft Kinect import library for python. That would help a whole lot with the slam that we want to start implementing very soon.

[OpenKinect](https://openkinect.org/) - Library for Xbox Kinect
[OpenKinect/libfreenect](https://github.com/OpenKinect/libfreenect) - Xbox Kinect v1 drivers for Windows, Linux, MacOS
- [OpenKinect/libfreenect2](https://github.com/OpenKinect/libfreenect2) - v2 drivers
- [ros-drivers/libfreenect](https://github.com/ros-drivers/libfreenect) - OpenKinect drivers for ROS - repo
[code-iai/iai_kinect2](https://github.com/code-iai/iai_kinect2) - Tools to interface with Xbox Kinect v2 in ROS
- [TheEngineRoom-UniGe/iai_kinect2](https://github.com/TheEngineRoom-UniGe/iai_kinect2) - Updated for noetic
