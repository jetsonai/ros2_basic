#!/usr/bin/env python
#
# Copyright (c) 2024 JetsonAI CO., LTD.
# Author: Kate Kim

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String


class BasicTopicPublisher(Node):

    def __init__(self):
        super().__init__('rostopic_pub')
        qos_profile = QoSProfile(depth=10)
        self.counter_publisher = self.create_publisher(String, 'counter', qos_profile)
        self.timer = self.create_timer(1, self.publish_counter_msg)
        self.count = 0

    def publish_counter_msg(self):
        msg = String()
        msg.data = 'Hello ROS2: {0}'.format(self.count)
        self.counter_publisher.publish(msg)
        self.get_logger().info('Published message: {0}'.format(msg.data))
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = BasicTopicPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
