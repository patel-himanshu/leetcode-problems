class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for i in J:
            total += S.count(i)
        return total