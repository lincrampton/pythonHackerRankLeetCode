'''Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
Note:  All numbers will be positive integers.  The solution set must not contain duplicate combinations.'''
class Solution12sep:
    def combinationSum3(self, k, n):
        import itertools
        return [c for c in itertools.combinations(list(range(1,10)),r=k) if sum(c) == n] 
    
Sol = Solution12sep()

k1 = 3
n1 = 9
out1 = [[1,2,6], [1,3,5], [2,3,4]]
print('get', Sol.combinationSum3(k1, n1), '... expect', out1)

k2 = 3
n2 = 7
out2 = [[1,2,4]]
print('get', Sol.combinationSum3(k2, n2), '... expect', out2)
