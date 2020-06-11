# Question: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3332/

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
    Input: s: "cbaebabacd" p: "abc"
    Output: [0, 6]
    Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

    Input: s: "abab" p: "ab"
    Output: [0, 1, 2]
    Explanation:
        The substring with start index = 0 is "ab", which is an anagram of "ab".
        The substring with start index = 1 is "ba", which is an anagram of "ab".
        The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

from collections import Counter

class Solution:
    def findAnagrams(self, s, p):   # findAnagrams(self, s: str, p: str) -> List[int]
        answer = []
        p_counter = Counter(p)
        flag = 0

        for i in range(len(s)-len(p)+1):
            substring = s[i:i+len(p)]

            if flag:
                if s[i-1] == s[i+len(p)-1]:
                    answer.append(i)
                else:
                    flag = 0
            
            else:
                new_counter = Counter(substring)
                if new_counter == p_counter:
                    answer.append(i)
                    flag = 1
        
        return answer

test_cases = [
    ['cbaebabacd', 'abc'],
    ['abab', 'ab']
]

S = Solution()
for i in test_cases:
    print(S.findAnagrams(i[0], i[1]))