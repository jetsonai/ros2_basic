#!/usr/bin/env python
#
# Copyright (c) 2024 JetsonAI CO., LTD.
# Author: Kate Kim

from custom_msgpack.srv import WordCount

import rclpy
from rclpy.node import Node


class BasicService(Node):

    def __init__(self):
        super().__init__('srv_server')
        self.srv = self.create_service(WordCount, 'word_count', self.word_count_callback)

    def word_count_callback(self, request, response):
        response.count = len(request.words.split())
        self.get_logger().info('response: %d request: %s' % (response.count, request.words))

        return response


def main(args=None):
    rclpy.init(args=args)

    basic_service = BasicService()

    rclpy.spin(basic_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
