import numpy as np
import matplotlib.pyplot as plt
from math import factorial
import scipy.signal

# Pass in array
def lowPass(array, window_ratio=.1, poly_order=3):
    window = len(array)*window_ratio
    if window % 2 == 0:
        window -= 1
    filtered = scipy.signal.savgol_filter(array, window, poly_order)
    return filtered

def lowPassAllChars(chars, window_ratio=.1, poly_order=3):
    newDict = {}

    for ch, sc in chars.items():

        unzip = zip(*sc)
        print unzip[1]
        print len(unzip[1])
        print type(unzip[1])
        newDict[ch] = lowPass(unzip[1])


    return newDict
