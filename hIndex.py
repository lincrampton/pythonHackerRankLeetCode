Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if not citations:
            return 0

	citations.sort()
    
        H, cites_len = 0, len(citations) 
        for i, cites_count in enumerate(citations):
            H = max(H, min(cites_len - i, cites_count)) 
        return H


class SolutionSomeoneElse:
    def hIndex(self, citations: List[int]) -> int:
    	return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))


class SolutionAnotherSomeone:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort( reverse = True )
        
        # find first index where citation smaller or equal to array index            
        for idx, citation in enumerate(citations):
            if idx >= citation:
                return idx
        
        return len(citations)

testCase1 = [1,2,3,4,5]
ans1 = 3

testCase2 = [2,1]
ans2 = 1
