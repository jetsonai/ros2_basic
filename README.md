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

cd ~/ros2_ws/src

웹에서 다운로드 받으세요
https://drive.google.com/file/d/1bWPNJ43AbFW3pFxFrMxxemuaZyk9zbNd/view?usp=sharing

cp -rf ~/Downloads/ros2_basic-exe/ros2_basic_test ./

ls

TODO 수

cd

cd ros2_ws/

colcon build --packages-select ros2_basic_test




