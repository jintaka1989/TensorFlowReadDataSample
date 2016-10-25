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
