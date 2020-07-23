'''Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        import collections
        num_array = collections.Counter(nums)
        
        ret_list = []
        num_dict = dict(num_array)
        for key in num_dict:
            if num_dict[key] == 1:
                ret_list.append(key)
                
        return ret_list
