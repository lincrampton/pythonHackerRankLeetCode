'''Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.  (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).  Find the minimum element.  The array may contain duplicates.'''


# my solution -- beats 85.87% of python solutions for runtime
# and is probably close to the minimum of complexity

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	return min(nums)

 -=-=-
# their solution.  should work better for very large array
# but mine passed beating 85.87% runtimes
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        while i < j:
            mid = i + (j-i) / 2
            if nums[mid] > nums[j]:
                i = mid+1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                j -= 1
        return nums[j]
