class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        if not nums: return False
        
        len_nums = len(nums)
        deck = deque([len_nums-1])
        for i in range( len_nums-2, -1, -1):
            if deck[0] - i > k:
                deck.popleft()
            nums[i] += nums[deck[0]]
            while len(deck) and nums[deck[-1]] <= nums[i]:
                deck.pop()
            deck.append(i)
        return nums[0]
    
    
#         len_nums = len(nums)
#         if len_nums < 2: return True
        
#         last_backwards = len_nums- 1  # the last entry, and we will be running backwards
        
#         for i in range (len_nums-2, -1, -1):
#             if nums[i] >= last_backwards -i:
#                 last_backwards == i
                
                
#         return last_backwards == 0   # implying we have succesfully jumped backwards to the end
