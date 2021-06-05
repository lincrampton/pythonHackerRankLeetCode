'''MAXIMUM PERFORMANCE OF A TEAM

Solution
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.'''

def maxPerformance(n, speed, efficiency, k: int):
    
    from heapq import heapify, heappush, heappop
    
    MOD = 10 ** 9+7     # return result in mod 10**9+7
    
    heap =[]
    heapify(heap)
    
    result, gesampt = 0, 0
    arr = [[efficiency[i], speed[i]] for i in range(len(speed))]
    arr.sort(reverse=True)
        
    for wirksam, schnell in arr:
        heappush(heap,schnell)
        gesamt += schnell
        
        if len(heap) > k:
            gesampt -= heappop(heap)
        
        result = max(result, gesampt*wirksam)
        
    return result % MOD

#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3768/
