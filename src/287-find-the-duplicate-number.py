'''https://leetcode.com/problems/find-the-duplicate-number/'''

#Solution 1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]

#Solution 2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        
        finder = nums[0]
        while finder!=slow:
            finder = nums[finder]
            slow = nums[slow]
        return finder
        