# Problem set: Read the MNIST data files

## Introduction
These problems relate to the famous MNIST data set. The files are in a bespoke format, as described on this website http://yann.lecun.com/exdb/mnist/

## Assignment Specification

__1. Read the data files__

Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

__2. Output an image to the console__

Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.

__3. Output the image files as PNGs__

Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.

## How to clone this repository

* In the Clone with HTTPs section, copy the clone URL for the repository.
* Open Git Bash.
* Change the current working directory to the location where you want the cloned directory to be made.
* Type `git clone`, and then paste the URL you copied in Step 2.
* Press Enter. Your local clone will be created.
