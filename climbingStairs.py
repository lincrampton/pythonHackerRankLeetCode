SolutionF:
    def climbStairs(self, n):

        fibCache = {}          # cache fibonacci numbers & avoid recalculating
        def fibPlus(n):
            if n < 3:
                return n
            elif n in fibCache:
                return fibCache[n]
            else:
                fibCache[n] = fibPlus(n - 1) + fibPlus(n - 2)
                return fibCache[n]
        return fibPlus(n)
    
    
Sol = SolutionF()
print(Sol.climbStairs(4))


''' Calculating Fibonacci numbers takes too long 
def fib(n):   # Fibonacci
    if n<2:
        return n
    return fib(n-1) + fib(n-2) '''
