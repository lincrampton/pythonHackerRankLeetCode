''' Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time. '''

    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums: return 0
        
        nums_len = len(nums)
        if nums_len < 2: return nums_len
        
        uniques = set(nums)   # the unique set of digits
        
        max_seq_len = 0       # the overall maximum sequence length
        for nummer in uniques:
            seq_len = 1       # the length of this sequence
            if nummer-1 not in uniques:
                while nummer+1 in uniques:
                    nummer += 1
                    seq_len += 1
                max_seq_len = max(max_seq_len, seq_len)
        
        return max_seq_len
        
