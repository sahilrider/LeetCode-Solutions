'''https://leetcode.com/problems/merge-two-sorted-lists/'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Iterative Solution
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        while(l1 is not None and l2 is not None):
            if l1.val <=l2.val:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next
        while l1:
            l3.next = ListNode(l1.val)
            l3 = l3.next
            l1 = l1.next
        while l2:
            l3.next = ListNode(l2.val)
            l3 = l3.next
            l2 = l2.next
        return head.next

# Recursive Solution
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2