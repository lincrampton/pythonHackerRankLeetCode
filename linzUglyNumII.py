'''Program finds n-th ugly number.  
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. '''

class SolutionJuly4:
    def linzUglyNum(self, n: int) -> int:

        if n == 1: return 1
        index2, index3, index5 = 0, 0, 0
        ugly = [0]*n
        ugly[0] = 1

        for i in range(1, n):
            ugly[i] = min(ugly[index2]*2, ugly[index3]*3, ugly[index5]*5)
            if ugly[i] == ugly[index2]*2: index2 += 1
            if ugly[i] == ugly[index3]*3: index3 += 1
            if ugly[i] == ugly[index5]*5: index5 += 1
        
        return ugly[n-1]

Sol = SolutionJuly4()
print(Sol.linzUglyNum(10), "should=12")
print(Sol.linzUglyNum(1), "should=1")
print(Sol.linzUglyNum(2), "should=2")
