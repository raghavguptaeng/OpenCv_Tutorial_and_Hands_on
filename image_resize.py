import cv2
import sys
import os
import fnmatch
import numpy as np

#following function will tell us how to process images in a huge batch

# Below is the function which will be used to blur our image using average value method
def blur(image):
    kernels = [3,5,9,13] #this is also referes as convolution matrix
    for idx , k in enumerate(kernels):
        image_blur = cv2.blur(image , ksize = (k , k))
        cv2.imshow(str(k) , image_blur) # more the kernel value would be , more the image will be blurred out
        cv2.waitKey(0)
    return True;
# Below is the function which will be used to sharpen up our image 
def sharpen(image):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]]) # following values were taken using GIMP (Google it)
    new_Image = cv2.filter2D(image , -1 , kernel) 
    cv2.imshow('Sharpned Image',new_Image)
    cv2.waitKey(0)
    return True;
# Below is the function which will be used to resize our image 
def resize(fname , width , height):
    image = cv2.imread(fname)
    #cv2.imshow('Orignal Image' , image)
    cv2.waitKey(0)
    orignal_height , orignal_width = image.shape[0:2]
    print('Width : ' , orignal_width)
    print('Height : ' , orignal_height)
    
    if(orignal_width>=orignal_height):
        new_img = cv2.resize(image , (width , height))
    else:
        new_img = cv2.resize(image , (height , width))

    return fname , new_img        
listOfFiles = os.listdir('.')
pattern = "*.jpg"
n = len(sys.argv)
if n==3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    width = 1280
    height = 960
if not os.path.exists('new_folder'):
    os.mkdir('new_folder')
for filename in listOfFiles :
    if fnmatch.fnmatch(filename , pattern):
        file_Name , New_Image =  resize(filename ,width,height )
        cv2.imwrite("new_foldr\\"+filename , New_Image)
# cv2.imshow('Resized Image',New_Image)
# cv2.waitKey(0)
# blur(New_Image)
# sharpen(New_Image)
