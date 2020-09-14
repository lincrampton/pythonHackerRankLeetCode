'''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.'''

class Solution14sep:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums) if nums else 0

        prev = curr = 0
        for num in nums:
            temp, prev = prev, curr
            curr = max(num+temp, prev)
        return curr

ip1 = [2,3,2]
op1 =  3

ip2 = [1,2,3,1]
op2 = 4

Sol = Solution14sep()
print(Sol.rob(ip1, 'should equal', op1)
print(Sol.rob(ip2, 'should equal', op2)

