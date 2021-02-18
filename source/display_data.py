'''
Display the RGB and depth images for a frame for chosen object and sequence.
Values can be chosen in initialise() function.
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


def initialise():
    path_to_dataset = "E:/test_data/"
    object = "20200815_174404"
    action = "" #RH, BH 0, 1 ...
    frame_number = 0

    return path_to_dataset, object, action, frame_number

def main(path_to_dataset, object, action, frame_number):


    # ----------- Load rgb and depth images -----------

    RGB_folder = os.path.join(path_to_dataset, object,'RGB/')
    depth_folder = os.path.join(path_to_dataset, object,'D/')

    rgb_image = cv2.imread(RGB_folder + str(frame_number) + ".png")
    rgb_image =cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)
    depth_image = cv2.imread(depth_folder + str(frame_number) + ".png")

    # ----------- Display using matplotlib -----------

    fig = plt.figure()
    fig.suptitle("Object " + object + " at frame " + str(frame_number))
    fig.add_subplot(1,2,1)
    plt.imshow(rgb_image)
    plt.title("RGB")
    fig.add_subplot(1,2,2)
    plt.imshow(depth_image)
    plt.title("Depth")
    plt.show()




if __name__ == '__main__':

    path_to_dataset, object, action, frame_number = initialise()
    main(path_to_dataset, object, action, frame_number)