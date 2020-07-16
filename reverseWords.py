# given a string, return words in reverse order
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
