# ros2_basic

교재의 실습 파일입니다.

TODO 있습니다.


## ros2 workspace 생성 

mkdir -p /data/ros2_ws/src


## package 생성 테스트

cd /data/ros2_ws/src

ros2 pkg create testpackage --build-type ament_python --dependencies rclpy std_msgs  --node-name testnode

cd /data/ros2_ws

colcon build --packages-select testpackage

source ./install/setup.bash

ros2 run testpackage testnode

## 기본 테스트

웹에서 다운로드 받으세요
https://drive.google.com/file/d/1bWPNJ43AbFW3pFxFrMxxemuaZyk9zbNd/view?usp=sharing

탐색기를 이용하여 패키지 파일들을 모두 ros2_basic_ws/src 아래로 옮겨주세요

### ros2_basic_test

TODO 수행

cd ros2_basic_ws/ 

혹은

cdbasic

colcon build --packages-select ros2_basic_test

source /home/nvidia/ros2_ws/install/setup.bash

ros2 run ros2_basic_test rostopic_pub

ros2 run ros2_basic_test rostopic_sub


### launch 테스트

TODO

colcon build --packages-select ros2_basic_test

ros2 launch ros2_basic_test basic_test_launch.py


### custom_msgpack

참고로 이 메시지 전용 패키지는 아래와 같이 만들어야합니다.

ros2 pkg create ros2_basic_topicmsg --build-type ament_cmake --dependencies rclcpp std_msgs  


colcon build --packages-select custom_msgpack

### 참고
builtin_interfaces
  --> https://docs.ros2.org/galactic/api/builtin_interfaces/msg/Time.html

rosidl_default_runtime, rosidl_default_generators
  --> https://github.com/ros2/rosidl_defaults

### ros2_basic_topicmsg


TODO 수행

colcon build --packages-select ros2_basic_topicmsg

ros2 run ros2_basic_topicmsg info_publisher

ros2 run ros2_basic_topicmsg info_subscriber

### ros2_basic_service

TODO 수행

colcon build --packages-select ros2_basic_service

ros2 run ros2_basic_service srv_server

ros2 run ros2_basic_service srv_client

### ros2_basic_action

TODO 수행

colcon build --packages-select ros2_basic_action

ros2 run ros2_basic_action simple_action_server

ros2 run ros2_basic_action simple_action_client

--------------------------------------------

# Camera Test

## <putty 터미널> 카메라 pub

export DISPLAY=:0

xhost +

DTA

sensorws

ros2 run cv_basics cam_pub

## <turboVNC> 화면 보기 테스트

터미널 창을 새로 열어주세요

export DISPLAY=:1

xhost +

DTA

export DISPLAY=:1

cd /data/CHECK/

python3 opencvtest.py

## <putty 터미널> 카메라 보기

화면보기 테스트 하신 창에서 

sensorws

ros2 run cv_basics cam_sub

-------------------------------------


## Lidar Sub 예제

colcon build --packages-select sensor_test_pack

source ./install/setup.bash

ros2 run sensor_test_pack lidar_sub_node



