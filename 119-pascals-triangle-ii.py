'''https://leetcode.com/problems/pascals-triangle-ii/'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        ans = [1]
        for i in range(1, rowIndex+1):
            for j in range(i-1, 0, -1):
                ans[j] +=ans[j-1]
            ans.append(1)
            # print(i, ans)
        return ans
        