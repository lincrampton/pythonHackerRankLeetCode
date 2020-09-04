'''A string S of lowercase English letters is given. We want to partition this string into as many parts as possible
so that each letter appears in at most one part, and return a list of integers representing the size of these parts.'''
class Solution4sept:
    def partitionLabels(self, S):

        d = {c: i for i, c in enumerate(S)}        

        begins, ends = 0, 0
        result = []
        
        for i, char in enumerate(S):
            ends = max(ends, d[char])
            if i == ends:
                result.append(ends-begins+1)
                begins = ends + 1
                
        return result

Sol = Solution4sept()
input1 = "ababcbacadefegdehijhklij"
outpu1 = [9,7,8]
print(Sol.partitionLabels(input1))
