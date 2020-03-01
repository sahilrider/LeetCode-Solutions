'''https://leetcode.com/problems/palindrome-linked-list/'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1
# Time Complexity - O(n)
# Space Complexity - O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = []
        while head:
            s+= [head.val]
            head = head.next
        return s==s[::-1]

# Solution 1
# Time Complexity - O(n)
# Space Complexity - O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #find mid element
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse second half
        prev = None #will store the reversed array
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        #compare first half and reversed second half
        while head and prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        return True
        
        
