import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random


class EnvironmmentMoniter(Node):
    def __init__(self):
        super().__init__("environmentmoniter")
        self.publisher_ = self.create_publisher(String ,'/home/environmentmointer',10)
        self.timer_ =self.create_timer(2.0,self.publish_environment)
        self.get_logger().info('环境检测器启动.......')

    def publish_environment(self):
        msg  = String()
        temperture  =  random.randint(10,15)        #随即生成10～15之间的温度 用来模拟房间的温度
        humidity    = random.randint(40,80)         #模拟生成房间的湿度变化
        msg.data    = f"房间的温度为:{temperture} 湿度：{humidity}%"
        self.publisher_.publish(msg)
        self.get_logger().info(f'发布环境的数据为{msg.data}')

def main ():
    rclpy.init()
    node  = EnvironmmentMoniter()
    rclpy.spin(node)
    rclpy.shutdown()
