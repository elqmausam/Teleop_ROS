import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisherAA(Node):
    def __init__(self):
        super().__init__('minimal_publisherAA')
        self.publisherAA_ = self.create_publisher(String, 'topicb', 10)
        timer_period = 1.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisherAA_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisherAA = MinimalPublisherAA()
    rclpy.spin(minimal_publisherAA)

  
    
    minimal_publisherAA.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
