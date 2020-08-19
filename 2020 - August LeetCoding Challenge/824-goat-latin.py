# Question: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3429/

"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:
    (1) If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
        For example, the word 'apple' becomes 'applema'.
    (2) If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
        For example, the word "goat" becomes "oatgma".
    (3) Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
        For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin. 

Example 1:
    Input: "I speak Goat Latin"
    Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:
    Input: "The quick brown fox jumped over the lazy dog"
    Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Notes:
    (1) S contains only uppercase, lowercase and spaces. Exactly one space between each word.
    (2) 1 <= S.length <= 150
"""

class Solution:
    def toGoatLatin(self, S: str) -> str:
        ans = []
        words = S.split()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        for i in range(len(words)):
            if words[i][0] in vowels:
                ans.append(words[i] + 'ma' + 'a'*(i+1))
            elif words[i][0] not in vowels:
                ans.append(words[i][1:] + words[i][0] + 'ma' + 'a'*(i+1))
        
        return ' '.join(ans)