#!/usr/bin/env python3
#################################################################################################
#################################################################################################
#                       Program : IMU driver for Xsense MTi-300 AHRS                            # 
#                       Creater : Nontanan Sommat                                               #
#                       Date    : 20/02/2566                                                    #
#                       company : Gensurv                                                       #
#                       Email   : Nontanan Sommat                                               #
#################################################################################################
#################################################################################################
import rclpy
import time
import numpy as np
import ahrs

from rclpy.node import Node
from sensor_msgs.msg import Imu,TimeReference
from std_msgs.msg import String,Float32
from geometry_msgs.msg import QuaternionStamped,Vector3


class Imu_filter(Node):
	def __init__(self):
		super().__init__('Imu_filter')
		self.imu_publisher_ = self.create_publisher(String, '/ang_vel', 10)
		timer_period = 0.5  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback(self):
		msg = String()
		msg.data = 'Hello World: %d' % self.i
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%s"' % msg.data)
		self.i += 1


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('Imu_filter')
        self.Quaternion_sub = self.create_subscription(QuaternionStamped,'/imu/dq',self.quaternion_callback,10)
        self.Acceleration_sub = self.create_subscription(Vector3Stamped,'/imu/dv',self.acceleration_callback,10)
        self.imu_publisher_ = self.create_publisher(QuaternionStamped, '/imu/dq2ang_vel', 10)
        timer_period = 0.01  # seconds
        self.imu = Imu()
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.prev_time = 0.00
        self.curr_time = 0.00
        self.dt = 0.00

    def quaternion_callback(self, dq):
    	self.delta_quaternion = QuaternionStamped()
    	self.delta_quaternion.header = quaternion.header
    	self.imu.header = quaternion.header
    	self.delta_quaternion.quaternion = quaternion.quaternion
    	self.curr_time = float(self.delta_quaternion.header.stamp.sec) + float(self.delta_quaternion.header.stamp.nanosec)/100000000.00
    	self.dt = self.curr_time - self.prev_time
    	self.prev_time = self.curr_time
        # self.get_logger().info('I heard: "%s"' % msg.data)

    def acceleration_callback(self, velocitys):
    	self.acceleration = Vector3()
    	self.acceleration.vector = velocitys.vector
    
    def ang_velocity_calc(self):
    	self.angular_velocity = Vector3()
    	self.angular_velocity.x = (2.00/self.dt)*()

    def linear_acceleration(self):
    	pass

    def timer_callback(self):
    	self.imu_publisher_.publish(self.delta_quaternion)


    # def angular_velocitys(self):
    # 	time = float(self.imu.header.stamp.sec) + float(self.imu.header.stamp.nanosec)/100000000.00
    # 	print(time) 


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
	main()