'''Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.'''

class Solution11sep:
    def maxProduct(self, nums):
        
        nums_len = len(nums)
        maxes, mins = [0]*nums_len, [0]*nums_len      # arrays of maxes and mins
        maxes[0], mins[0] = nums[0], nums[0]          # seed array with something to multiply
        
        for n in range(1, nums_len):
            maxes[n] = max(nums[n], maxes[n-1]*nums[n], nums[n]*mins[n-1])    
            mins[n] = min(nums[n], maxes[n-1]*nums[n], nums[n]*mins[n-1])    # because have possible neg num
            
        return max(maxes)

Sol = Solution11sep()
print(Sol.maxProduct([0, 2, -1, 24, 7]))
