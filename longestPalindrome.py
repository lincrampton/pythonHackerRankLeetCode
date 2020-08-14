'''Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.'''

class Solution14aug:
    def longestPalindrome(self, s):
        
        s_len = len(s)
        if s_len<2:
            return s_len
        
        import collections
        odds = sum((v & 1) for v in collections.Counter(s).values())
        return  s_len - odds + 1 if odds else s_len


    
test1 = "ZCccccdd"
answer1 = 7
Sol=Solution14aug()
print(Sol.longestPalindrome(test1))
