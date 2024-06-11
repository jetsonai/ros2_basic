#!/usr/bin/env python
#
# Copyright (c) 2024 JetsonAI CO., LTD.
# Author: Kate Kim

import threading
import time

from custom_msgpack.action import Timer

import rclpy
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node


class BasicActionServer(Node):

    def __init__(self):
        super().__init__('simple_action_server')
        self._goal_handle = None
        self._goal_lock = threading.Lock()
        self._action_server = ActionServer(
            self,
            Timer,
            'timer',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            handle_accepted_callback=self.handle_accepted_callback,
            cancel_callback=self.cancel_callback,
            callback_group=ReentrantCallbackGroup())

    def destroy(self):
        self._action_server.destroy()
        super().destroy_node()

    def goal_callback(self, goal_request):
        """Accept or reject a client request to begin an action."""
        self.get_logger().info('Received goal request')
        return GoalResponse.ACCEPT

    def handle_accepted_callback(self, goal_handle):
        with self._goal_lock:
            # This server only allows one goal at a time
            if self._goal_handle is not None and self._goal_handle.is_active:
                self.get_logger().info('Aborting previous goal')
                # Abort the existing goal
                self._goal_handle.abort()
            self._goal_handle = goal_handle

        goal_handle.execute()

    def cancel_callback(self, goal):
        """Accept or reject a client request to cancel an action."""
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):
        """Execute the goal."""
        self.get_logger().info('Executing goal...')
        start_time = time.time()
        
        # BEGIN PART_2
        update_count = 0
        # END PART_2
        #feedback_msg = Timer.Feedback()
        goal_sec = goal_handle.request.time_to_wait

        # BEGIN PART_4
        while (time.time() - start_time) < goal_sec:
        # END PART_4

            # then stop executing
            if not goal_handle.is_active:
                self.get_logger().info('Goal aborted')
                return Timer.Result()

            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled')
                return Timer.Result()
                
            # BEGIN PART_6
            feedback_msg = Timer.Feedback()
            feedback_msg.time_elapsed = time.time() - start_time
            feedback_msg.time_remaining = goal_sec - feedback_msg.time_elapsed
            self.get_logger().info('Publishing feedback: {0}'.format(feedback_msg.time_elapsed))

            # Publish the feedback
            goal_handle.publish_feedback(feedback_msg)
            
            update_count += 1
            # END PART_6

            # BEGIN PART_7
            time.sleep(1.0)
            # END PART_7

        goal_handle.succeed()

        # BEGIN PART_8
        # Populate result message
        result = Timer.Result()
        result.time_elapsed = time.time() - start_time
        self.get_logger().info('Result'.format(feedback_msg.time_elapsed))
        result.updates_sent = update_count
##########
        return result


def main(args=None):
    rclpy.init(args=args)

    action_server = BasicActionServer()

    # We use a MultiThreadedExecutor to handle incoming goal requests concurrently
    executor = MultiThreadedExecutor()
    rclpy.spin(action_server, executor=executor)

    action_server.destroy()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
