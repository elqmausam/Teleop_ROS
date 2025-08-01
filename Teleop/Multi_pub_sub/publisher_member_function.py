import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Publisher1
class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

# Subscriber2
class MinimalSubscriberAA(Node):
    def __init__(self):
        super().__init__('minimal_subscriberAA')
        self.subscription = self.create_subscription(
            String,
            'topicb',
            self.listener_callback,
            10)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    minimal_subscriberAA = MinimalSubscriberAA()

    try:
        while rclpy.ok():
            rclpy.spin_once(minimal_publisher, timeout_sec=0.1)
            rclpy.spin_once(minimal_subscriberAA, timeout_sec=0.1)
    except KeyboardInterrupt:
        pass
    finally:
        minimal_publisher.destroy_node()
        minimal_subscriberAA.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
