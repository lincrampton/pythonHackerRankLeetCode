'''Design a data structure that supports the following two operations: void addWord(word) bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.'''

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class WordDictionary:
    
    from collections import defaultdict

    def __init__(self):
        """ Initialize your data structure here.  """
        self.worter = defaultdict(list)
        

    def addWord(self, word: str) -> None:
        """ Adds a word into the data structure.  """
        self.worter[len(word)].append(word)

        
    def search(self, word: str) -> bool:
        """ Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.  """

        wortlange = len(word)
        
        if wortlange not in self.worter:
            return False
  
        for jedes_zeichen in self.worter[wortlange]:
            bisher = True
            for c in range(wortlange):
                if (jedes_zeichen[c]!=word[c] and word[c] != '.'):
                    bisher = False
                    break
            if bisher:
                return True
