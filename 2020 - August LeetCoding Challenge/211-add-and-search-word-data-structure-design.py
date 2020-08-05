# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3413/

"""
Design a data structure that supports the following two operations:
    (1) void addWord(word)
    (2) bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:
    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

Note: You may assume that all words are consist of lowercase letters a-z.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        temp = self.root
        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = TrieNode()
            temp = temp.children[letter]
        temp.word_end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. 
        A word could contain the dot character '.' to represent any one letter.
        """
        def backtrack(node, word):
            if not word:
                return node.word_end
            
            if word[0] == '.':
                for child in node.children.keys():
                    if backtrack(node.children[child], word[1:]):
                        return True
            else:
                if word[0] in node.children:
                    if backtrack(node.children[word[0]], word[1:]):
                        return True

        return backtrack(self.root, word)
        
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)