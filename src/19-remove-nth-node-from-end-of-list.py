'''https://leetcode.com/problems/remove-nth-node-from-end-of-list/'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1, p2 = head, head
        for i in range(n):
            p2 = p2.next
        if p2 is None:
            return head.next
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head
        