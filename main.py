import numpy as np
import cv2

# def read_image(filename):
#   """Reads an image file and returns a NumPy array of the pixel values."""
#   img = Image.open(filename)
#   img_arr = np.array(img)
#   #print(img_arr)
#   return img_arr

def read_image(filename):
  """Reads an image file and returns a NumPy array of the pixel values."""
  img = cv2.imread(filename)
  return img

def get_color_points(img_arr):
  """Returns a matrix of width, height, and color values for each pixel."""
  width, height, _ = img_arr.shape   # width: 794, height: 1102
  print("w, h: ", width, height)
  #points = np.zeros((width, height, 4))
  for x in range(width):
    for y in range(height):
      color = img_arr[y, x]
      print(x, y, color)
      #points[x, y] = (x, y, color)
  #return points

if __name__ == "__main__":
  filename = "heatmap_spain.png"    # 1102 x 794
  img_arr = read_image(filename)
  points = get_color_points(img_arr)
  print(points)