'''Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231. 
Find the maximum result of ai XOR aj, where 0 ≤ i, j < n. Could you do this in O(n) runtime?'''
class Solution16sept:
    def findMaximumXOR(self, nums):
        maxXOR, max_lenB = 0, len(bin(max(nums)))-2  # lose the initial '0b'

        for pref_lenB in range(1, max_lenB+1):
            maxXOR <<= 1
            currXOR = maxXOR | 1
            
            bshift = max_lenB - pref_lenB
            prefixes = {n >> bshift for n in nums}  
            
            passender = any(currXOR ^ prefix in prefixes for prefix in prefixes)
            maxXOR |= passender
        return maxXOR
ip1 = [3, 10, 5, 25, 2, 8]
op1 = 28
Sol = Solution16sept()
print(Sol.findMaximumXOR(ip1), op1)
