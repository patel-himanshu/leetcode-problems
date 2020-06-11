# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/

"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
    (1) Insert a character
    (2) Delete a character
    (3) Replace a character

Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: 
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
intention
execution
Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: 
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
"""

class Solution:
    def minDistance(self, word1, word2): # minDistance(self, word1: str, word2: str) -> int
        l1, l2 = len(word1), len(word2)
        table = [[0]*(l2+1) for _ in range(l1+1)]

        for i in range(1, l1+1):
            table[i][0] = i
        for j in range(1, l2+1):
            table[0][j] = j

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
        return table[-1][-1]

inputs = [
    ['horse', 'ros'],
    ['intention', 'execution']
]
outputs = [3, 5]

S = Solution()
for i in range(len(outputs)):
    print('Case {}: {}'.format(i+1, S.minDistance(inputs[i][0], inputs[i][1]) == outputs[i]))