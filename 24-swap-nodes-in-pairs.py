'''https://leetcode.com/problems/swap-nodes-in-pairs/'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is not None and head.next is not None:
            temp = head.next.next
            head.next.next = head
            head = head.next
            head.next.next = temp
            head.next.next = self.swapPairs(head.next.next)
        return head
        