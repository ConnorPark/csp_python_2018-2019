from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path 
import numpy as np
import PIL
import PIL.ImageDraw
import PIL.ImageFont
import textwrap
import time


#-------------------------------------------------------------------------------
def insaniTea_border(width, height, original_image):
    '''
    Returns original image with the insaniTea border in the code. 
    Takes the dimensions of an image and takes the original image itself.
    Gets every even pixel and replaces it with a color that the user inputs. 
    '''
    img = PIL.Image.new('RGBA', (height, width))
    image = np.array(img)
    for row in range(width):
        for column in range(height):
            if (row+column)/5 % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[-row][column] = [255, 127, 127, 50] # pale red, alpha=0
                if width > 60:
                    image[-row][column] = [0, 127, 127, 220]
            
            #if (row+column)/stripe_width in range(1, 20):
             #   image[row][column] = [0, 0, 0, 50]
            else:
                # Odd stripe
                image[row][column] = [255, 0, 255, 0] # magenta, alpha=255
    for row in range(width):
        for column in range(height):
            column = row**2 - 2*row + 1
            if column in range(height):
                image[row][column] = [0, 0, 0, 225]
            #####if row >= 100: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                #####image[row][column] = [255, 127, 127, 0] # pale red, alpha=0
                #if height > 60:
                    #image[row][column] = [0, 127, 127, 220]
            
            #if (row+column)/stripe_width in range(1, 20):
             #   image[row][column] = [0, 0, 0, 50]
            #####else:
                # Odd stripe
                # if row==360 or column==360:
                #     import pdb; pdb.set_trace()
                #####image[row][column] = [255, 0, 255, 255] # magenta, alpha=255
    '''for row in range(height):
        for column in range(width):
            column = row**2 - 2*row + 1
            if column in range(width):
                image[row][column] = [0, 0, 0, 0]'''
    for row in range(width):
        for column in range(height):
            if row in range(width // 6, 5 * width // 6) and column in range(height // 6, 5 * height // 6):
                image[row][column] = [0, 0, 0, 255]
    
    mask_image = PIL.Image.fromarray(image)
    mask_image = mask_image.resize((width, height))
    
    mask_in_use = mask_image
    
    return mask_in_use
    
    #result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    #result.paste(shading, (0, 0), mask=shading)
    #result.paste(original_image, (0,0), mask=mask_in_use)
    #result = PIL.Image.alpha_composite(result, shade)
    #result.paste(black_layer, ((width // 2) - (wlogo - 5), (height // 2) - hlogo), mask=logo) #new change
    #result.paste(logo, ((width // 2) - wlogo, (height // 2) - hlogo), mask=logo)
    #result.paste(qr_code_for_image, (width // 4, height // 4), mask=qr_code_for_image)

def border(width, height, original_image):
    '''
    Outputs the original image with a mask that makes a border around the image.
    Takes the dimension of the original images and the image itself.
    Takes the width and the height divided by 6 on the edge and replaces it with
    a color of the users choice. 
    '''
    img2 = PIL.Image.new('RGBA', (height, width))
    image2 = np.array(img2)
    
    for row in range(width):
        for column in range(height):
            image2[row][column] = [0, 0, 0, 0]
    
    for row in range(width):
        for column in range(height):
            if row in range(width // 6, 5 * width // 6) and column in range(height // 6, 5 * height // 6):
                image2[row][column] = [0, 0, 0, 255]
                
    mask_image_2 = PIL.Image.fromarray(image2)
    mask_image_2 = mask_image_2.resize((width, height))
    
    mask_in_use = mask_image_2
    
    return mask_in_use
    
def shading_for_image(width, height, original_image):
    '''
    Takes the width and height of the original image along with the image itself.
    Outputs an image with a shadow like effect. 
    Makes a mask that turns any pixel with a brightness less than 100 to black 
    in order to make a shadow like effect.
    '''
    img3 = PIL.Image.new('RGBA', (height, width))
    img3.paste(original_image, (0,0))
    #img3.convert("RGB")
    shading_image = np.array(img3)
    
    for row in range(width):
        for column in range(height):
            #if shading_image[row][column][3] != 255:
                #total_value = sum(shading_image[row][column]) - shading_image[row][column][3]
            #else:
                #total_value = 500
            total_value = shading_image[row][column][0] + shading_image[row][column][1] + shading_image[row][column][2]
            print (total_value)
            ##temp_shading = PIL.Image.fromarray(shading_image)
            ##temp_shading.convert("RGBA")
            #if total_value not in range(100, 765):
            if total_value <= 100:
               shading_image[row][column] = [0,0,0,0]
            else:
               shading_image[row][column] = [total_value // 3, total_value // 3, total_value // 3, 100]
            ###shading_image[row][column] = [total_value // 3, total_value // 3, total_value // 3, 100]
            
    shading = PIL.Image.fromarray(shading_image)
    shade = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    shade.paste(shading, (0,0))
    
    shade = shade
    
    return shade
    
def compare_and_contrast_mask(width, height, original_image, current_result):
    #partial_original_image = PIL.Image.new('RGBA', (width, height), (0,0,0,0))
    partial_original_image = PIL.Image.new('RGBA', (width, height))
    '''partial_image = np.array(partial_original_image)
    
    for row in range(width):
        for column in range(height):
            partial_image[row][column] = [0, 0, 0, 0]
    
    for row in range(width):
        for column in range(height):
            if row in range(0, width // 2):
                partial_image[row][column] = [0, 0, 0, 255]
                
    mask_out = PIL.Image.fromarray(partial_image)
    mask_out_image = mask_out.resize((width, height))'''
    #partial_original_image.paste(original_image, (0,0))
    
    partial_curr_result = PIL.Image.new('RGBA', (width, height))
    partial_curr_result.paste(current_result, (0,0))
    partial_result = np.array(partial_curr_result)
    
    
    for row in range(partial_result.shape[0]-1):
        for column in range(partial_result.shape[1]-1):
            if row not in range(width // 2, width-1):
                partial_result[row][column] = [0, 0, 0, 0]
                
    mask_out_2 = PIL.Image.fromarray(partial_result)
    #mask_out_result = mask_out_2.resize((width, height))
    
    partial_original_image.paste(current_result, (0, 0), mask=mask_out_2)
    
    partial_original_image = partial_original_image.resize((width, height))
    
    return partial_original_image
    
    
def combine(width, height, original_image, curr_result):
    
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(original_image)
    axes[1].imshow(original_image)
    fig.savefig('poster.png')
    

def rounded_corners(width, height, original_image, percent_of_side=.3):
    '''
    Takes the dimensions of the original image and the images iteself. Also has 
    a non default argument.
    Draws a mask where it covers everything but the corners of the image and 
    leaves the code like that. 
    '''
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    temp_rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(temp_rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    '''drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                           (width,height),(0,height)],
                            fill=(127,0,127,255))'''
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #drawing_layer.polygon([(0, 0), (height, 0), (height, width), (0, width)])

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
    '''for pixel in range(height):
        for pixel2 in range(width):
            if pixel > 900 and pixel2 > 100 :
                rounded_mask[pixel][pixel2] = [0,0,0,0]'''
    #load = rounded_mask.load()
    temp_rounded_mask= temp_rounded_mask.resize((int(.90 * width), int(.90 * height)))
    
    rounded_mask.paste(temp_rounded_mask, ((width // 2 ) - int(.45 * width), (height // 2 ) - int(.45 * height)))
    
    mask_in_use = rounded_mask
    
    return mask_in_use

def round_corners_one_image(original_image, chosen_mask, code, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    print('Instrucions: Follow the steps below without typos.')
    print('Images are organized in alphabetical order. ')
    time.sleep(1)
    
    picking_mask = raw_input("Which mask would you like? Rounded mask, Border mask or insaniTea? ")
    #set the radius of the rounded corners
    print("What color would you like the border to be?:")
    time.sleep(.5)
    print("You can type: red, green, blue, pruple, white or black.")
    time.sleep(.5)
    print("If you want a custom color type custom")
    picking_color = raw_input()
    
    print("Please input below yes/no you'd like the image shaded")
    shading_yes_no = raw_input()
    
    print ("Enter below what you'd like the text to be: ")
    text = raw_input()
    
    print ("")
    
    print ("Image loading, please wait.")
    directory2 = os.path.dirname(os.path.abspath(__file__))  
    logo_file = os.path.join(directory2, 'unicornlogo.png')
    logo = PIL.Image.open(logo_file)
    width, height = original_image.size
    width2, height2  = logo.size
    
    if width <= 500 or height <= 500:
        if width <= height:
            logo = logo.resize((width//2, width//2))
        if height <= width:
            logo = logo.resize((height//2, height//2))
        width2, height2 = logo.size
    
#-------------------------------------------------------------------------------
    
#-------------------------------------------------------------------------------
    
#-------------------------------------------------------------------------------
 
   
    
    
#Checkered Pattern
    '''
    for row in range(width//200):
        for column in range(height//200):
            drawing_layer.rectangle([(0+row*200,0+column*200),(100+row*200,100+column*200)],
                            fill=(127,0,127,255)) 
            drawing_layer.rectangle([(100+row*200,100+column*200),(200+row*200,200+column*200)],
                            fill=(127,0,127,255))
            drawing_layer.rectangle([(200+row*200,200+column*200),(300+row*200,300+column*200)],
                            fill=(127,0,127,255))
            drawing_layer.rectangle([(300+row*200,300+column*200),(400+row*200,400+column*200)],
                            fill=(127,0,127,255))
            drawing_layer.rectangle([(0+row*200,0+column*200),(100+row*200,100+column*200)],
                            fill=(127,0,127,255))
    '''    
    
#-------------------------------------------------------------------------------
    """if picking_mask.lower() == "rounded mask":
        mask_in_use = rounded_mask
    elif picking_mask.lower() == "border mask":
        mask_in_use = mask_image_2
    else:
        mask_in_use = mask_image
    #if printing_color = red:
     #   printing_color = (255,0,0,255)"""
    
#-------------------------------------------------------------------------------
    #Uncomment the following line to show the mask
    #plt.imshow(rounded_mask)
    #w2 = width // 2
    #h2 = height // 2
    #logo_mask = PIL.Image.new('RGBA', original_image.size, (127,0,127,0))
    #logo_mask
#-------------------------------------------------------------------------------
    wlogo = width2 // 2
    hlogo = height2 // 2 
    
    #new change
    black_layer = PIL.Image.new('RGBA', logo.size, (0,0,0,255))
    #gradient = PIL.GimpGradientFile.curved(width, height)
    
    #new_layer = PIL.image.new('RGBA', original_image.size, (0,0,0,0))
    #new_layer.paste(balck_layer, )
    
    if width >= 700 or height >= 700:
        qr_code_for_image = code.resize((50, 50))
    else:
        qr_code_for_image = code.resize([width//10,width//10])
    # Make the new image, starting with all transparent
    ####Image 1 = freckles Image 2 = fat rec. Image 3 = Rose Image 4 = Tall rec. Image 5 = square
#-------------------------------------------------------------------------------
    
    fontsize = width // 10
    font =  PIL.ImageFont.truetype("../circulat.ttf", fontsize)
        
#-------------------------------------------------------------------------------    
    #pick_check = [0]
    if picking_color == 'red':
        colorchose = (255,0,0,255)
    elif picking_color == 'blue':
        colorchose = (0,0,255,255)
    elif picking_color == 'green':
        colorchose = (0,225,0,255)
    elif picking_color == 'purple':
        colorchose = (255,0,255,255)
    elif picking_color == 'white':
        colorchose = (255,255,255,255)
    elif picking_color == 'black':
        colorchose = (0,0,0,255)
    elif picking_color == "custom":
        print('Enter the red value, then hit enter then repeat for green and blue values')
        time.sleep(0.5)
        #picking_color = raw_input("Please type the RGB value you would like as follows (#, #, #): ")
        red = int(raw_input())
        green = int(raw_input())
        blue = int(raw_input())
        colorchose = (red, green, blue, 255)
    else:
        print('Please type a valid color')
        time.sleep(1)
        print('Enter the red value, then hit enter then repeat for green and blue values')
        #picking_color = raw_input("Please type the RGB value you would like as follows (#, #, #): ")
        red = int(raw_input())
        green = int(raw_input())
        blue = int(raw_input())
        colorchose = (red, green, blue, 255)
        #pick_check[0] = picking_color
        #print (pick_check[0])
            #try:
             #   tuple(picking_color)
            #except TypeError:
             #   pass
        
        
    
#-------------------------------------------------------------------------------

    #shadow = PIL.Image.new('RGBA', original_image.size, (0,0,0,100))
    
    
    
    #masking_check = 0
    
    result = PIL.Image.new('RGBA', original_image.size, colorchose)
    #result.paste(shading, (0, 0), mask=shading)
    
    if shading_yes_no.lower() == 'yes':
        #result.paste(original_image, (0,0), mask=mask_in_use)
        res
        result = PIL.Image.alpha_composite(result, shading_for_image(width, height, original_image))
    #if shading_yes_no == 'no' and masking_check == 0:
    #    result.paste(original_image, (0,0))
     #   result = PIL.Image.alpha_composite(result, shading_for_image(width, height, original_image))
    if shading_yes_no.lower() == 'even shading':
        shadow = PIL.Image.new('RGBA', original_image.size, (0,0,0,100))
        #result.paste(shading, (0, 0), mask=shading)
        result = PIL.Image.alpha_composite(result, shadow)
    
    if picking_mask.lower() == "rounded mask":
        result.paste(original_image, (0,0), mask=rounded_corners(width, height, original_image))
        #masking_check = 1
        #mask_in_use = rounded_corners(width, height, original_image)
    if picking_mask.lower() == "border mask":
        result.paste(original_image, (0,0), mask=border(width, height, original_image))
        #masking_check = 1
        #mask_in_use = border(width, height, original_image)
    if picking_mask.lower() == "insanitea":
        result.paste(original_image, (0,0), mask=insaniTea_border(width, height, original_image))
        #masking_check = 1
        #mask_in_use = insaniTea_border(width, height, original_image)
    if picking_mask.lower() != "border mask" and picking_mask.lower() != "rounded mask" and picking_mask.lower() != "insanitea":
        result.paste(original_image, (0,0))
    
    '''if shading_yes_no.lower() == 'yes':
        #result.paste(original_image, (0,0), mask=mask_in_use)
        result = PIL.Image.alpha_composite(result, shading_for_image(width, height, original_image))
    #if shading_yes_no == 'no' and masking_check == 0:
    #    result.paste(original_image, (0,0))
     #   result = PIL.Image.alpha_composite(result, shading_for_image(width, height, original_image))
    if shading_yes_no.lower() == 'even shading':
        shadow = PIL.Image.new('RGBA', original_image.size, (0,0,0,100))
        #result.paste(shading, (0, 0), mask=shading)
        result = PIL.Image.alpha_composite(result, shadow)'''
    #else:
    #    result.paste(original_image, (0,0), mask=mask_in_use)
    
    result.paste(black_layer, ((width // 2) - (wlogo - 5), (height // 2) - hlogo), mask=logo) #new change
    result.paste(logo, ((width // 2) - wlogo, (height // 2) - hlogo), mask=logo)
    result.paste(qr_code_for_image, (0,0), mask=qr_code_for_image)
    #result.paste(gradient, (0, 0), mask=mask_in_use)
    #new code
    text_width = font.getsize(text)
    
    add_text = PIL.ImageDraw.Draw(result)
    if text_width[0] <= width:
        add_text.text(((width // 2) - (text_width[0] // 2), (height // 2)), text, font=font, fill=(0, 0, 0, 255))
    elif text_width[0] >= width:
        scalar = text_width[0] // width
        wrap_text = textwrap.wrap(text, width=15)  #https://docs.python.org/2/library/textwrap.html#textwrap.TextWrapper.wrap
        for n in range(len(wrap_text)):
            num = 20 * n
            wrap_text_measurment = font.getsize(wrap_text[n])
            wrap_text_width = wrap_text_measurment[0] // 2
            #add_text.text(((width // 2) - 40, (height // 2) + num), str(wrap_text[n]), font=font, fill=(255, 255, 255, 255))
            add_text.text(((width // 2) - wrap_text_width, (height // 8) + num), str(wrap_text[n]), font=font, fill=(0, 0, 0, 255))
        #text = "realllllllllllllllllllllllllllllllllllllllllllllllllllly looooooooooooooooooooooooooooooooooooog"
        print (wrap_text)
    
     
    if picking_mask.lower() == "combine":
        #result.paste(compare_and_contrast_mask(width, height, original_image, result), (0,0))
        new_image = PIL.Image.new("RGBA", (width * 2, height))
        new_image.paste(combine(width, height, original_image, result), (0,0))
        result = new_image
        
    
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
    
def get_qr_codes(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    qr_image_list = [] # Initialize aggregaotrs
    qr_file_list = []
    
    new_directory = os.path.join(directory, "Qr_codes")
    directory_list = os.listdir("Qr_codes") # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(new_directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            qr_file_list += [entry]
            qr_image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return qr_image_list, qr_file_list

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
    qr_image_list, qr_file_list = get_qr_codes(directory)

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print("Image "+str(n+1))
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        curr_code = qr_image_list[n]
        new_image = round_corners_one_image(curr_image, "insaniTea", curr_code) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        
round_corners_of_all_images()