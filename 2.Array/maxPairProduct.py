# How to find maximum product of two integers in an array where all elements 
# are positive.

import numpy as np
myArray = np.array([1,20,30,44,5,56,57,89,10,31,12,13,14,35,16,27,58,19,21])

def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i]) + " " + str(array[j])
    print(pairs)
    print(maxProduct)
    
    
findMaxProduct(myArray)