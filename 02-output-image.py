# Program to read in bytes and convert them into images - print the images to the screen and save as PNG
# Author: Adrian Sypos
# Date: 13/10/2017

#imports
import gzip
import PIL.Image as pilImage
import numpy as np

def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        # Get the magic number
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is: ", magic)
        # Get the number of labels
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels: ", nolab)
        # Read the labels into an appropriate data structure i.e as array
        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]

        return labels

# A function to read the images
def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        # Get the magic number
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is: ", magic)
        # Get the number of images
        noimages = f.read(4)
        noimages = int.from_bytes(noimages, 'big')
        print("Number of images: ", noimages)
        # Number of rows
        norows = f.read(4)
        norows = int.from_bytes(norows, 'big')
        print("Rows: ", norows)
        # Number of columns
        nocols = f.read(4)
        nocols = int.from_bytes(nocols, 'big')
        print("Columns: ", nocols)

		#initialize array called images
        images = []

		#iterate over images
        for i in range(noimages):
			#initialize rows array
            rows = []
			#iterate rows
            for j in range(norows):
				#initialize cols array
                cols = []
				#iterate cols
                for k in range(nocols):
					#read bytes and append into cols array
                    cols.append(int.from_bytes(f.read(1), 'big'))
				#add cols to corresponding rows
                rows.append(cols)
			#add rows to images array
            images.append(rows)

        return images
		
# function to print image to console	
def print_image(image):
	#iterate rows
    for row in image:
		#iterate cols
        for col in row:
			# print '.' or '#' depending on pixel number (white / black)
            print('.' if col < 128 else '#', end='')
        print()
		
#function to save images
def save_image(image, tag, index, label):
	#output destination
    target = "images/%s-%05d-%d.png"
    
	#array of pixels
    pixels = np.array(image)
	#create an image from array of pixels
    img = pilImage.fromarray(pixels.astype('uint8'))
	#save the picture into the target destination with appropiate label
    img.save(target % (tag, index, label))

#read labels
train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')

#read images
train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')

#print image of X index
print_image(train_images[4999])

for i in range(len(train_images)):
    save_image(train_images[i], 'train', (i+1), train_labels[i])

for i in range(len(test_images)):
    save_image(test_images[i], 'test', (i+1), test_labels[i])