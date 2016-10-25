import sys
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.python.platform
from PIL import Image
import scipy
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from scipy import ndimage
from image_data_set import ImageDataSet

if __name__ == "__main__":
    dataset = ImageDataSet()
    print dataset.image
    ImageDataSet.create_labels("/home/ya65857/tensorflow/study/ReadData/test_data_set/class0", 0)
    ImageDataSet.create_labels("/home/ya65857/tensorflow/study/ReadData/test_data_set/class1", 1)
    ImageDataSet.create_labels("/home/ya65857/tensorflow/study/ReadData/test_data_set/class2", 2)
    ImageDataSet.create_labels("/home/ya65857/tensorflow/study/ReadData/test_data_set/class3", 3)
    ImageDataSet.create_labels("/home/ya65857/tensorflow/study/ReadData/test_data_set/class4", 4)
