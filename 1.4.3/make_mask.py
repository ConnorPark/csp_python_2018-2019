import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import PIL

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)

    for row in range(420,500):
        for column in (270, 300):
            img[row][column]=[34,98,120]
                
                
    for row in range(rows):
        for column in range(columns):
            if (row+column+72)/stripe_width % 2 == 0: 
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
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask')            
              
