#Augement synthetic data with colour and lighting variations and blurring

import cv2
import numpy as np
import torch
from torchvision import transforms


#https://kornia.readthedocs.io/en/v0.1.2/_modules/torchgeometry/image/gaussian.html
class GaussianBlur(torch.nn.Module):
    def __init__(self, kernel_size, std_dev):
        super(GaussianBlur, self).__init__()
        self.kernel_size = kernel_size
        self.std_dev = std_dev

    def forward(self, img):
        image = np.array(img)
        image_blur = cv2.GaussianBlur(image, self.kernel_size, self.std_dev)
        return image_blur 

    
def transform_data(brightness_range = 0.75, contrast_range = 0.75, saturation_range = 0.1, hue_range= 0.01):
    rgb_transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.ColorJitter(brightness=brightness_range, contrast=contrast_range, saturation=saturation_range, hue=hue_range),
         transforms.ToTensor()
        ])
    return rgb_transform