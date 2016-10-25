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
    print dataset.image[0]
    cv2.imshow(str(dataset.train_label[0]),dataset.image[0])
    cv2.imshow(str(dataset.train_label[1]),dataset.image[1])
    cv2.imshow(str(dataset.train_label[2]),dataset.image[2])
    cv2.imshow(str(dataset.train_label[3]),dataset.image[3])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
