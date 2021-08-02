'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for n in range(len(nums)):
            delta = target - nums[n]
            if delta in dict:
                return [n, dict[delta]]
            else:
                dict[nums[n]] = n
