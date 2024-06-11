#!/usr/bin/env python
#
# Copyright (c) 2024 JetsonAI CO., LTD.
# Author: Kate Kim

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from random import random
#TODO

class InfoTopicPublisher(Node):

    def __init__(self):
        super().__init__('info_publisher')
        qos_profile = QoSProfile(depth=10)
        self.info_publisher = self.create_publisher(String, 'infodata', qos_profile)
        self.timer = self.create_timer(1, self.publish_counter_info)
        self.count = 0

    def publish_counter_info(self):
        #TODO
        msg.id_num = random()
        msg.account = random()
        #TODO
        self.get_logger().info('Published id_num:{0} id_accountnum: {0}'.format(msg.id_num, msg.account))


def main(args=None):
    #TODO
    #TODO
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
