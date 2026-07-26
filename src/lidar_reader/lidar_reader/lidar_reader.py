import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class LidarReader(Node):

    def __init__(self):
        super().__init__('lidar_reader')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

    def scan_callback(self, msg):
        front_distance = msg.ranges[0]
        self.get_logger().info(f'Front Distance: {front_distance:.2f} m')


def main(args=None):
    rclpy.init(args=args)

    node = LidarReader()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
