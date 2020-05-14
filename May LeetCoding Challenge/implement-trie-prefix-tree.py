# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3329/

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.total = 0

class Trie:
    def __init__(self):
        self.root = self.createNode()
    
    def createNode(self):
        return TrieNode()
    
    def getIndexValue(self, letter):
        return ord(letter) - ord('a')
    
    def insert(self, word):
        temp = self.root
        for i in range(len(word)):
            index = self.getIndexValue(word[i])
            # print(self.root)
            # print(len(self.root.children))
            # print(self.root.total)
            # print(word[i], index)
            if not temp.children[index]:
                temp.children[index] = self.createNode()
            temp = temp.children[index]
        temp.total += 1
        
    def search(self, word):
        temp = self.root
        for i in range(len(word)):
            index = self.getIndexValue(word[i])
            if not temp.children[index]:
                return 0
            temp = temp.children[index]
        return 1 if temp.total else 0

    def startsWith(self, prefix):
        temp = self.root
        for i in range(len(prefix)):
            index = self.getIndexValue(prefix[i])
            if not temp.children[index]:
                return 0
            temp = temp.children[index]
        return 1

# T = int(input())
# for t in range(T):
#     N = int(input())
#     sentence = input().split()
#     A = input()
#     T = Trie()
#     for i in sentence:
#         T.insert(i)
#     print(T.search(A))

words = 'the a there answer any by bye their'
testcases1 = ['the', 'a', 'theer', 'answe', 'theri'] # Testcases for 'search' method
testcases2 = ['th', 'an', 'thi', 'by', 'be'] # Testcases for 'startsWith' method

S = words.split()
T = Trie()

for i in S:
    T.insert(i)
print('Searching Results: ', end='')
for j in testcases1:
    print(T.search(j), end='')


print('\nStartsWith Results: ', end='')
for k in testcases2:
    print(T.startsWith(k), end='')

print()