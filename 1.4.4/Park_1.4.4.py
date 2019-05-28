'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_eye')

#13
'''
matplotlib.pyplot is used to plot points onto graphs and to create graphs for the
user. 
'''

'''
numpy is a library that includes arrays, and high mathematics to operate the 
arrays.
'''

'''
PIL is the Python Imaging library. It changes images to objects that the user 
can manipulate and change. 
'''
#15
'''
a)
Line 19 calls the function subplots() from the matplotlib library. The function 
is being called with two arguments. : 1 and 2. The function returns two objects, 
which are being assigned to fig and ax. 
'''

'''
b)
Line 20 calls imshow() on ax[0]
Line 23 calls imshow() on ax[1]
Line 24 calls set_xsticks() on ax[1]
Line 25 calls set_xlim() on ax[1]
Line 26 calls set_ylim() on ax[1]
Line 27 calls savefig() on fig
'''

'''
c)
The coordinates are (1162,996)
'''
#16
'''
1010, 950
720, 770
'''
#17
'''
a)Line 30 uses the join() method from the os.path module. It is being passed
 2 arguments. The value it returns is being assigned to the variable 
earth_file.
'''

'''
b)In line 31 the open() function of the PIL.Image module returns a new 
PIL.Image object, which is being assigned to the variable earth_img'''

'''
c)If there was only one pair of parenthesis, the tuple would not be identified.
Therefore, the code would not identify a tuple.'''

'''
d)The (89,87) tells us about the width and the height of the image. Without it,
the code would not be able to resize the figure. 
'''

'''
e)
Line 33 calls the function subplots from the matplotlib library with 2 arguments:
1 and 2. The function returns 2 object(s), which is/are being assigned to 
fig2, axes2.

Line 34 calls the method imshow on the object axes2[0] with 1 argument(s): 
earth_img. 

Line 35 calls the method imshow on the object axe2[1] with 1 argument:
earth_small

Line 36 calls the method savefig on the object fig2. with 1 argument:
'resize earth'
'''

'''
f)
    i)You can add a filter or you can add the size
    ii)The default of the filter is nearest
    iii)
'''

'''
g)
The size attribute is representing a two tuple. 
'''

'''
h)
The first output is the width and height of the original earth that's on the left.
The second output is the width and height of the second earth.
The third output is the width of the second row. 
'''

'''
i)
You can tell that the images are different sizes by looking at the graphs rows
and columns. They all have different values. The axes on the first image have a 
higher value than the ones on the left. 
'''

#18
'''
The resize funtion groups the pixels to what the users need for their size. Then
it gets the average color of each pixel in the group, making a smaller image. 
'''

#19
'''
a)
student_img bytes = 479 * 475 * 3 = 682,575
earth_small bytes = 89 * 87 * 4 = 30972
'''

'''
c)
student.jpg bytes = 206 kb
earth_small.png bytes = 18.3 kb
'''

'''
d)
There is an discreptancy because the files are acutally two different files. So
naturally, they have different amounts of byes
'''

'''
e)
The function will set the group of pixels as the color that was given to us. 
'''

'''
f)
If both images are different, then they are converted into one format.
'''

'''
g)
The first argument is the small earth with the right amount. The second argument
is the coordinate that the earth should be pasted on. The third argument is the 
earth becoming the mask.
'''
#20
student_img.paste(earth_small, (695, 940), mask=earth_small) 
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_eyes2')
#Colclusion Questions
#1
'''
We used the classes from the matplotlib library and the Python imaging library. 
Most of the code comes from the two libraries. 
'''
#2
'''
All of the comments that are organized helps with the abstraction. It divides up
everything to make the user able to understand the code.
'''