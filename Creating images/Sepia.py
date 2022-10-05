#****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: Sepia.py
#       Due Date: 12/10/2021
#       Description: This program converts an image to sepia tone.
#
#
#
#
#****************************************************************************************************
from cImage import *

#****************************************************************************************************

def makeSepia(image):
    oldImage = FileImage(image)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    mywin = ImageWin('Sepia tone', width * 2, height)
    oldImage.draw(mywin)

    newIm = EmptyImage(width, height)
    for r in range(height):
        for c in range(width):
            oldPixel = oldImage.getPixel(c, r)
            newR = int(oldPixel.getRed() * 0.393 +
                       oldPixel.getGreen() * 0.769 +
                       oldPixel.getBlue() * 0.189)
            newG = int(oldPixel.getRed() * 0.349 +
                       oldPixel.getGreen() * 0.686 +
                       oldPixel.getBlue() * 0.168)
            newB = int(oldPixel.getRed() * 0.272 +
                       oldPixel.getGreen() * 0.534 +
                       oldPixel.getBlue() * 0.131)
            newPixel = Pixel(newR, newG, newB)
            newIm.setPixel(c, r, newPixel)

    newIm.setPosition(width+1, 0)
    newIm.draw(mywin)
    mywin.exitOnClick()

#****************************************************************************************************

if __name__ == '__main__':
    makeSepia('butterfly.jpg')
