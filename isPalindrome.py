'''Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  For the purpose of this problem, we define empty string as valid palindrome.'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) < 2:
            return True
    
        import re
        s = re.sub(r'[^a-z\d]','',s.lower())
        return (s == s[::-1]) 
