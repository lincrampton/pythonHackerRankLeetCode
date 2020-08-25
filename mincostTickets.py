'''In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways: 
   a 1-day pass is sold for costs[0] dollars;
   a 7-day pass is sold for costs[1] dollars;
   a 30-day pass is sold for costs[2] dollars.

Return the minimum number of dollars you need to travel every day in the given list of days.'''

class Solution25aug:
    def mincostTickets(self, days, costs):
        last_day = days[-1]
        days = set(days)
        dp = [0 for _ in range(last_day+1)]
        
        for d in range(1, last_day+1):
            
            if d not in days:
                dp[d] = dp[d-1]
                continue
                
            cost_1day = dp[d-1] + costs[0]
            cost_7days = dp[max(d-7, 0)] + costs[1]
            cost_30days = dp[max(d-30, 0)] + costs[2]
            dp[d] = min(cost_1day, cost_7days, cost_30days)
            
        return dp[-1]
        
days1 = [1,2,3,4,5,6,7,8,9,10,30,31]
costs1 = [2,7,15]
answer1 = 17

days2 = [1,4,6,7,8,20]
costs2 = [2,7,15]
answer2 = 11

Sol = Solution25aug()
print(Sol.mincostTickets(days1,costs1), "\t should equal", answer1)
print(Sol.mincostTickets(days2,costs2), "\t should equal", answer2)
