# ros2_basic_test
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir

def generate_launch_description():
    return LaunchDescription([
    
        Node(
            package='ros2_basic_test', 
            executable='rostopic_pub', 
            output='screen',
            emulate_tty=True),
        Node(
            package='ros2_basic_test', 
            executable='rostopic_sub', 
            output='screen',
            emulate_tty=True),        
    ])
