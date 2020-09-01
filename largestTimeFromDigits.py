'''Given an array of 4 digits, return the largest 24 hour time that can be made.  The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.  Return the answer as a string of length 5.  If no valid time can be made, return an empty string.'''

class Solution1sept:
    def largestTimeFromDigits(self, A): 
        MAX_HOURS, MAX_MINUTES = 23, 59
        A.sort()
        for h in range(MAX_HOURS, -1, -1):
            for m in range(MAX_MINUTES, -1, -1):
                t = [h//10, h%10, m//10, m%10]
                times = sorted(t)
                if times == A:
                    hours=10*t[0]+t[1]
                    minutes=10*t[2]+t[3]
                    return "{:02}:{:02}".format(hours, minutes)
        return ""
Sol = Solution1sept()
print("17:11 answer is:", Sol.largestTimeFromDigits([1,1,1,7]))
print("6:26 answer is:", Sol.largestTimeFromDigits([2,0,6,6]))
print("4,30 answer is:", Sol.largestTimeFromDigits([0,0,3,4]))
print("13:30 answer is:", Sol.largestTimeFromDigits([0,1,3,3]))
print("23:51 answer is:", Sol.largestTimeFromDigits([2,1,5,3]))
print("00:00 answer is:", Sol.largestTimeFromDigits([0,0,0,0]))
print("09:09 answer is:", Sol.largestTimeFromDigits([9,9,0,0]))
print("nada answer is:", Sol.largestTimeFromDigits([5,5,5,5]))
print("19:06 answer is:", Sol.largestTimeFromDigits([1,9,0,6]))
print("nada answer is:", Sol.largestTimeFromDigits([7,9,0,6]))
print("nada answer is", Sol.largestTimeFromDigits([7,9,2,3]))
