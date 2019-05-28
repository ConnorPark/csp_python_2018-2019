#4
"""Arrays and lists are both able to store data and be able to iterate through 
it. The difference is that Arrays can have the values and perform mathematical 
operations."""
#5
from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np  # 'as' lets us use standard abbreviations
import PIL

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
#ax.imshow(img, interpolation='none')
# Saves the figure
'''
Height:960
Width:584
Green Intensity(5,9,1):94
Red Intensity(4,10,0):62
Red Intensity(24,49,0):75
'''
#6
###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])


#7
###
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
#fig.savefig('woman_sky_earing')
###
# Show the image data
###
'''
a)
Lines 28-31 is stating that if the pixels in the range of 0 and 155 height wise 
and if the pixels brightness is greater than 500, the color will be changed to 
magenta.
'''
#8
#9
#directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
#filename = os.path.join(directory, 'woman.jpg')
#filename2 = os.path.join(directory, 'mask.png')
# Read the image data into an array
#img = plt.imread(filename)
#img2 = plt.imread(filename2)
ax[0].imshow(img)
def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    
    for row in range(rows):
        for column in range(columns):
            if (row+column+72)/stripe_width % 3 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [212, 85, 200, 8] # pale red, alpha=0
            
            else:
                # Odd stripe
                image[row][column] = [24, 0, 105, 45] # magenta, alpha=255
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
   
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    

    
ax[1].imshow(image)
fig.savefig('woman_mask')

#Conclusions
#1
'''Digital images contain pixels in rows and columns. They also contain information
on the amount of each color of the RGB spectrum. It is possible to alter the 
RGB value of each pixel. '''
#2
'''Photographs with film and digital photos both show a photo with color on it.
Photographs with digital photos however, digital photos can have the color edited.'''
#3
'''
a)The 6 digits represent information, and they don't represent anything about the
image itself.
b)With 6 digits, you can make more than 720 combinations, way more than 63.
c)The RGB color is changed so that we get a different image altogether.
'''
#4
'''The algorithm can look at the image, and analyze each individual pixel. Then
they can find the color and look for the corresponding RGB value.  '''