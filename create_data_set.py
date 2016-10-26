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
    app_root_path = "/home/ya65857/tensorflow/study/TensorFlowReadDataSample/"
    ImageDataSet.create_labels(app_root_path + "data_set/train/class0", 0)
    ImageDataSet.create_labels(app_root_path + "data_set/train/class1", 1)
    ImageDataSet.create_labels(app_root_path + "data_set/train/class2", 2)
    ImageDataSet.create_labels(app_root_path + "data_set/train/class3", 3)
    ImageDataSet.create_labels(app_root_path + "data_set/train/class4", 4)
    ImageDataSet.create_labels(app_root_path + "data_set/test/class0", 0)
    ImageDataSet.create_labels(app_root_path + "data_set/test/class1", 1)
    ImageDataSet.create_labels(app_root_path + "data_set/test/class2", 2)
    ImageDataSet.create_labels(app_root_path + "data_set/test/class3", 3)
    ImageDataSet.create_labels(app_root_path + "data_set/test/class4", 4)
