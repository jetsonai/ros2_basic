#!/usr/bin/env python
#
# Copyright (c) 2024 JetsonAI CO., LTD.
# Author: Kate Kim

from custom_msgpack.srv import WordCount

import rclpy
from rclpy.node import Node


class BasicClient(Node):

    def __init__(self):
        super().__init__('srv_client')
        #TODO
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        #TODO

    def send_request(self):
        #TODO
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    #TODO
    #TODO

    while rclpy.ok():
        rclpy.spin_once(basic_client)
        if basic_client.future.done():
            response = basic_client.future.result()
            basic_client.get_logger().info('response: %d' % (response.count))

            break

    basic_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
