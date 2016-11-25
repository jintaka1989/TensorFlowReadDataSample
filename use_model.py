# -*- coding: utf-8 -*-

import sys
import os
import numpy as np
import tensorflow as tf
import cv2
import tensorflow.python.platform
from types import *

# read config.ini
import ConfigParser
inifile = ConfigParser.SafeConfigParser()
inifile.read('./config.ini')
NUM_CLASSES = int(inifile.get("settings", "num_classes"))
DOWNLOAD_LIMIT = int(inifile.get("settings", "download_limit"))

IMAGE_SIZE = int(inifile.get("settings", "image_size"))
IMAGE_PIXELS = IMAGE_SIZE*IMAGE_SIZE*3

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('readmodels', 'models/model.ckpt', 'File name of model data')
flags.DEFINE_string('train', 'data_set/train.txt', 'File name of train data')
flags.DEFINE_string('test', 'data_set/test.txt', 'File name of test data')
flags.DEFINE_string('train_dir', '/tmp/pict_data', 'Directory to put the data_set data.')
flags.DEFINE_integer('max_steps', 201, 'Number of steps to run trainer.')
flags.DEFINE_integer('batch_size', 256, 'Batch size'
                     'Must divide evenly into the dataset sizes.')
flags.DEFINE_float('learning_rate', 1e-4, 'Initial learning rate.')

def inference(images_placeholder, keep_prob):
    def weight_variable(shape):
      initial = tf.truncated_normal(shape, stddev=0.1)
      return tf.Variable(initial)

    def bias_variable(shape):
      initial = tf.constant(0.1, shape=shape)
      return tf.Variable(initial)

    def conv2d(x, W):
      return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

    def max_pool_2x2(x):
      return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                            strides=[1, 2, 2, 1], padding='SAME')

    x_image = tf.reshape(images_placeholder, [-1, IMAGE_SIZE, IMAGE_SIZE, 3])

    with tf.name_scope('conv1') as scope:
        W_conv1 = weight_variable([5, 5, 3, 32])
        b_conv1 = bias_variable([32])
        h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)

    with tf.name_scope('pool1') as scope:
        h_pool1 = max_pool_2x2(h_conv1)

    with tf.name_scope('conv2') as scope:
        W_conv2 = weight_variable([5, 5, 32, 64])
        b_conv2 = bias_variable([64])
        h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

    with tf.name_scope('pool2') as scope:
        h_pool2 = max_pool_2x2(h_conv2)

    with tf.name_scope('fc1') as scope:
        W_fc1 = weight_variable([(IMAGE_SIZE/4)*(IMAGE_SIZE/4)*64, 1024])
        b_fc1 = bias_variable([1024])
        h_pool2_flat = tf.reshape(h_pool2, [-1, (IMAGE_SIZE/4)*(IMAGE_SIZE/4)*64])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
        h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

    with tf.name_scope('fc2') as scope:
        W_fc2 = weight_variable([1024, NUM_CLASSES])
        b_fc2 = bias_variable([NUM_CLASSES])

    with tf.name_scope('softmax') as scope:
        y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

    return y_conv

if __name__ == '__main__':

    with open(FLAGS.test, 'r') as f: # test.txt
        test_image = []
        test_label = []
        test_image_name = []
        for line in f:
            line = line.rstrip()
            l = line.split()
            img = cv2.imread(l[0])
            test_image_name.append(l[0])
            img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
            test_image.append(img.flatten().astype(np.float32)/255.0)
            tmp = np.zeros(NUM_CLASSES)
            tmp[int(l[1])] = 1
            test_label.append(tmp)
        test_image = np.asarray(test_image)
        test_label = np.asarray(test_label)
        test_len = len(test_image)

    images_placeholder = tf.placeholder("float", shape=(None, IMAGE_PIXELS))
    labels_placeholder = tf.placeholder("float", shape=(None, NUM_CLASSES))
    keep_prob = tf.placeholder("float")

    logits = inference(images_placeholder, keep_prob)
    sess = tf.InteractiveSession()

    saver = tf.train.Saver()
    sess.run(tf.initialize_all_variables())
    saver.restore(sess,FLAGS.readmodels)

    if test_len % FLAGS.batch_size is 0:
        test_batch = test_len/FLAGS.batch_size
    else:
        test_batch = (test_len/FLAGS.batch_size)+1
        print "test_batch = "+str(test_batch)

    # for i in range(test_batch):
    #     batch = FLAGS.batch_size*i
    #     batch_plus = FLAGS.batch_size*(i+1)
    #     pr = logits.eval(feed_dict={
    #             images_placeholder: test_image[batch:batch_plus]})
    #     pred = np.argmax(pr)
    #     # print pr
    #     jpgname = test_image_name[i].lstrip(os.getcwd() + "/data_set")
    #     print jpgname + (":" + str(pred)).rjust(30-len(jpgname), " ")

    for i in range(len(test_image)):
        pr = logits.eval(feed_dict={
            images_placeholder: [test_image[i]],
            keep_prob: 1.0 })[0]
        pred = np.argmax(pr)
        # print pr
        jpgname = test_image_name[i].lstrip(os.getcwd() + "/data_set")
        print jpgname + (":" + str(pred)).rjust(30-len(jpgname), " ")
    print "finish"
