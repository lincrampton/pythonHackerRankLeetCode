class Solution27august:
    def findRightInterval(self, intervals):
        
        lfind = sorted(list(enumerate(intervals)), key = lambda x:x[1][0])
        n, res = len(lfind), []
        
        for _, r in intervals:
            i, j = 0, n
            while i < j:
                mid = (i+j)//2
                if lfind[mid][1][0] < r:
                    i = mid + 1
                else:
                    j = mid
            res.append(lfind[i][0] if i != n else -1)
        return res
    
Sol = Solution27august()
input1 = [ [1,2] ]
output1 = [-1]
input2 = [ [3,4], [2,3], [1,2] ]
output2 = [-1, 0, 1]
input3 = [ [1,4], [2,3], [3,4] ]
output3 = [-1, 2, -1]

print (Sol.findRightInterval(input1), "?==?", output1)
print (Sol.findRightInterval(input2), "?==?", output2)
print (Sol.findRightInterval(input3), "?==?", output3)
