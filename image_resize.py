import cv2

def resize(fname , width , height):
    image = cv2.imread(fname)
    cv2.imshow('Orignal Image' , image)
    cv2.waitKey(0)
    orignal_height , orignal_width = image.shape[0:2]
    print('Width : ' , orignal_width)
    print('Height : ' , orignal_height)
    
    if(orignal_width>=orignal_height):
        new_img = cv2.resize(image , (width , height))
    else:
        new_img = cv2.resize(image , (height , width))

    return fname , new_img        

file_Name , New_Image =  resize('bird.jpg' ,1280,960 )
cv2.imshow('Resized Image',New_Image)
cv2.waitKey(0)