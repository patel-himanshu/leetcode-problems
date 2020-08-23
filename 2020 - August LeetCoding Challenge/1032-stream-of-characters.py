# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3434/

"""
Implement the StreamChecker class as follows:
    (1) StreamChecker(words): Constructor, init the data structure with the given words.
    (2) query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest,
        including this letter just queried) spell one of the words in the given list.

Example:
    StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
    streamChecker.query('a');          // return false
    streamChecker.query('b');          // return false
    streamChecker.query('c');          // return false
    streamChecker.query('d');          // return true, because 'cd' is in the wordlist
    streamChecker.query('e');          // return false
    streamChecker.query('f');          // return true, because 'f' is in the wordlist
    streamChecker.query('g');          // return false
    streamChecker.query('h');          // return false
    streamChecker.query('i');          // return false
    streamChecker.query('j');          // return false
    streamChecker.query('k');          // return false
    streamChecker.query('l');          // return true, because 'kl' is in the wordlist

Note:
    (1) 1 <= words.length <= 2000
    (2) 1 <= words[i].length <= 2000
    (3) Words will only consist of lowercase English letters.
    (4) Queries will only consist of lowercase English letters.
    (5) The number of queries is at most 40000.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False
        
class RevTrie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        temp = self.root
        
        for i in range(-1, -len(word)-1, -1):
            if word[i] not in temp.children:
                temp.children[word[i]] = TrieNode()
            temp = temp.children[word[i]]
        
        temp.word_end = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = ''
        self.rev_trie = RevTrie()
        
        for word in words:
            self.rev_trie.insert(word)

    def query(self, letter: str) -> bool:
        self.letters += letter
        temp = self.rev_trie.root

        for i in self.letters[::-1]:
            if i not in temp.children:
                 break
            temp = temp.children[i]
            if temp.word_end:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)