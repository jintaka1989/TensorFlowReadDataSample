# -*- coding: utf-8 -*-
import os
import glob
import sys
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.python.platform

# 画像を分類するときの分類数
NUM_CLASSES = 6
IMAGE_SIZE = 28
# カラー画像だから*3？
IMAGE_PIXELS = IMAGE_SIZE*IMAGE_SIZE*3

flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('save_model', 'models/model.ckpt', 'File name of model data')
flags.DEFINE_string('train', 'data_set/train.txt', 'File name of train data')
flags.DEFINE_string('test', 'data_set/test.txt', 'File name of test data')
flags.DEFINE_string('train_dir', '/tmp/pict_data', 'Directory to put the data_set data.')
flags.DEFINE_integer('max_steps', 201, 'Number of steps to run trainer.')
flags.DEFINE_integer('batch_size', 256, 'Batch size'
                     'Must divide evenly into the dataset sizes.')
flags.DEFINE_float('learning_rate', 1e-4, 'Initial learning rate.')

class ImageDataSet:
    def  __init__(self):
        # データを入れる配列
        self.train_image = []
        self.train_label = []
        self.image = []

        with open(FLAGS.train, 'r') as f: # train.txt
            for line in f:
                line = line.rstrip()
                l = line.split()
                img = cv2.imread(l[0])
                img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
                self.image.append(img.astype(np.float32)/255)
                self.train_image.append(img.flatten().astype(np.float32)/255.0)
                tmp = np.zeros(NUM_CLASSES)
                tmp[int(l[1])] = 1
                self.train_label.append(tmp)
            self.train_image = np.asarray(self.train_image)
            self.train_label = np.asarray(self.train_label)
            self.train_len = len(self.train_image)

    @staticmethod
    def create_labels(filepath, class_num):
        files = glob.glob(filepath + "/*")
        f = open(os.path.dirname(filepath) + "/class" + str(class_num) + ".txt", "w")
        for file in files:
            f.write(file + " " + str(class_num) + "\n")

        f.close()

    @staticmethod
    def append_labels(filepath, class_num):
        files = glob.glob(filepath + "/*")
        f = open(os.path.dirname(filepath) + "/class" + str(class_num) + ".txt", "a")
        for file in files:
            f.write(file + " " + str(class_num) + "\n")

        f.close()

    @staticmethod
    def create_train_labels(app_root_path, num_of_classes):
        for num in range(0, num_of_classes):
            ImageDataSet.create_labels(app_root_path + "data_set/train/class" + str(num), num)

    @staticmethod
    def create_test_labels(app_root_path, num_of_classes):
        for num in range(0, num_of_classes):
            ImageDataSet.create_labels(app_root_path + "data_set/test/class" + str(num), num)


    # @staticmethod
    # def cat_labels(filepath1, filepath2):
    #     # use cat command
