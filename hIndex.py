Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if not citations:
            return 0
    
        h, len_cites = 0, len(citations) 
        for i, cit_count in enumerate(citations):
            h = max(h, min(len_cites - i, cit_count)) 
        return h

test_case = [1,2,3,4,5]
answer = 3
