# docs.opencv.org

import cv2
import numpy as np

# dummy function
def dummy(value):
  pass

# read in image, make a grayscale copy
# imS = cv2.resize(im, (960, 540))
image = cv2.imread('davidZip.jpg')
color_original = cv2.resize(image, (540, 960))
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)

# create the UI (window and trackbars)
cv2.namedWindow('Image Processing')
# arguments: trackbarName, windowName, value (initial val), count (max value), onChange (event handler)
cv2.createTrackbar('contrast', 'Image Processing', 1, 100, dummy)
cv2.createTrackbar('brightness', 'Image Processing', 50, 100, dummy)
cv2.createTrackbar('filter', 'Image Processing', 0, 1, dummy) # TODO: update max val to number of filters
cv2.createTrackbar('grayscale', 'Image Processing', 0, 1, dummy)


# main UI loop
while True:
  # read all of the tracker values
  grayscale = cv2.getTrackbarPos('grayscale', 'Image Processing')
  contrast = cv2.getTrackbarPos('contrast', 'Image Processing')
  brightness = cv2.getTrackbarPos('brightness', 'Image Processing') - 50

  # apply filters

  # apply brightness and contrast
  # cv2.addWeighted: dst = src1*alpha + src2*beta + gamma
  color_modified = cv2.addWeighted(color_original, contrast, np.zeros_like(color_original), 0, brightness)
  gray_modified = cv2.addWeighted(gray_original, contrast, np.zeros_like(gray_original), 0, brightness)

  # wait for keypress (milliseconds)
  key = cv2.waitKey(100) # returns an integer
  # ord converts integer to character
  if key == ord('q'):
    break
  # to save image
  elif key == ord('s'):
    pass

  # show the image
  if grayscale == 0:
    cv2.imshow('Image Processing', color_modified)
  else:
    cv2.imshow('Image Processing', gray_modified)

# TODO: remove this line!
cv2.waitKey(0)

# window cleanup
cv2.destroyAllWindows()
