Repo for UTSA's R5 Robotics Comp Robot
===

## :package: Package Overview
### AAV
- [`aav.repos`](./aav.repos): VCS install of other required packages for AAV
- [`aav_control`](./aav_control):  Package for control of tello drone
- [`aav_description`](./aav_description): URDF description of AAV
### AGV
- [`agv.repos`](./agv.repos): VCS install of other required packages for AGV
- [`agv_base`](./agv_base): Hardware drivers and MCU code
- [`agv_bringup`](./agv_bringup): Launch files to bring up the hardware driver nodes (cameras, microcontroller, etc.) as well as the C++ nodes from the agv_base package for the real robot.
- [`agv_control`](./agv_control): Package for ROS control implementation and control inputs (keyboard
- [`agv_description`](./agv_description): URDF description of AGV including its sensors.
- [`agv_metapkg`](./agv_metapkg): ROS metapkg convention for easy install of whole ROS stack
- [`agv_msgs`](./agv_msgs): Message definitions specific to AGV, for example the message for encoder data
- [`agv_navigation`](./agv_navigation): Navigation package for implementationof ROS Nav stack
### General
- [`perception_utils`](./perception_utils): Utility package for Robot's perception systems
- [`obj_detection`](./obj_identification): Identification package of key competition objects (Boxes, box faces, gaffer tape on carpet, AGV, and AAV)
- [`autonomy`](./states_round1): State code package for both AAV and AGV
- [`misc`](./misc): Holds all previous repo files. Need to sort and clean...
- [`docs`](./docs): General notes, images, and documents related to Robot's development
## Installation
- cd to your workspace's src directory
```
git clone https://github.com/UTSARobotics/R5Robot_22-23.git
```
- Install some dependencies
```
sudo apt-get install -y \
ros-noetic-roslint \
ros-noetic-rosserial \
ros-noetic-rosserial-arduino \
ros-noetic-imu-filter-madgwick \
ros-noetic-gmapping \
ros-noetic-map-server \
ros-noetic-navigation \
ros-noetic-robot-localization \
ros-noetic-tf2 \
ros-noetic-tf2-ros
```
