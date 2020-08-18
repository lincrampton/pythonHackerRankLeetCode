'''Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K. Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid. You may return the answer in any order.
'''     
class Solution18aug:
    def numsSameConsecDiff(self, N, K):
    
        if N==1: 
            return list(range(10))
        if K==0:
            return [int(str(i) * N) for i in range(1, 10)]
        
        from collections import deque
        deck = deque(range(10))
        
        cnt = 1
        while cnt < N:
            temp_deck = deque()
            while deck:
                pivot = deck.popleft()
                if pivot==0:
                    continue
                num = pivot%10 
                
                for tail in {num + K, num - K}:
                    if 0<=tail<=9:
                        temp_deck.append(pivot*10 + tail)
                        
            deck = temp_deck
            cnt += 1
        return list(deck)


N1 = 3
K1 = 7
op1 = [181,292,707,818,929]

N2 = 2
K2 = 1
op2 = [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    
Sol = Solution18aug()
print(Sol.numsSameConsecDiff(N1,K1), 'should equal\n', op1)
print("\n", Sol.numsSameConsecDiff(N2,K2), 'should equal\n', op2)
