# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/

"""
Given an array of strings, group anagrams together.

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
            [
            ["ate","eat","tea"],
            ["nat","tan"],
            ["bat"]
            ]

Note:
    (1) All inputs will be in lowercase.
    (2) The order of your output does not matter.
"""

from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        ans_index = -1
        length = len(strs)
        check = [0]*length
        count = [Counter(elem) for elem in strs]
        
        for i in range(length):
            if not check[i]:
                check[i] = 1
                ans.append([strs[i]])
                ans_index += 1

                
                for j in range(i, length):
                    if not check[j] and (count[i]==count[j]):
                        check[j] = 1
                        ans[ans_index].append(strs[j])
        
        return ans