from PIL import Image
import numpy as np

ROT_TYPES = { i: name for (i, name) in enumerate(["RIGHT_DOWN", "UP_RIGHT", "LEFT_UP", "DOWN_LEFT"])}


def mirror(image, horizontally=True):
    output = image.copy()
    height = image.shape[0]
    width = image.shape[1]
    
    for y in range(height):
        for x in range(width):
            if horizontally:
                output[y][x] = image[y][width - x - 1]
            else:
                output[y][x] = image[height - y - 1][x]            

    return output


def rotate(image, degree=0, clockwise=False, buf=None):
    height = image.shape[0]
    width = image.shape[1]

    if clockwise:
        degree = -degree
    rtype = degree % 360 // 90

    # Alternative implementation to be discussed
    
    if ROT_TYPES[rtype] == "RIGHT_DOWN":
        output = image.copy()
        return output
    elif ROT_TYPES[rtype] == "LEFT_UP":
        output = np.zeros(image.shape, dtype=image.dtype)
    else:
        new_shape = list(image.shape)
        new_shape[0], new_shape[1] = image.shape[1], image.shape[0]
        output = np.zeros(new_shape, dtype=image.dtype)

    for y in range(height):
        for x in range(width):
            if ROT_TYPES[rtype] == "UP_RIGHT":
                output[width - x - 1][y] = image[y][x]
            elif ROT_TYPES[rtype] == "LEFT_UP":
                output[height - y - 1][width - x - 1] = image[y][x]
            elif ROT_TYPES[rtype] == "DOWN_LEFT":
                output[x][height - y - 1] = image[y][x]
    return output

def sobel(image, horizontal=True):
    pass

def median(image, rad=0):
    pass

def gauss(image, sigma=1):
    pass

def gradient(image, sigma=1):
    pass