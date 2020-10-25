'''https://leetcode.com/problems/number-complement/'''

class Solution:
    def findComplement(self, num: int) -> int:
        bitlength = len(bin(num)[2:])
        return num^(2**bitlength - 1)
        