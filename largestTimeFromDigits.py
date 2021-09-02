'''Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit 
exactly once. 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is 
between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, 
return an empty string.'''

# import itertools
from itertools import permutations

class Solution(object):
    def largestTimeFromDigits(arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        result = ""
        for i in range(len(arr)):
            arr[i] *= 1
        arr.sort(reverse=True)
        
        for h1, h2, m1, m2 in permutations(arr):
            hours, mins = (10*h1 + h2), (10*m1 + m2)
            if hours>=0 and hours<24 and mins>=0 and mins<60:
                result = "{:02}:{:02}".format(hours, mins)
                break
        return result
    
    def largestTimeFromDigitsX(arr):
        return max((f"{a}{b}:{c}{d}" for a,b,c,d in permutations(arr) 
                   if f"{a}{b}" < "24" and f"{c}{d}" < "60"), default = "") 
    
    in1 = [0,0,1,0]
    out1 = "10:00"
    print(largestTimeFromDigits(in1), "should equal", out1, "and should equal", largestTimeFromDigitsX(in1))
    
    
    in2 = [0,9,9,1]
    out2 = "19:09"
    print(largestTimeFromDigits(in2), "should equal", out2,"and should equal", largestTimeFromDigitsX(in2))
    
    in3 = [2,9,9,2]
    out3 = ""
    print(largestTimeFromDigits(in3), "should equal", out3,"and should equal", largestTimeFromDigitsX(in3))

