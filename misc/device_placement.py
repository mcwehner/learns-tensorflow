#!/usr/bin/env python

import tensorflow as tf


def main():
	# Creates a graph.
	a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
	b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
	c = tf.matmul(a, b)

	# Creates a session with log_device_placement set to True.
	with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
		print sess.run(c)


if '__main__' == __name__:
	main()
