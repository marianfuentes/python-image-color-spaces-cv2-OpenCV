"""
Created on Sun Aug 16 18:18:19 2020


Pontificia Universidad Javeriana
Procesamiento de Imágenes y Visión 
Taller 1
@author: Marian Fuentes

This file contains main function. 
Main function uses colorImage constructos and methods:
-Read image.
-Print image properties.
-Show gray scale image
-Colorize and show image.
-Highlight hue tones and show image.


"""
### Libraries ###

import cv2 
from colorImage import *

##### Main function #####
def main():
    
    ########### READ IMAGE ###############
    #Ask the user to enter the image path
    image = colorImage(input("Enter your image path \n"))
    #Show original image in a window
    cv2.imshow('Original image', image.img)
    #wait indefinitely for a key stroke (e.g press "enter" to continue running)
    cv2.waitKey(0)
    cv2.destroyAllWindows() #destroy all the windows we created
    
    ############ PRINT PROPERTIES #########
    #Print image height and width
    image.displayProperties()
    
    ########### SHOW GRAY IMAGE ##########
    #Apply gray method
    grayim = image.makeGray()
    #Show gray image in a window
    cv2.imshow('Gray Image', grayim)
    #wait indefinitely for a key stroke (e.g press "enter" to continue running )
    cv2.waitKey(0)
    cv2.destroyAllWindows() #destroy all the windows we created
    
    ########### COLORIZE IMAGE ############
    #Ask user to enter a color between red, green or blue in order to colorize image.
    colorizedim = image.colorizeRGB(input("Enter a color (red, green or blue) \n"))
    #Show colorized image in a window
    cv2.imshow('Colorized Image', colorizedim)
    #wait indefinitely for a key stroke (e.g press "enter" to continue running)
    cv2.waitKey(0)
    cv2.destroyAllWindows() #destroy all the windows we created
    
    
    ########## HIGHLIGHT IMAGE (HUE) TONES  #######
    #Apply makeHue method
    hueim = image.makeHue()
    #Show image in a window
    cv2.imshow('Hue Image', hueim)
    #wait indefinitely for a key stroke (e.g press "enter" to continue running)
    cv2.waitKey(0)
    cv2.destroyAllWindows() #destroy all the windows we created
 

######## CALL MAIN ################
main()