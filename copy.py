directory = os.path.dirname(os.path.abspath(__file__))  
logo_file = os.path.join(directory, 'unicornlogo.png')
logo = PIL.Image.open(logo_file)
fig, axes = plt.subplots(1, 1)
#axes[0].imshow(student_img, interpolation='none'



def images(): 
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
    for n in range(len(image_list)):
            # Parse the filename
            print(n)
            filename, filetype = os.path.splitext(file_list[n])
            
            # Round the corners with default percent of radius
            curr_image = image_list[n]
            new_image = curr_image
            width, height = new_image.size
            h2 = height % 2
            w2 = width % 2
            new_image.paste(logo, (w2 , h2), mask=logo)
            #new_img = PIL.Image.open(curr_image)
            #new_image = round_corners_one_image(curr_image) 
            
            # Save the altered image, suing PNG to retain transparency
            new_image_filename = os.path.join(directory, filename + '.png')
            new_image.save(new_image_filename)
    return image_list, file_list