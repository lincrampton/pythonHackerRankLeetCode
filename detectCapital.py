'''Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in word are capitals ("USA") OR All letters in word are not capitals ("leetcode") OR 
Only the first letter in this word is capital ("Google").
'''
class SolutionAug1:
    def detectCapitalUse(self, word: str) -> bool:
        
        word_len = len(word)
        
        if word_len < 2:
            return True
        
        if all(letter.islower() for letter in word):
            return True
        if all(letter.isupper() for letter in word):
            return True
        if ( word[0].isupper() and all(letter.islower() for letter in word[1:]) ):
            return True
        return False
    
input1true = "Google"
input2false = "gooGle"
input3true = "UNIX"

Sol = SolutionAug1()
print("true examples are:", Sol.detectCapitalUse(input1true), Sol.detectCapitalUse(input3true))
print("expecting false here:", Sol.detectCapitalUse(input2false))
