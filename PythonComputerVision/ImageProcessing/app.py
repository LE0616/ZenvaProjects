import cv2
import numpy as np

# dummy function
def dummy(value):
  pass
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
  # apply filters
  # apply brightness and contrast
  # wait for keypress (milliseconds)
  key = cv2.waitKey(100) # returns an integer
  # ord converts integer to character
  if key == ord('q'):
    break
  # to save image
  elif key == ord('s'):
    pass

# TODO: remove this line!
cv2.waitKey(0)

# window cleanup
cv2.destroyAllWindows()
