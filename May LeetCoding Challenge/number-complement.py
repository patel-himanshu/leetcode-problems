class Solution:
    def findComplement(self, num: int) -> int:
        complement = ''
        for i in format(num, 'b'):
            if i=='0':
                complement += '1'
            else:
                complement += '0'
        return int(complement,2)