'''Given a column title as appear in an Excel sheet, return its corresponding column number.  E.g., "A"->1, "AB"->28, "ZY"->701'''


class Solution:
    def titleToNumber(self, s: str) -> int:
    	ltr_offset = ord("A") - 1
    	str_len = len(s)
  	col_num = 0
    
    	for str_pos in range(str_len):
       		col_num += 26**(str_len-1-str_pos) * (ord(s[str_pos])-ltr_offset)
    
    	return col_num

# str_pos -> position of letter in string
# col_num
