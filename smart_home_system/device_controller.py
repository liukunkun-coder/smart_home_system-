import rclpy
from  rclpy.node import Node
from custom_interfaces.srv import SetDeviceStatus

class DeviceController (Node):
    def __init__(self):
        super().__init__('device_controler')
        self.service = self.create_service(SetDeviceStatus,'/control_device',self.control_device_callback)
        self.get_logger().info('设备控制其启动，等待服务中')

    def control_device_callback(self,request,response):
        device_name = request.device_name
        status = "开启" if request.status else "关闭"

        self.get_logger().info(f'收到设备请求 {device_name}->{status}')

        response.success = True
        response.message = f"设备{device_name}应成功{status}"

        return response
    
def main ():
    rclpy.init()
    node  =  DeviceController()
    rclpy.spin(node)
    rclpy.shutdown()