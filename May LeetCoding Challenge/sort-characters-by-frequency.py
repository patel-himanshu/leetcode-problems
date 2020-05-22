# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3337/

'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
    Input: "tree"
    Output: "eert"
    Explanation:
        'e' appears twice while 'r' and 't' both appear once.
        So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
    Input: "cccaaa"
    Output: "cccaaa"
    Explanation:
        Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
        Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
    Input: "Aabb"
    Output: "bbAa"
    Explanation:
        "bbaA" is also a valid answer, but "Aabb" is incorrect.
        Note that 'A' and 'a' are treated as two different characters.
'''

from collections import Counter
from operator import itemgetter

class Solution:
    def frequencySort(self, s):             # frequencySort(self, s: str) -> str
                    # Input = 'tree'

        c = Counter(s)
                    # Returns Counter({'e': 2, 't': 1, 'r': 1})

        c_keys = list(c.keys())             # List which stores keys from the Counter(s)
                    # Returns ['e', 't', 'r']
    
        c_values = list(c.values())         # List which stores values from the Counter(s)
                    # Returns [2,1,1]

        # Sorts the zipped list, on the basis of frequency of characters, and then reverses it
        s_sorted = sorted(zip(c_keys, c_values), key = itemgetter(1), reverse=True)
                    # Returns [('e', 2), ('t', 1), ('r', 1)]

        # Creates a new list which stores each character whose length is equal to its frequency 
        s_joined = list(map(lambda i: i[0]*i[1], s_sorted))
                    # Returns ['ee', 't', 'r']
            
        return ''.join(s_joined)
                    # Returns 'eetr'

inputs = ['tree', 'cccaaa', 'Aabb']
outputs = [
    ['eetr', 'eert'],
    ['cccaaa', 'aaaccc'],
    ['bbAa', 'bbaA']
]

S = Solution()
for i in range(len(inputs)):
    if S.frequencySort(inputs[i]) in outputs[i]:
        print('Case {} passed'.format(i+1))
    else:
        print('Case {} failed'.format(i+1))
