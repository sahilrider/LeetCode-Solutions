'''https://leetcode.com/problems/rotate-list/'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        curr = head
        ctr = 1
        while curr.next:
            curr = curr.next
            ctr+=1
        curr.next = head
        
        k = k%ctr
        for i in range(ctr - k):
            curr = curr.next
        ans = curr.next
        curr.next = None
        return ans
        