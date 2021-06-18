'''We are given an array nums of positive integers, and two positive integers left and right (left <= right).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.'''

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        result, low, mid = 0, 0, 0
        for num in nums:
            if num > right: mid = 0
            else:
                mid += 1
                result += mid
            if num >= left: low = 0
            else:
                low += 1
                result -= low
        return result
             
# Testing
a = [ 2, 1, 4, 3]
l = 2
r = 3
printf(countSubarrays(a, n, l, r), ' should equal 3.')
