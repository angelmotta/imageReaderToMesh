import cv2
import numpy as np

# Load the image using OpenCV
# heatmap_small.png is a 340x215
image = cv2.imread('./heatmap_small.png')

# Get the dimensions of the image
height, width, _ = image.shape
print("height:", height, "width:", width)
# Create a 2D array to store the color values
#color_array = np.empty((height, width, 3))

# Iterate over each pixel in the image
mimatrix = []

for y in range(height):
    mirow = []
    for x in range(width):
        # Get the color values for the pixel at (x, y)
        b, g, r = image[y, x]
        color = (int(b) + int(g) + int(r))/3
        alturaColor = 255 - color
        # print type of b,g,r
        #print(y, x, val)
        # print (x, y, z) for opengl
        #print(x/4, alturaColor/4, y/4)
        mirow.append((x/4, alturaColor/8, y/4))
    mimatrix.append(mirow)

temp = []
for row in range(height):
    for pixel in range(width):
        try:
            # do try catch to avoid error in last pixel
            a = np.array(mimatrix[row][pixel])
            b = np.array(mimatrix[row][pixel+1])
            c = np.array(mimatrix[row+1][pixel])
            p1 = b - a
            p2 = c - a
            n1 = np.cross(p1, p2)
            #temp.append((a, n1), (b, n1), (c, n1))
            print(a[0], a[1], a[2], n1[0], n1[1], n1[2])
            print(b[0], b[1], b[2], n1[0], n1[1], n1[2])
            print(c[0], c[1], c[2], n1[0], n1[1], n1[2])

            d = np.array(mimatrix[row+1][pixel+1])
            p1 = b - d
            p2 = c - d
            n2 = np.cross(p1, p2)
            #temp.append((b, n2), (c, n2), (d, n2))
            print(b[0], b[1], b[2], n2[0], n2[1], n2[2])
            print(c[0], c[1], c[2], n2[0], n2[1], n2[2])
            print(d[0], d[1], d[2], n2[0], n2[1], n2[2])
        except:
            pass
        
# Print the color values for each pixel
'''
for y in range(height):
    for x in range(width):
        print(f"Pixel at ({x}, {y}): B={color_array[y, x][0]}, G={color_array[y, x][1]}, R={color_array[y, x][2]}")
'''