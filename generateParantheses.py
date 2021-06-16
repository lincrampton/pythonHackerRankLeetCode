class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result=[]
        if not n: return result
                    
        result = [[] for _ in range(n+1)]
        result[0] = ['']
        for i in range(1, n+1):
            for j in range(i):
                res1 = result[j]
                res2 = result[i-j-1]
                for k1 in res1:
                    for k2 in res2:
                        result[i].append('(' + k1 +')' + k2)
        return result[n]
