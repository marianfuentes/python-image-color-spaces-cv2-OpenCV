"""
Created on Sun Aug 16 15:28:04 2020

Pontificia Universidad Javeriana
Procesamiento de Imágenes y Visión 
Taller 1
@author: Marian Fuentes

This file contains a colorImage class with constructor and methods:
-receive image path.
-displayProperties.
-mageGray
-colorizeRGB.
-makeHue.

"""
### Libraries #####

import cv2


###Define for "colorImage" class
class colorImage:
    
    ########  Constructor  #######
    def __init__(self,path):
        #Receives path image of type string
        self.im_path = path
        #Saves image in self
        self.img = cv2.imread(self.im_path)
    
    ####  Methods   ######
    
    def displayProperties(self):
        #Prints image height and width 
        self.shape = self.img.shape
        print("Height", self.shape[0]) #number of rows
        print("Width", self.shape[1]) #number of columns
    
    #Returns gray image
    def makeGray(self):
        self.copy = self.img
        self.gray_img = cv2.cvtColor(self.copy, cv2.COLOR_BGR2GRAY)
        return self.gray_img
    
    #Colorize the image depending on the chosen color.
    def colorizeRGB(self,color):
        
        self.colorized_img = cv2.imread(self.im_path) #copy original image
        
        #Clear image channels
        self.colorized_img[:,:,0] = 0
        self.colorized_img[:,:,1] = 0
        self.colorized_img[:,:,2] = 0
        
        #Colorize image red
        if color == "red":  
            self.colorized_img[:,:,2] = self.gray_img
            return self.colorized_img
        #Colorize image green
        elif color == "green":
            self.colorized_img[:,:,1] =self.gray_img
            return self.colorized_img
        #Colorize image red
        elif color == "blue":
            self.colorized_img[:,:,0] = self.gray_img
            return self.colorized_img
        
        else:
            print("Invalid color")
        
    #Returns image with Hue tones highlighted    
    def makeHue(self):
        
        self.hue_img = cv2.imread(self.im_path) #copy original image
        #change color space from RGB to HSV
        self.HSV_img = cv2.cvtColor(self.hue_img, cv2.COLOR_BGR2HSV)
        
        #S channel changed to 255 constant
        self.HSV_img[:, :, 1] = 255; 
        #V channel changed to 255 constant
        self.HSV_img[:, :, 2] = 255; 
        
        #HSV color space changed to RGB color space
        #return RGB image
        self.RGB_img = cv2.cvtColor(self.HSV_img, cv2.COLOR_HSV2BGR) 
        return self.RGB_img
    

        
