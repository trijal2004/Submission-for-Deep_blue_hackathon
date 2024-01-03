
# encoding=utf-8
import os
import numpy as np
import cv2
import natsort

from LabStretching import LABStretching
from relativeglobalhistogramstretching import RelativeGHstretching

def cal_equalisation(img,ratio):
    Array = img * ratio
    Array = np.clip(Array, 0, 255)
    return Array

def RGB_equalisation(img):
    img = np.float32(img)
    avg_RGB = []
    for i in range(3):
        avg = np.mean(img[:,:,i])
        avg_RGB.append(avg)
    avg_RGB = 128/np.array(avg_RGB)
    ratio = avg_RGB

    for i in range(0,2):
        img[:,:,i] = cal_equalisation(img[:,:,i],ratio[i])
    return img

def stretching(img):
    height = len(img)
    width = len(img[0])
    for k in range(0, 3):
        Max_channel  = np.max(img[:,:,k])
        Min_channel  = np.min(img[:,:,k])
        for i in range(height):
            for j in range(width):
                img[i,j,k] = (img[i,j,k] - Min_channel) * (255 - 0) / (Max_channel - Min_channel)+ 0
    return img



np.seterr(over='ignore')
if __name__ == '__main__':
    pass


# # folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/NonPhysical/RGHS"
# folder = "/home/trijal/Documents/GitHub/Single-Underwater-Image-Enhancement-and-Color-Restoration"
# path = folder + "/midframe"
# files = os.listdir(path)
# files =  natsort.natsorted(files)

# for i in range(len(files)):
#     file = files[i]
#     filepath = path + "/" + file
#     prefix = file.split('.')[0]
#     if os.path.isfile(filepath):
#         print('********    file   ********',file)
#         img = cv2.imread(folder +'/midframe/' + file)
#         # img = cv2.imread('InputImages/' + file)
#         # path = np.unicode(path, 'utf-8')
#         # img = cv2.imread('InputImages/' + file)
#         # img = cv2.imread(np.unicode('InputImages/' + file, 'utf-8'))

#         # print('img',img)
#         height = len(img)
#         width = len(img[0])
        # sceneRadiance = RGB_equalisation(img)

def rghs(img):
        sceneRadiance = img
        # sceneRadiance = RelativeGHstretching(sceneRadiance, height, width)

        sceneRadiance = stretching(sceneRadiance)


        sceneRadiance = LABStretching(sceneRadiance)


        # cv2.imwrite(folder +'/midframe_output/' + prefix + '_RGHS.jpg', sceneRadiance)
        return sceneRadiance
