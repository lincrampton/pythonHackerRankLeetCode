'''You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.'''''
linzStr = " 2 3 4 5"
linzLst = list(map(int,linzStr.split()))
linzLst = linzLst[::-1]
import numpy as np
linzNp = np.array(linzLst, float)
print(linzNp)
