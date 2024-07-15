import math
import numpy as np
import talib


close = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sma_length = 5

def get_mean(array):
    total = 0
    for i in range(0, len(array)):
        total += array[i]
    return total / len(array)

def get_stddev(array):
    total = 0
    mean = get_mean(array)
    for i in range(0, len(array)):
        minus_mean = math.pow(array[i] - mean, 2)
        total += minus_mean

    return math.sqrt(total / (len(array) - 1))

std = get_stddev(close[-sma_length:])
print (std)

# Convert the close list to a NumPy array of type double
close_array = np.array(close, dtype=np.double)

std2_p = talib.STDDEV(close_array, sma_length)
print (std2_p[-1])

# convert std2_p to sample standard deviation
std2_s = std2_p * math.sqrt(sma_length / (sma_length - 1))
print (std2_s[-1])

