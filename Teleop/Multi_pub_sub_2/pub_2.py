import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class MinimalPublisherAA(Node):
    def __init__(self):
        super().__init__('minimal_publisherAA')
        self.publisherAA_ = self.create_publisher(Float64, 'topicb', 10)
        timer_period = 1.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        print('*********publisherB*********')

        self.x = 0.0
        self.y = 0.0
        self.a = 0.0
        self.b = 1.0
        self.i = 0.0

    def timer_callback(self):
        if self.x == 0.0:
            self.i = 0.0
            self.x += 1.0
            self.y += 1.0
        elif self.y == 1.0:
            self.i = 1.0
            self.y += 1.0
        else:
            self.i = self.a + self.b
            self.a = self.b
            self.b = self.i

        msg = Float64()
        msg.data = self.i
        self.publisherAA_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisherAA = MinimalPublisherAA()
    rclpy.spin(minimal_publisherAA)

    minimal_publisherAA.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
