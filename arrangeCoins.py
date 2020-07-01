''' You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
    Given n, find the total number of full staircase rows that can be formed.
    n is a non-negative integer and fits within the range of a 32-bit signed integer.'''

class SolutionAC:
#     def arrangeCoins(self, n: int) -> int:
    def arrangeCoins(n):
        # arithmetic progression is k*(k+1)/2
        # if you follow the math, you want the answer to be <= k(k+1)/2
        import math
        return int(math.sqrt(2*n + 1/4) - 1/2)

# test cases
input1=5
output1=2
input2=8
output2=3

Sol = SolutionAC
print(Sol.arrangeCoins(input1),'=', output1)
print(Sol.arrangeCoins(input2),'=', output2)

