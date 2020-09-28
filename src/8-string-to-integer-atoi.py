'''https://leetcode.com/problems/string-to-integer-atoi/'''

class Solution:
    def myAtoi(self, str: str) -> int:
        intmax = 2**31 - 1
        intmin = -2**31
        
        pointer, result, sign = 0, 0, 1
        if not str:
            return 0
        #strip whitespace
        while pointer<len(str) and str[pointer]==' ':
            pointer+=1
        #check sign
        if pointer<len(str):
            if str[pointer]=='-':
                sign = -1
                pointer+=1
            elif str[pointer]=='+':
                sign = 1
                pointer+=1
            elif str[pointer].isdigit():
                sign = 1
            else:
                return 0
        
        while pointer<len(str) and str[pointer].isdigit():
            digit = int(str[pointer])
            
            #check overflow
            if (result>intmax//10) or (result==intmax//10 and digit>intmax%10):
                #overflow
                return intmax if sign==1 else intmin
            else:
                result = result*10 + digit
            pointer+=1
        return result*sign