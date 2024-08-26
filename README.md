# ros2_basic

교재의 실습 파일입니다.

TODO 있습니다.


# ros2 workspace 생성 및 소스 다운로드와 빌드

mkdir -p ~/ros2_ws/src


# package 생성 테스트

cd ~/ros2_ws/src

ros2 pkg create testpackage --build-type ament_python --dependencies rclpy std_msgs  --node-name testnode

cd ~/ros2_ws

colcon build --packages-select testpackage

source ./install/setup.bash

ros2 run testpackage testnode

# 기본 테스트

gedit .bashrc 수정

cd ~/ros2_ws/src

웹에서 다운로드 받으세요
https://drive.google.com/file/d/1bWPNJ43AbFW3pFxFrMxxemuaZyk9zbNd/view?usp=sharing

탐색기를 이용하여 패키지 파일들을 모두 ros2_ws/src 아래로 옮겨주세요

## ros2_basic_test

TODO 수행

cd ros2_ws/

colcon build --packages-select ros2_basic_test

source /home/nvidia/ros2_ws/install/setup.bash

ros2 run ros2_basic_test rostopic_pub

ros2 run ros2_basic_test rostopic_sub

## custom_msgpack

colcon build --packages-select custom_msgpack

## ros2_basic_topicmsg

TODO 수행

colcon build --packages-select ros2_basic_topicmsg

ros2 run ros2_basic_topicmsg info_publisher

ros2 run ros2_basic_topicmsg info_subscriber

## ros2_basic_service

TODO 수행

colcon build --packages-select ros2_basic_service

ros2 run ros2_basic_service srv_server

ros2 run ros2_basic_service srv_client

## ros2_basic_action

TODO 수행

colcon build --packages-select ros2_basic_action

ros2 run ros2_basic_action simple_action_server

ros2 run ros2_basic_action simple_action_client

ros2 launch ros2_basic_test basic_test_launch.py

colcon build --packages-select ros2_basic_test


