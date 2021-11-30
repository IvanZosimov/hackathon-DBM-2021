import os
import matplotlib.pyplot as plt
import shutil
import json
import numpy as np
import io
import cv2
from PIL import Image
from tqdm import tqdm_notebook
from moviepy.editor import *
from base64 import b64encode
import cv2
import os
import numpy as np
import utils
import torch
from IPython.display import Image, clear_output

from IPython.display import Image
#import yolov5.detect
from yolov5.detect import run

print(torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU')
#source='./yolov5/testImages/'q

# vid = cv2.VideoCapture("/dev/video0")
# vid.open(0, cv2.CAP_DSHOW)

run(conf_thres=0.9, source=0, weights='./yolov5/hakvelon_model.pt', save_txt=True, save_conf=True, classes=[0, 1, 2], save_crop=True)
# exit(0)
# # # cv2.namedWindow("test")
# vid = cv2.VideoCapture(0)
# if not vid.isOpened():
#     print("Error opening video")
# while (True):
#
#     # Capture the video frame
#     # by frame
#     ret, frame = vid.read()
#
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
#
#
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # After the loop release the cap object
# vid.release()
# # Destroy all the windows
# cv2.destroyAllWindows()
#
# # perform detection
#
#
# run(img=512, conf_thres=0.5, source='/testImages/', weights='hakvelon_model.pt', save_txt=True, save_conf=True, save_crop=True)
# #!python detect.py --weights 'C:\Python\Freelance\BlackSwanTechnology\Hakvelon\hakvelon_model.pt' --img 512 --conf 0.5 --source 'C:\Python\Freelance\BlackSwanTechnology\Hakvelon\testImages\' --save-txt --save-conf