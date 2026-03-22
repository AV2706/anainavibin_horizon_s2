import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random
#this node publishes random numbers to the /distance topic every second
class sensorNode(Node):
	def __init__(self):
		super().__init__('sensor_node')
		#create a publisher for the '/distance' topic using Int32 messages
		self.publisher_ = self.create_publisher(Int32, 'distance', 10)
		#timer to trigger the callback every second
		self.timer = self.create_timer(1.0, self.timer_callback)
		
	def timer_callback(self):
		msg = Int32()
		#generate random distance
		
		msg.data = random.randint(0, 100)
		self.publisher_.publish(msg)
		self.get_logger().info(f'Publishing distance: {msg.data}')
		
def main(args=None):
	rclpy.init(args=args)
	node = sensorNode()
	rclpy.spin(node)
	rclpy.shutdown()
	