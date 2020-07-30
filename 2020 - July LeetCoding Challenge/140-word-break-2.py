# Question: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/548/week-5-july-29th-july-31st/3406/

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences.

Note:
    (1) The same word in the dictionary may be reused multiple times in the segmentation.
    (2) You may assume the dictionary does not contain duplicate words.

Example 1:
    Input: s = "catsanddog"; wordDict = ["cat", "cats", "and", "sand", "dog"]
    Output:
    [
    "cats and dog",
    "cat sand dog"
    ]

Example 2:
    Input: s = "pineapplepenapple"; wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    Output:
    [
    "pine apple pen apple",
    "pineapple pen apple",
    "pine applepen apple"
    ]
    Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
    Input: s = "catsandog"; wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: []
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        
        def DFS(s):
            if not s: return ['']
            if s not in memo:
                memo[s] = []
                for i in range(1, len(s)+1):
                    word = s[:i]
                    if word in wordDict:
                        ans_on_rem_word = DFS(s[i:])
                        for item in ans_on_rem_word:
                            memo[s].append(word + ' ' + item)
            return memo[s]
        
        DFS(s)
        return [ans[:-1] for ans in memo[s]]