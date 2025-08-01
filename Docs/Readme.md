# Car Teleoperation Simulation in Gazebo

A ROS-based simulation project that enables remote control of a car model in Gazebo using keyboard teleoperation.

## 📋 Overview

This project demonstrates the implementation of a car teleoperation system using ROS (Robot Operating System) and Gazebo simulator. The system allows users to control a simulated car model remotely through keyboard inputs, providing an intuitive interface for vehicle navigation and control.

**Teleoperation** refers to the operation of a system or machine at a distance, enabling users to control robotic systems without direct physical interaction.

## 🎯 Features

- **Real-time Car Control**: Control car movement using keyboard inputs
- **3D Visualization**: Monitor and visualize the car model in Gazebo's 3D environment
- **ROS Integration**: Leverages ROS communication system for seamless data exchange
- **Cross-platform Compatibility**: Runs on Linux environments with ROS support

## 🛠️ Technologies Used

- **ROS (Robot Operating System)**: Middleware framework for robot software development
- **Gazebo**: Open-source 3D robotics simulator
- ** UBUNTU 20.04LTS **: Operating system environment
- **Python/C++**: Programming languages for ROS nodes

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

### System Requirements
- Ubuntu 18.04/20.04/22.04 (recommended)
- ROS Melodic/Noetic/Humble (depending on Ubuntu version)
- Gazebo (usually comes with ROS installation)

### ROS Packages
```bash
sudo apt-get install ros-<distro>-gazebo-ros-pkgs
sudo apt-get install ros-<distro>-gazebo-ros-control
sudo apt-get install ros-<distro>-teleop-twist-keyboard
```

Replace `<distro>` with your ROS distribution (melodic, noetic, humble, etc.)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/elqmausam/Teleop_ROS.git
   cd car-teleoperation-simulation
   ```

2. **Build the workspace**
   ```bash
   catkin_make
   # or for ROS2
   colcon build
   ```

3. **Source the workspace**
   ```bash
   source devel/setup.bash
   # or for ROS2
   source install/setup.bash
   ```

## 🎮 Usage

### Starting the Simulation

1. **Launch Gazebo with the car model**
   ```bash
   roslaunch car_simulation car_world.launch
   ```

2. **Start the teleoperation node** (in a new terminal)
   ```bash
   rosrun teleop_twist_keyboard teleop_twist_keyboard.py
   ```

### Control Commands

Use the following keys to control the car:

| Key | Action |
|-----|--------|
| `i` | Move Forward |
| `k` | Stop |
| `j` | Turn Left |
| `l` | Turn Right |


Press `Ctrl+C` to exit teleoperation mode.


## 🔧 Configuration

### Modifying Car Parameters

Edit the URDF file in `car_description/urdf/car.urdf` to modify:
- Vehicle dimensions
- Wheel properties
- Sensor configurations
- Physical properties (mass, inertia)

### Adjusting Simulation Environment

Modify the world file in `car_gazebo/worlds/` to change:
- Terrain and obstacles
- Lighting conditions
- Environmental factors

## 🐛 Troubleshooting

### Common Issues

1. **Gazebo doesn't start**
   ```bash
   # Check if Gazebo is properly installed
   gazebo --version
   # Kill any existing Gazebo processes
   killall gzserver gzclient
   ```

2. **Car model not visible**
   - Ensure all mesh files are in the correct directory
   - Check URDF file paths
   - Verify model spawning in launch file

3. **Teleoperation not working**
   - Confirm the topic names match between publisher and subscriber
   - Check if the keyboard node is publishing to the correct topic
   - Verify ROS master is running

### Debug Commands

```bash
# Check active topics
rostopic list

# Monitor velocity commands
rostopic echo /cmd_vel

# View TF tree
rosrun tf view_frames
```




## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Saniya Kureshi** - *Initial work* - (https://github.com/elqmausam)

## 🙏 Acknowledgments

- ROS Community for the excellent documentation
- Gazebo team for the powerful simulation environment
- Open Source Robotics Foundation (OSRF)

## 📚 References

- [ROS Documentation](http://wiki.ros.org/)
- [Gazebo Tutorials](http://gazebosim.org/tutorials)
- [URDF XML Specification](http://wiki.ros.org/urdf/XML)


---

**Happy Simulating! 🚗💨**
