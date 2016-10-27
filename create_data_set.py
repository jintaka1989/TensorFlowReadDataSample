import sys
import os
import commands as cmd
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

NUM_CLASSES = 6

if __name__ == "__main__":
    app_root_path = os.getcwd() + "/"
    ImageDataSet.create_train_labels(app_root_path, NUM_CLASSES)
    ImageDataSet.create_test_labels(app_root_path, NUM_CLASSES)
