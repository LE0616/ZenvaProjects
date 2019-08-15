# docs.opencv.org

import cv2
import numpy as np

# dummy function
def dummy(value):
  pass

# define convolution kernels
identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) # puts the most weight on anchor pt and applies less weight to pixels around it
gaussian_kernel1 = cv2.getGaussianKernel(3, 0) # blurring
gaussian_kernel2 = cv2.getGaussianKernel(10, 0) # blurring
box_kernel = np.ones((3, 3), np.float32) / 9.0 # averaging

kernels = [identity_kernel, box_kernel, sharpen_kernel, gaussian_kernel1, gaussian_kernel2]

# read in image, make a grayscale copy
# imS = cv2.resize(im, (960, 540))
image = cv2.imread('davidZip2.jpg')
color_original = cv2.resize(image, (960, 540))
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)

# create the UI (window and trackbars)
cv2.namedWindow('Image Processing')
# arguments: trackbarName, windowName, value (initial val), count (max value), onChange (event handler)
cv2.createTrackbar('contrast', 'Image Processing', 1, 10, dummy)
cv2.createTrackbar('brightness', 'Image Processing', 50, 100, dummy)
cv2.createTrackbar('filter', 'Image Processing', 0, len(kernels)-1, dummy) # TODO: update max val to number of filters
cv2.createTrackbar('grayscale', 'Image Processing', 0, 1, dummy)

count = 1

# main UI loop
while True:
  # read all of the tracker values
  grayscale = cv2.getTrackbarPos('grayscale', 'Image Processing')
  contrast = cv2.getTrackbarPos('contrast', 'Image Processing')
  brightness = cv2.getTrackbarPos('brightness', 'Image Processing') - 50
  kernel_idx = cv2.getTrackbarPos('filter', 'Image Processing')

  # apply filters
  color_modified = cv2.filter2D(color_original, -1, kernels[kernel_idx])
  gray_modified = cv2.filter2D(gray_original, -1, kernels[kernel_idx])

  # apply brightness and contrast
  # cv2.addWeighted: dst = src1*alpha + src2*beta + gamma
  color_modified = cv2.addWeighted(color_modified, contrast, np.zeros_like(color_original), 0, brightness)
  gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros_like(gray_original), 0, brightness)

  # wait for keypress (milliseconds)
  key = cv2.waitKey(100) # returns an integer
  # ord converts integer to character
  if key == ord('q'):
    break
  # to save image
  elif key == ord('s'):
    if grayscale == 0:
      cv2.imwrite('output-{}.png'.format(count), color_modified)
    else:
      cv2.imwrite('output-{}.png'.format(count), gray_modified)
    count += 1

  # show the image
  if grayscale == 0:
    cv2.imshow('Image Processing', color_modified)
  else:
    cv2.imshow('Image Processing', gray_modified)

# TODO: remove this line!
cv2.waitKey(0)

# window cleanup
cv2.destroyAllWindows()
