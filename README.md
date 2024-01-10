
# Deep Blue Hackathon 

Submission for Deep Blue hackathon by team **Transformers**.



## Table Of Contents

* [Introduction](#Introduction)
* [Pipeline](#Pipeline)
* [Performance](#Performance)
* [Installation](#Installation)
* [Challenges](#Challenges)
* [Conclusion](#Conclusion)


## Introduction 


#### Problem statement 
The exploration of underwater environments present lots of challenges, particularly in the domain of computer vision and image processing. Among the many complexities, the detection and identification of submerged structures, such as gates, are pivotal for various underwater applications, ranging from marine research to infrastructure maintenance and underwater robotics.

#### Significance of our Submission

Due to the light absorption and scattering, captured underwater images and videos usually contain severe color distortion and contrast reduction. The underwater robots also have less computational power and hence cant afford to run big Deep learning based models on them. 

To address this issue we propose completely raw image processing based algorithm which is computationally less heavy making it suitable for resource-constrained underwater robotic systems and really swift in its runtime operation. 


## Pipeline

![pipeline](https://i.postimg.cc/BQGqMFhT/Screenshot-from-2024-01-03-11-11-30.png)

 

- We finalised ```Retinex``` ,```RGHS filters``` and our own ```customized algorithm``` finally for image preprocessing after trying out various techniques like( GC, ICM and RD barely improved contrast. CLAHE, RGHS and UCM ).

#### Retinex

 The retinex algorithm is applied, to achieve color constancy, to achieve color constancy, which means that the perceived color of an object remains relatively constant under different lighting conditions


#### RGHS
 Red Thresholding: Identify regions in the image where the red component exceeds a certain threshold.
Green Thresholding: Isolate areas in the image where the green component surpasses a predefined threshold.
 Hue-Saturation Thresholding: Determine regions based on specific hue and saturation ranges that correspond to the gate's color.


#### Customized Algo
Template matching with a veritcal pool line to remove it, Sharpens the image further, takes the blue the channel, histogram equalization, then inverts the image followed by border clearing.

#### Detection algorithm

 Finally we used **Adaptive thesholding** followed by **countour detection**, the enclosing the contours into individual BBs and then using geometric properties of BB to filter out the BBs




## Performance

After passing an image through our enhancement + detection algorithm.

![image](https://i.postimg.cc/y8KpQmSz/Untitled.jpg)



## Installation

We created a Dataset on **RoboFlow** which can be accessed seprately using the code snippit given below.     
This labelled dataset is really valuable for testing and training ML models. 

```python
!pip install roboflow

from roboflow import Roboflow
from pycocotools.coco import COCO

rf = Roboflow(api_key="wbs3ef01W1OQTdLhbY9o")
project = rf.workspace("auv-hackathon").project("underwater-object-detection-s8xhb")
dataset = project.version(1).download("coco")


# Specify the path to your COCO annotations JSON file
coco_annotation_file = 'Underwater-object-detection-1/train/_annotations.coco.json'

# Create a COCO instance
coco = COCO(coco_annotation_file)
   
```
#### Requirements
To test code first of all install the requirements :
```
pip install -r requirements.txt
```

#### Run Locally

The run code, simply run the command :
```
python main.py <$path to your images directory>
```

The results will be saved in the [outputs](outputs/) directory




## Challenges 

#### Color Distorted,  Blur and  Limited Visibility of images

- This was the main challenge we faced with the dataset that was given, we went through various image enhancement as well as color restoration algorithms and did a comprehensive litrature reviews of what exactly are the problems and how to tackle them. 
- To list a few image enhancement and color restoration algorithms: GC, ICM, RD, CLAHE, RGHS and UCM. Among all the above listed methods, **RGHS** seemed to give the best results. 
- ```OutputImages``` contains output of all the tried models.
- First we convolve a gaussian function with the image, this was done to get a smoother appearance. This reduces noise and helps is edge detection as edges caused by noise are diminished. The **Retinex algorithm** was then applied, to achieve color constancy, to achieve color constancy, which means that the perceived color of an object remains relatively constant under different lighting conditions.
- Further our **Custom algorithm** was used beacuse pool line removal helps in reducing false BBs and the blue channel is used as the blue is spread throughout the image and is  comparatively lesser near the gate area. This helps remove a lot of unwanted objects before detection.  

#### Computational constraints for detection

- Since we were given the contraint of not using heavy deep learning based models, we faced various difficulties in finding good detection algorithms as moslty object detection research has been DL based only after 2012. 
- We explored **imagenet** Challenges solution before 2010. 
- We tried **clustering algorithms** but due to black tiles the results were bad. 
- **PCA analysis** gave decent results but the water reflection posed a serious challenge here. 
- Since the pixel value of underwater images was almost same, **HOG features + SVM** didn't work too.
- Finally we used **Adaptive thesholding** followed by **countour detection**, the enclosing the contours into individual BBs and then using geometric properties of BB to filter out the BBs.

#### Relfection of gates on water surface and the surrounding noises like Black tiles

- These were the main causes of all the noises we were getting during the detection. 
- After carrying out all the listed algorithms in our pipeline we were able to minimize these noises but still these noises were a big mess.

## Conclusion

We explored almost all the available algorithms and finalized the pipeline we have presented above. The runtime for detection algorithm was barely few milisecond but enhancement part took considerable time causing latency issues. 


### Scope of improvement 

- We didnt have enough time to convert the code into C++, but doing that will automatically descrease the runtime of our code. 
- Latency issues needs to be tackeled properly. 
- Currently since we couldn't reduce the Latency, we are taking images as input and then creating output. When in future we make the code fast, videos can we broken down into frames and then the algorithm can be used.
