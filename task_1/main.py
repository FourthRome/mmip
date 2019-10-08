# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import sys
import functions as fun

IMG_FOLDER = "../img"
IMG_PATH = IMG_FOLDER + "/" + "lena.bmp"
OUTPUT_IMG_PATH = "result.bmp"

if __name__ == "__main__":
    img = Image.open(IMG_PATH)
    contents = np.array(img)
    grayscale = False
    if grayscale and contents.ndim > 2:
        contents_gray = [[int(sum(contents[y, x]) / contents.shape[2])
                          for x in range(contents.shape[1])]
                          for y in range(contents.shape[0])]
        contents = np.array(contents_gray, dtype=contents.dtype)

    # result = fun.mirror(contents, False)
    # result = fun.rotate(contents, 270, clockwise=True)
    result = contents
    
    if grayscale:
        Image.fromarray(result, mode="L").save(OUTPUT_IMG_PATH)
    else:
        Image.fromarray(result, mode="RGB").save(OUTPUT_IMG_PATH)
