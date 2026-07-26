import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

    def scan_callback(self, msg):

        front = msg.ranges[0]

        twist = Twist()

        if front > 0.5:
            twist.linear.x = 0.2
            twist.angular.z = 0.0
            self.get_logger().info("Moving Forward")

        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.5
            self.get_logger().warn("Obstacle! Turning Left")

        self.publisher.publish(twist)


def main(args=None):
    rclpy.init(args=args)

    node = ObstacleAvoidance()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
