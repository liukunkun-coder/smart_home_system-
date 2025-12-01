import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
import time

from example_interfaces.action import Fibonacci

class Securitypatrol(Node):
    def __init__ (self):
        super().__init__('security_patrol')
        self.action_sever = ActionServer(
            self,
            Fibonacci,
            '/patrol_home',
            self.execute_patrol_callback,
        )
        self.get_logger().info("安防巡逻启动....")


    def execute_patrol_callback(self,goal_handle:ServerGoalHandle):
        self.get_logger().info("开始执行安全执行任务")


        patrol_points = ['大门','客厅','厨房','卧室','阳台']
        feedback_msg =  Fibonacci.Feedback()
        result       =  Fibonacci.Result()


        for i ,point in enumerate(patrol_points):
            if  goal_handle.is_cancel_requested:
                goal_handle.canceled()
                result.sequence = [0]
                self.get_logger().info('巡逻任务取消')
                return result
            
            progress = (i+1)*20
            self.get_logger().info(f'正在巡逻{point},巡逻进度{progress}%')
            time.sleep(1)


            #更新反馈
            feedback_msg.sequence = [progress]
            goal_handle.publish_feedback(feedback_msg)
        
        goal_handle.succeed()
        result.sequence = [100]
        self.get_logger().info('安防巡逻完成')
        return result


def main ():
    rclpy.init()
    node = Securitypatrol()
    rclpy.spin(node)
    rclpy.shutdown()