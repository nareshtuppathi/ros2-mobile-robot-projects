# ROS 2 Mobile Robot Projects 🤖

This repository contains the ROS 2-based mobile robot project featuring URDF modeling, Gazebo simulation, RViz visualization, and autonomous navigation using computer vision, machine learning.


## Environment

- ROS 2 Humble
- Ubuntu
- Docker
- Python 3
- TurtleBot3
- Gazebo

---

# Projects

## 1. LiDAR Reader

### Description
A ROS 2 node that reads LiDAR sensor data from the TurtleBot3 laser scanner.

### Concepts Learned
- ROS 2 Nodes
- Subscribers
- LaserScan messages
- Topics

### Topic
/scan

---

## 2. Obstacle Avoidance

### Description
A basic autonomous navigation node that stops the robot when an obstacle is det>

### Concepts Learned
- LiDAR processing
- Distance thresholding
- Publishing velocity commands

### Topics

Input:
/scan
Output:
/cmd_vel

---

## 3. Smart Obstacle Avoidance

### Description
A smarter obstacle avoidance system using LiDAR data to make movement decisions.

## Architecture
LiDAR Sensor
|
v
/scan Topic
|
v
Obstacle Avoidance Node
|
v
/cmd_vel
|
v
Robot Movement


### Technologies

- ROS 2 Humble
- Python
- - TurtleBot3
- Gazebo
- LiDAR

---

# How to Build

```bash
cd ~/robotics_ws

colcon build

source install/setup.bash

How to Run:
EX: ros2 run smart_obstacle_avoidance smart_obstacle_avoidance

Future Projects:
Camera Integration
OpenCV Robotics
Object Detection
SLAM
Navigation2
Autonomous Mobile Robot




