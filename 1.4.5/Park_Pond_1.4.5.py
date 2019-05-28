from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw            

def round_corners_one_image(original_image, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-3*radius, height-5*radius, width, height), 
                            fill=(0,127,100,255)) #bottom right

    # Uncomment the following line to show the mask
    plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def round_corners_of_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = round_corners_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        
round_corners_of_all_images()
#5
'''
The names of the three functions are round_corners_of_all_images, get_images
and round_corners_one_image.
'''
#6
'''
The function gets all of the images and gives all of them rounded corners. 
'''
#7
'''
a)
Argument 1:original_image
Argument 2:percent_of_side
Return value: PIL image with rounded corners
'''

'''
b)
The color is purple. 
'''

'''
c)
Line 26: rounded_mask
Line 27: drawing_layer
'''

'''
d)
The alpha value should be 0 because then it makes the mask invisible. 
'''

'''
e)
33-38: Square mask
41-48: Circle mask
'''

'''
f)
If it was RGB it would be black, but since it's RGBA, it's transparent.
'''

'''
g)
The color values of the corners is blalck, but the result is transparent. 
'''

#8
'''
a)
Because a default value is specified for directory, that argument is optional, 
so get_images() can be passed either 0 or 1 arguments.
'''

'''
b)
There are 2 objects that are being returned and they are a 2 tuple.
'''

'''
c)
os.getcwd()
os.listdir()
os.path.join()
'''

'''
d)
Return a list containing the names of the entries in the directory given by path.
'''

'''
e)
The program usesthe try except block because if there is an error which is common, 
then the code won't stop at random. The advantage is that you can have errors 
that you need to ignore. The disadvantage is that it can ignore a pretty important
error that has to stop the code. 
'''

'''
f)
When you get an IOError, then the program ignores those kinds of errors. 
'''

#9
'''
a)
We need to have a try except structure because if we already have a new directory
with the same name, then there would be another one. 
'''

'''
b)
len(image_list) represents all the image and it is going through all of the 
images. 
'''

'''
c)
n goes through all the images in the image list, otherwise known as a stepper.
'''

#Conclusion Questions

#1
'''
This is possible by making the edges of the icon have an A value of zero.( in 
RGBA). If the image was only RGB, then the image would be a rectangle. 
'''

#2
'''
This makes the coed reuse easier because if there is an error in the code, you 
can check the code more easily because all you have to do is look at one section 
of the code. 
'''

#3
'''
I agree with Alice. Every image is manipulated in some way. Even our eyes 
manipulate what we see. Some people have perfect vision and some people have to 
wear glasses. Nobody is able to see the real image because everyone have different
kinds of vision. 
'''

#4
'''
An image is yours if you created it or if you took the picture. There are some 
limitations, as you are not able to draw many disney characters and you can't 
take pictures of certain things. If you were to use someones image on the 
internet, you would need their permission unless you are using it for personal 
uses. If you were to use someones photo for buisness and you don't get their 
permission, then you can be sued by that person. 
'''

#5
'''
For this project, my partner and I worked seperatly. It wasn't ideal, because 
when one of us needed help, the other one was usually behind. So next time if we 
were on the same page, then we might be able to finish this project more quickly.
'''