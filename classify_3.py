import os
import numpy as np
import cv2
import shutil

def func_filter_dir(directory):
    try:
        for (dirpath, dirnames, filenames) in os.walk(directory + '/cache'):
            for f in filenames:
                f_path = os.path.join(dirpath, f)
                variable = filter(f_path)
                if variable > 1:
                    shutil.move(f_path, directory+'/Claras/')
    except NameError as erro:
        print(erro)

def filter(directory):
    img = cv2.imread(directory)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_bin = cv2.threshold(img_gray, 75, 255, cv2.THRESH_BINARY)[1]

    result = np.median(img_bin)

    return result
if __name__ == "__main__":
    func_filter_dir('C:/Users/willianmoreira/Desktop/teste/van/')