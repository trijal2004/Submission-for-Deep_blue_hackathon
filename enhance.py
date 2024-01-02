import cv2
import matplotlib.pyplot as plt
import numpy as np

#create image path
def enhance_image(img):

    #make rgb from bgr
    img_bgr=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    template=cv2.imread('/content/pool line.png')
    template=cv2.cvtColor(template, cv2.COLOR_BGR2RGB)

    # Store width and height of template in w and h
    w=template.shape[1]
    h=template.shape[0]

    # Perform match operations.
    res = cv2.matchTemplate(img_bgr, template, cv2.TM_CCOEFF_NORMED)

    # Specify a threshold
    threshold = 0.5
    average_pixel_value = [np.mean(img_bgr[:,:,0]),np.mean(img_bgr[:,:,1]),np.mean(img_bgr[:,:,2])]
    # Store the coordinates of matched area in a numpy array
    loc = np.where(res >= threshold)

    # Draw a rectangle around the matched region.
    for pt in zip(*loc[::-1]):
        img_bgr[pt[1]-3:pt[1] +h+3, pt[0]-3:pt[0] + w+3] = average_pixel_value


    sharpen_filter=np.array([[-1,-1,-1],
                    [-1,9.5,-1],
                  [-1,-1,-1]
    ])
    padded_image = cv2.copyMakeBorder(img_bgr, 2, 2, 2, 2, cv2.BORDER_WRAP)
    img_bgr=cv2.filter2D(padded_image,-1,sharpen_filter)

    blue=img_bgr[:,:,2]

    equ = cv2.equalizeHist(blue)

    inverted_equ=cv2.bitwise_not(equ)


    height, width = inverted_equ.shape

    border_size = 3

    image_cleared = inverted_equ[border_size:height-border_size, border_size:width-border_size]

    return image_cleared