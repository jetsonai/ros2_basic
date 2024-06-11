#!/usr/bin/env python
#
# Copyright (c) 2024 JetsonAI CO., LTD.
# Author: Kate Kim


from action_msgs.msg import GoalStatus
from custom_msgpack.action import Timer

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node


class BasicActionClient(Node):

    def __init__(self):
        super().__init__('simple_action_client')
        self._action_client = ActionClient(self, Timer, 'timer')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def feedback_callback(self, feedback):
        self.get_logger().info('Received feedback time_elapsed: {0}'.format(feedback.feedback.time_elapsed))

    def get_result_callback(self, future):
        result = future.result().result
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Goal succeeded! time_elapsed: {0}'.format(result.time_elapsed))
        else:
            self.get_logger().info('Goal failed with status: {0}'.format(status))

        # Shutdown after receiving a result
        rclpy.shutdown()

    def send_goal(self):
        self.get_logger().info('Waiting for action server...')
        self._action_client.wait_for_server()

        goal_msg = Timer.Goal()
        goal_msg.time_to_wait = 5.0

        self.get_logger().info('Sending goal request...')

        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)


def main(args=None):
    rclpy.init(args=args)

    action_client = BasicActionClient()

    action_client.send_goal()

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
