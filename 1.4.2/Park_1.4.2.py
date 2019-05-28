#4
'''
C:/Users/Studentlogin/Desktop/nice.jpg
'''
#5
'''
..Users/Studentlogin/Desktop/nice.jpg
'''
#6
'''
In cloud 9 there are no base files, as there arent as many compared to windows.
'''
#7

'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[0].set_xlim(10,20)
ax[1].set_xlim(20,30)
ax[2].set_xlim(30,40)
ax[0].set_ylim(70,80)
ax[1].set_ylim(50,60)
ax[2].set_ylim(60,70)
# Show the figure on the screen
# fig.show()
fig.savefig('three_closeups')
#a
'''
The nose is at (420,250)
'''
#b
'''
The tip of the nose is at (484,224)
'''
'''When I ran the first set of code, the program crashed already, and the ipython
session wasnt useable. The reason that the first set of code doesn't work is 
because ipython isnt a GUI, so we need to make the code usable for non GUI 
interfaces. '''
#8
#a
'''
fig is an instance of the class Figure
ax is an instance of the class AxesSubplot
'''
#b
'''
Simlilarly, in line 25, the method savefig() is being called on the object fig.
That method is being given 1 argument. That method is a method of the class
Figures.
'''
#c
'''
Each comment explains the line of code below the comment, except for lines 37 
and 38, because there are 2 comments instead of one. 
'''
#9
#a
'''The method imshow() is being called on the object ax'''
"""
#10
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig('leaf_earing2')"""
'''Interpolation is adding something different to what it is added into. The
interpolation in pythong mixes up the two colors, making it look prettier. 
Otherwise, the picture would look pixelized. '''

#11 N/A
#12
'''The agg_filter is an argument that filters the dpi of a color.'''
#13
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1,1)
# Show the image data in a subplot
ax.imshow(img)
ax.plot(39, 43, 'ro')
ax.plot(119, 41, 'ro')
ax.plot(140, 40, 'ro')
# Show the figure on the screen
# fig.show()
fig.savefig('crazy_mice')

#Conclusion questions
#1
'''Absolute filenames and relative filenames both start at the root from the 
files. Absolute files specify all of the folders while relative files don't.'''
#2
'''An object is something in python that we can modify and change visually however
we want. '''
#3
'''Methods are things that the object can do and Functions can have many methods.'''
#4
'''When the method is being called on the object, the method is looked through 
in the dictionary. If it's not there, an error would occur.'''
