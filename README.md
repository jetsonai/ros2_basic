# ros2_basic

교재의 실습 파일입니다.

TODO 있습니다.

# ros2 workspace 생성 및 소스 다운로드와 빌드

mkdir -p ~/ros2_ws/src

cd ~/ros2_ws/src

git clone https://github.com/jetsonai/ros2_basic

ls

cd

rosdep install -i --from-path src --rosdistro foxy -y

rosdep update

cd ros2_ws/

colcon build


# package 생성 테스트

cd ~/ros2_ws/src

ros2 pkg create testpackage --build-type ament_python --dependencies rclpy std_msgs  --node-name testnode

cd ~/ros2_ws

colcon build --packages-select testpackage

source ./install/setup.bash

ros2 run testpackage testnode



