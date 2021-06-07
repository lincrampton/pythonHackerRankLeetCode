'''You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        len_cost=len(cost)
        
        if not cost or len_cost==1: return 0
        if len_cost == 2: return min(cost[0], cost[1])
        
        for s in range(2, len_cost):
            cost[s] += min(cost[s-1], cost[s-2])
        return min(cost[-1], cost[-2])
