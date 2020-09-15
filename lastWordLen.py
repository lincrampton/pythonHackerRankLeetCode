'''Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.  If the last word does not exist, return 0.'''

class Solution:
            # # beats 53% on compute
        # return len(s.rstrip().split(" ")[-1])

        # # beats 53% on compute
        # res, s = 0, s.rstrip()
        # while res < len(s) and s[-(res+1)].isalpha():
        #     res += 1
        # return res

        # # beats 17% on compute
        # end = len(s) - 1
        # while end > 0 and s[end] == " ":
        #     end -= 1
        # beg = end
        # while beg >= 0 and s[beg] != " ":
        #     beg -= 1
        # return end - beg

        # # beats 17% on compute
        # str_split = s.split()
        # return len(str_split[-1]) if str_split else 0

        # # beats 8% on compute
        # return len(s.split()[-1]) if s.split() else 0
