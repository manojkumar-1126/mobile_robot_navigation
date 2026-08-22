# Warehouse Navigation with ROS 2

https://github.com/user-attachments/assets/1cdecc9e-ed34-4921-aae2-93e111f515ad

A ROS 2 warehouse simulation project focused on autonomous mobile robot navigation using Gazebo, 2D LiDAR, SLAM Toolbox, AMCL, and Nav2.

## Overview

This project simulates a differential-drive mobile robot operating inside a custom warehouse environment.

The robot is equipped with:

- Differential-drive motion
- Wheel odometry
- 2D LiDAR
- TF2 frame tree
- Gazebo simulation

The navigation pipeline uses:

- SLAM Toolbox for mapping
- AMCL for localization
- Nav2 for autonomous navigation
- Global and local costmaps
- Global path planning
- Local trajectory control
- RViz2 for visualization

 **Gazebo warehouse simulation**  
  The robot operates inside a custom warehouse environment containing racks, shelves, boxes, and obstacles.

- **Robot perception**  
  The simulated 2D LiDAR continuously observes the surrounding environment through the `/scan` topic.

- **Odometry and TF**  
  Wheel odometry is published through `/odom`, while TF2 maintains the relationship between the robot frames and the navigation frames.

- **RViz2 navigation initialization**  
  RViz2 is used to visualize the generated warehouse map, robot pose, LiDAR data, navigation costmaps, and planned paths. The robot's initial pose is provided using **2D Pose Estimate**.

- **AMCL localization**  
  AMCL estimates the robot's position within the previously generated warehouse map using LiDAR observations and odometry.

- **Nav2 autonomous navigation**  
  A navigation goal is provided through RViz2. Nav2 generates a global path and uses the local costmap and controller to guide the robot toward the goal while considering detected obstacles.

- **Gazebo and RViz2 observation**  
  Gazebo is used to observe the robot's actual movement inside the simulated warehouse, while RViz2 provides the navigation and perception visualization.

## Running Autonomous Navigation

After generating and saving the warehouse map, the robot can be started in autonomous navigation mode using the following steps.

### 1. Source the ROS 2 Workspace

Open a terminal and source the workspace:

```bash
source ~/ros2_ws/install/setup.bash
```
### 2. Launch Nav2 Navigation

```bash
ros2 launch warehouse_navigation navigation.launch.py
```

The navigation.launch.py file starts the Nav2 navigation system and loads the saved warehouse map and the project's Nav2 configuration.

### 3. Start RViz2

Open a second terminal and source the workspace:

```bash
source ~/ros2_ws/install/setup.bash
rviz2
```
### 4. Initialize the Robot Pose

In RViz2, select 2D Pose Estimate and provide the robot's initial position and orientation on the warehouse map.

### 5. Send a Navigation Goal

Use the navigation goal tool in RViz2 to select the desired destination.

Nav2 then:

- Generates a global path to the goal.
- Uses the global and local costmaps for obstacle-aware navigation.
- Uses LiDAR observations to detect obstacles.
- Generates velocity commands for the robot.
- Drives the robot autonomously toward the goal.

The robot's actual movement is observed in Gazebo, while the map, localization, costmaps, planned path, and navigation state are monitored in RViz2.

## System Architecture

```text
                  Gazebo
                    |
          +---------+---------+
          |                   |
       Odometry             LiDAR
          |                   |
          v                   v
        /odom               /scan
          |                   |
          +--------+----------+
                   |
                  TF2
                   |
          +--------+--------+
          |                 |
       SLAM Toolbox       AMCL
          |                 |
       /map              map -> odom
          |                 |
          +--------+--------+
                   |
                  Nav2
                   |
        +----------+----------+
        |                     |
 Global Costmap          Local Costmap
        |                     |
        +----------+----------+
                   |
             Path Planning
                   |
              /cmd_vel
                   |
                 Robot
```

### Conclusion

This project successfully demonstrates autonomous mobile robot navigation in a simulated warehouse using ROS 2, Gazebo, SLAM Toolbox, AMCL, and Nav2.
The robot was mapped, localized, and navigated to goals through RViz2 while its movement was observed in Gazebo.
