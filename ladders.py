'''A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.'''


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words, letters = set(wordList), list(map(set, zip(*wordList)))
        queue, found = [[beginWord]], False
        paths = []
        while queue and endWord in words:
            next_queue = []
            for path in queue:
                word = path[-1]
                for i in range(len(word)):
                    for c in letters[i]:
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word == endWord:
                            paths.append(path + [next_word])
                        elif next_word in words:
                            next_queue.append(path + [next_word])
            queue = next_queue
            words -= set(map(lambda x: x[-1], queue))
            if paths:
                break
        return paths
