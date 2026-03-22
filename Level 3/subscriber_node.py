import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class subscriberNode(Node):
	def __init__(self):
		super().__init__('subscriber_node')
		#creating a subscription to '/distance' topic
		self.subscription = self.create_subscription(
		Int32, 'distance', self.listener_callback,10)
		
	def listener_callback(self, msg):
	
	#print recieved distance value to the terminal 
		self.get_logger().info(f'Received distance: {msg.data}')
		
def main(args=None):
	rclpy.init(args=args)
	node = subscriberNode()
	rclpy.spin(node)
	rclpy.shutdown()