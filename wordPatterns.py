'''Given a pattern and a string str, find if str follows the same pattern.Here follow means a full match, 
such that there is a bijection between a letter in pattern and a non-empty word in str.'''
class Solution7sept:
    def wordPattern(self, pattern, str):
        
        list_of_words = str.split()
        if len(list_of_words) != len(pattern):
            return False
        
        symbols, words = {}, {}
        for letter, word in zip(pattern, list_of_words):
            if letter not in symbols:
                if word in words: 
                    return False     # ynyn, 'yes','yes', 'yes', yes'
                else:
                    symbols[letter] = word
                    words[word] = letter
            elif symbols[letter] != word: 
                return False    # yyyy, 'yes', 'no', 'yes', 'no'
            
            
        return True

Sol = Solution7sept()

pattern1 = "abba"
str1 = "dog cat cat dog"
output1 = True

pattern2 = "abba"
str2 = "dog cat cat fish"
output2 = False

pattern3 = "aaaa"
str3 = "dog cat cat dog"
output3 = False

pattern4 = "abba"
str4 = "dog dog dog dog"
output4 = False

print(Sol.wordPattern(pattern1, str1), output1)
print(Sol.wordPattern(pattern2, str2), output2)
print(Sol.wordPattern(pattern3, str3), output3)
print(Sol.wordPattern(pattern4, str4), output4)
