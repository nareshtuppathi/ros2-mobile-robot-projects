import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class SmartObstacleAvoidance(Node):

    def __init__(self):
        super().__init__("smart_obstacle_avoidance")

        self.scan_sub = self.create_subscription(
            LaserScan,
            "/scan",
            self.scan_callback,
            10
        )

        self.cmd_pub = self.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        self.safe_distance = 0.5

        self.get_logger().info("Smart Obstacle Avoidance Started!")

    def scan_callback(self, msg):

        front = min(min(msg.ranges[0:20]), min(msg.ranges[-20:]))

        cmd = Twist()

        if front > self.safe_distance:
            cmd.linear.x = 0.2
            cmd.angular.z = 0.0
        else:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0

        self.cmd_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)

    node = SmartObstacleAvoidance()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
