# Warehouse Navigation with ROS 2

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

